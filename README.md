# ckanext-sso
OpenID connect plugin for CKAN used by the B.C. Catalogue.

## Requirements
- Ckan 2.7

## Notes
- Currently only supports keycloak
- This extension provides the ability for users to use access-tokens from Keycloak server to access CKAN functions via CKAN REST API. Via the `Authorization: Bearer` token format
- A new user will be created automatically in ckan database for corresponding keycloak user if it does not exist
- Original ckan auth still works normally with this extension, it only provides additional login means for rest access

## Installation
To install
1) activate your virtual environment ie `source venv/bin/activate`
2) Install the requirements `pip install -r requirements.txt`
3) Install the package `python setup.py install`
4) Add `sso` settings in CKAN config file
```
ckan.plugins = sso {OTHER PLUGINS}
ckan.sso.authorization_endpoint = http://localhost/auth
ckan.sso.realm = master
ckan.sso.client_id = client_id
ckan.sso.client_secret = client_secret
ckan.sso.sysadmin_group_name = admin
ckan.sso.profile_group_field = groups
ckan.sso.profile_username_field = preferred_username
ckan.sso.profile_email_field = email
ckan.sso.profile_fullname_field = name
```
5) Restart CKAN if it was already running