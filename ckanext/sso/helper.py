# -*- coding: utf-8 -*-

import ckan.model as model
import json
import logging
import os
from six.moves.urllib.parse import urljoin
from base64 import b64encode, b64decode
from pylons import config
from keycloak.realm import KeycloakRealm

log = logging.getLogger(__name__)

class SSOHelper(object):

    def __init__(self):
        self.authorization_endpoint = config.get('ckan.sso.authorization_endpoint', None)
        self.client_id = config.get('ckan.sso.client_id', None)
        self.client_secret = config.get('ckan.sso.client_secret', None)
        self.realm = config.get('ckan.sso.realm', 'ckan')
        self.profile_username_field = config.get('ckan.sso.profile_username_field', None)
        self.profile_fullname_field = config.get('ckan.sso.profile_fullname_field', None)
        self.profile_email_field = config.get('ckan.sso.profile_email_field', None)
        self.profile_group_field = config.get('ckan.sso.profile_group_field', None)
        self.sysadmin_group_name = config.get('ckan.sso.sysadmin_group_name', None)
        realm = KeycloakRealm(server_url=self.authorization_endpoint, realm_name=self.realm)
        self.oidc_client = realm.open_id_connect(client_id=self.client_id,client_secret=self.client_secret)

    def identify(self, token):
        user_token = self.oidc_client.userinfo(token)
        # user_data = self.oidc_client.decode_token(user_token, '', options={ 'verify_signature': False })
        import jwt
        user_data = jwt.decode(token, '', False)
        try : email = user_data[self.profile_email_field]
        except :
            log.debug("Not Found Email.")
        try : user_name = user_data[self.profile_username_field]
        except :
            log.debug("Not Found User Name.")

        user = model.User.get(user_name)
        if user :
            return user.name
        user = None
        users = model.User.by_email(email)
        if len(users) == 1:
            user = users[0]
        if user is None:
            user = model.User(email=email)
        user.name = user_name
        if self.profile_fullname_field and self.profile_fullname_field in user_data:
            user.fullname = user_data[self.profile_fullname_field]
        if self.profile_group_field and self.profile_group_field in user_data:
            if self.sysadmin_group_name and self.sysadmin_group_name in user_data[self.profile_group_field]:
                user.sysadmin = True
            else:
                user.sysadmin = False
        model.Session.add(user)
        model.Session.commit()
        model.Session.remove()
        log.info('Add keycloak user into ckan database: %s'%user)
        return user.name
