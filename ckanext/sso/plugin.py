# -*- coding: utf-8 -*-

import logging
from . import helper

from ckan import plugins
from ckan.plugins import toolkit
from ckan.plugins.toolkit import config
from urllib.parse import urlparse

import ckan.model as model
from ckan.lib.helpers import redirect_to as redirect

log = logging.getLogger(__name__)


class SSOPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IAuthenticator, inherit=True)
    plugins.implements(plugins.IConfigurer)

    def __init__(self, name=None):
        self.sso_helper = helper.SSOHelper()

    def update_config(self, config):
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
            'ckan.sso.sysadmin_group_name',
            'ckan.sso.profile_group_delim'
        )
        for key in required_keys:
            if config.get(key) is None:
                raise RuntimeError('Required configuration option {0} not found.'.format(key))

    def identify(self):
        if not getattr(toolkit.c, 'user', None):
            self._identify_user_default()
        if toolkit.c.user and not getattr(toolkit.c, 'userobj', None):
            toolkit.c.userobj = model.User.by_name(toolkit.c.user)

    def _identify_user_default(self):
        toolkit.c.user = toolkit.request.environ.get('REMOTE_USER', '')
        if toolkit.c.user:
            toolkit.c.user = toolkit.c.user.decode('utf8')
            toolkit.c.userobj = model.User.by_name(toolkit.c.user)
            if toolkit.c.userobj is None or not toolkit.c.userobj.is_active():
                ev = toolkit.request.environ
                if 'repoze.who.plugins' in ev:
                    pth = getattr(ev['repoze.who.plugins']['friendlyform'],
                          'logout_handler_path')
                redirect(pth)
        else:
            toolkit.c.userobj = self._get_user_info()
            if 'name' in dir(toolkit.c.userobj):
                toolkit.c.user = toolkit.c.userobj.name
                toolkit.c.author = toolkit.c.userobj.name
                log.debug('toolkit.c.userobj.id :' + toolkit.c.userobj.id)
                log.debug('toolkit.c.userobj.name :' + toolkit.c.userobj.name)

    def _get_user_info(self):
        authorizationKey = toolkit.request.headers.get('Authorization', '')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get('Authorization', '')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get('HTTP_AUTHORIZATION', '')
        if not authorizationKey:
            authorizationKey = toolkit.request.environ.get('Authorization', '')
            if ' ' in authorizationKey:
                authorizationKey = ''
        if not authorizationKey:
            return None

        authorizationKey = authorizationKey.decode('utf8', 'ignore')
        if authorizationKey.startswith("Bearer "):
            authorizationKey = authorizationKey[len("Bearer ")::]
            
        user = None
        query = model.Session.query(model.User)
        user = query.filter_by(apikey=authorizationKey).first()
        if user is None:
            try:
                user = self.sso_helper.identify(authorizationKey)
                user = query.filter_by(name=user).first()
            except Exception as e:
                error_message = str(e)
                log.error(error_message)
        return user
