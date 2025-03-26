# -*- coding: utf-8 -*-

import ckan.model as model
import json
import logging
import os
from six.moves.urllib.parse import urljoin
from base64 import b64encode, b64decode
from ckan.plugins.toolkit import config
from keycloak.realm import KeycloakRealm

log = logging.getLogger(__name__)

class SSOHelper(object):

    def __init__(self):
        self.authorization_endpoint = config.get('ckan.sso.authorization_endpoint') or None
        self.client_id = config.get('ckan.sso.client_id') or None
        self.client_secret = config.get('ckan.sso.client_secret') or None
        self.realm = config.get('ckan.sso.realm') or 'ckan'
        self.profile_username_field = config.get('ckan.sso.profile_username_field') or None
        self.profile_fullname_field = config.get('ckan.sso.profile_fullname_field') or None
        self.profile_email_field = config.get('ckan.sso.profile_email_field') or None
        self.profile_group_field = config.get('ckan.sso.profile_group_field') or None
        self.sysadmin_group_name = config.get('ckan.sso.sysadmin_group_name') or None
        self.profile_group_delim = config.get('ckan.sso.profile_group_delim') or None
        realm = KeycloakRealm(server_url=self.authorization_endpoint, realm_name=self.realm)
        self.oidc_client = realm.open_id_connect(client_id=self.client_id,client_secret=self.client_secret)

    def identify(self, token):
        log.info("SSO Identify")
        user_token = self.oidc_client.userinfo(token)
        # user_data = self.oidc_client.decode_token(user_token, '', options={ 'verify_signature': False })
        import jwt
        user_data = jwt.decode(token, '', verify=False, options={'verify_signature': False})
        try:
            email = user_data[self.profile_email_field]
        except:
            log.debug("Not Found: Email")
            email = None
        try:
            user_name = user_data[self.profile_username_field].lower()
            if "@idir" not in user_name:
                user_name += "@idir"
        except:
            log.debug("Not Found: User Name")
            return None

        user = model.User.get(user_name)
        if user is None:
            user = model.User(name=user_name)
        user.email = email
        user.sysadmin = False
        if self.profile_fullname_field and self.profile_fullname_field in user_data:
            user.fullname = user_data[self.profile_fullname_field]
        if self.profile_group_field and self.profile_group_field in user_data:
            if self.sysadmin_group_name and (self.sysadmin_group_name in user_data[
                self.profile_group_field] or self.profile_group_delim + self.sysadmin_group_name in user_data[
                                                 self.profile_group_field]):
                user.sysadmin = True

        log.info('Add user into CKAN database: %s'%user)
        model.Session.add(user)
        model.Session.commit()

        # Add users to top level orgs as members to facilitate IDIR secure
        # datasets in CKAN 2.9
        # Done with this custom query to improve performance
        groups_to_join = model.Session.execute('''
            SELECT g.id AS group_id
            FROM "group" AS g
            WHERE g.is_organization
                AND g.id NOT IN (
                    SELECT m.group_id 
                    FROM "member" AS m 
                    WHERE m.table_name = 'group'
                        OR (m.table_id = :userid
                            AND m.table_name = 'user'
                            AND m.state = 'active')
                );
        ''', {'userid': user.id})

        group_added = False
        for group in groups_to_join:
            log.info('Add user into group: %s'%group.group_id)
            org = model.Group.get(group.group_id)
            member = model.Member(table_name='user', table_id=user.id, capacity='member', group=org)
            model.Session.add(member)
            group_added = True

        if group_added:
            model.Session.commit()
        
        model.Session.remove()

        return user.name
