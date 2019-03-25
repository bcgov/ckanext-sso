# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import helper

from ckan import plugins
from ckan.plugins import toolkit
from pylons import config
from urlparse import urlparse

import ckan.model as model
from ckan.lib.helpers import redirect_to as redirect

log = logging.getLogger(__name__)

class SSOPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthenticator, inherit=True)
    plugins.implements(plugins.IConfigurer)

    def __init__(self, name=None):
        self.sso_helper = helper.SSOHelper()

    def update_config(self,config):
        return None

    def configure(self, config):
        required_keys = (
            'ckan.sso.authorization_endpoint',
            'ckan.sso.client_id',
            'ckan.sso.client_secret',
            'ckan.sso.realm',
            'ckan.sso.profile_username_field',
            'ckan.sso.profile_fullname_field',
            'ckan.sso.profile_email_field',
            'ckan.sso.profile_group_field',
            'ckan.sso.sysadmin_group_name'
        )
        for key in required_keys:
            if config.get(key) is None:
                raise RuntimeError('Required configuration option {0} not found.'.format(key))

    def identify(self):
        if not getattr(toolkit.c, u'user', None):
            self._identify_user_default()
        if toolkit.c.user and not getattr(toolkit.c, u'userobj', None):
            toolkit.c.userobj = model.User.by_name(toolkit.c.user)

    def _identify_user_default(self):
        toolkit.c.user = toolkit.request.environ.get(u'REMOTE_USER', u'')
        if toolkit.c.user:
            toolkit.c.user = toolkit.c.user.decode(u'utf8')
            toolkit.c.userobj = model.User.by_name(toolkit.c.user)
            if toolkit.c.userobj is None or not toolkit.c.userobj.is_active():
                ev = request.environ
                if u'repoze.who.plugins' in ev:
                    pth = getattr(ev[u'repoze.who.plugins'][u'friendlyform'],
                          u'logout_handler_path')
                redirect(pth)
        else:
            toolkit.c.userobj = self._get_user_info()
            if 'name' in dir(toolkit.c.userobj) :
                toolkit.c.user = toolkit.c.userobj.name
                toolkit.c.author = toolkit.c.userobj.name
                log.debug('toolkit.c.userobj.id :' + toolkit.c.userobj.id)
                log.debug('toolkit.c.userobj.name :' + toolkit.c.userobj.name)

    def _get_user_info(self):
        authorizationKey = toolkit.request.headers.get(u'Authorization', u'')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get(u'Authorization', u'')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get(u'HTTP_AUTHORIZATION', u'')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get(u'Authorization', u'')
            if u' ' in authorizationKey:
                authorizationKey = u''
        if not authorizationKey:
            return None

        authorizationKey = authorizationKey.decode(u'utf8', u'ignore')
        if authorizationKey.startswith("Bearer "):
            authorizationKey = authorizationKey[len("Bearer ")::]
            
        user = None
        query = model.Session.query(model.User)
        user = query.filter_by(apikey=authorizationKey).first()
        if user == None :
            try:
                user = self.sso_helper.identify(authorizationKey)
                user = query.filter_by(name=user).first()
            except Exception as e:
                log.error( e.message)
        return user
