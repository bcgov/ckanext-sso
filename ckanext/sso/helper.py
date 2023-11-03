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
        log.info('profile group field: %s'%self.profile_group_field)
        log.info('sysadmin group name: %s'%self.sysadmin_group_name)
        log.info('Add user into ckan database: %s'%user_data[self.profile_group_field])
        model.Session.add(user)
        model.Session.commit()
        model.Session.remove()

        # Add users to top level orgs as members to facilitate IDIR secure
        # datasets in CKAN 2.9
        changedGroups = False
        top_level_orgs = model.Group.get_top_level_groups(type="organization")

        if self.profile_group_field and self.profile_group_delim and self.profile_group_field in user_data:
            membership = model.Session.query(model.Member).filter(model.Member.table_name == 'user').filter(model.Member.table_id == user.id).all()
            
            for top_group in top_level_orgs:
                if top_group.id not in [g.group_id for g in membership]:
                    # dbGroup = model.Session.query(model.Group).filter(model.Group.id == top_group.id).first()
                    member = model.Member(table_name='user', table_id=user.id, capacity='member', group=top_group)
                    log.info('Add user %s into group %s', user.name, top_group.name)
                    model.Session.add(member)
                    changedGroups = True
        
        if changedGroups:
            model.Session.commit()

                
        

        # changedGroups = False
        # if self.profile_group_field and self.profile_group_delim and self.profile_group_field in user_data:
        #     membership = model.Session.query(model.Member).filter(model.Member.table_name == 'user').filter(model.Member.table_id == user.id).all()
            
        #     for group in user_data[self.profile_group_field]:

        #         group = group.lstrip(self.profile_group_delim)
                
        #         group = group.split(self.profile_group_delim)

        #         if len(group) >= 2:
        #             group_name = "".join(group[len(group)-2].strip())
        #             capacity = group[len(group)-1].lower()

        #             dbGroup = model.Session.query(model.Group).filter(model.Group.name == group_name).first()
        #             if not dbGroup is None:
                        
        #                 capacity = capacity.lower()

        #                 if capacity in ["admin", "editor", "member"]:
        #                     memberDb = None
        #                     for memberOf in membership:
        #                         if memberOf.group_id == dbGroup.id and memberOf.capacity == capacity and memberOf.state == 'active':
        #                             memberDb = memberOf
        #                             break

        #                     if not memberDb is None:
        #                         membership.remove(memberDb)

        #                     if memberDb is None:
        #                         member = model.Member(table_name='user', table_id=user.id, capacity=capacity, group=dbGroup)
        #                         log.info('Add user %s into group %s', user.name, dbGroup.name)
        #                         rev = model.repo.new_revision()
        #                         rev.author = user.id
        #                         model.Session.add(member)
        #                         changedGroups = True

        #     for memberRec in membership:
        #         changedGroups = True
        #         log.info('Removing user %s from group %s', user.name, memberRec.group_id)
        #         model.Session.delete(memberRec)


        #     if changedGroups:
        #         model.Session.commit()
        #         model.Session.remove()

        return user.name
