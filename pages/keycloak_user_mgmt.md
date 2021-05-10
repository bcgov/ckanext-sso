# KEYCLOAK MANAGEMENT FOR BC DATA CATALOGUE

|**AUDIENCE**|
|:---:|
| *Keycloak Administrators* | 
| *BCDC Administrators* |

## Table of Contents
+ [**ROLE DEFINITIONS**](#role-definitions)
+ 

-----------------------

## RESOURCES
+	Keycloak User Management: https://www.keycloak.org/docs/9.0/server_admin/index.html#user-management
+	Keycloak Roles: https://www.keycloak.org/docs/9.0/server_admin/index.html#roles
+	Keycloak Groups: https://www.keycloak.org/docs/9.0/server_admin/index.html#groups
+ CKAN User Management: https://docs.ckan.org/en/ckan-2.7.3/maintaining/authorization.html

## ROLE DEFINITIONS

|User Role| Definition|Abilities|Implimented|
|:---:|:---:|:---:|:---:|
|Sysadmin| | | |
|Parent Org Admin|Parent granting will provide child or suborgs abilities| |
| | | |
|Parent Org Editor|Parent granting will provide child or suborgs abilities | |Not at this time|
|Parent Org Member|Parent granting will provide child or suborgs abilities | |Not at this time|
|Suborg Admin| | | |
|Suborg Editor| | | |
|Suborg Member| | |Not at this time |
|Group Admin| | | | 
|Group Editor| | | |
|Group Member| | |Not at this time |


## KEYCLOAK USERS
+ Add

Adding users to Keycloak requires the following
    - Username*: lowercase <idir>@idir
    - Email
    - First Name
    - Last Name
+ Delete

## KEYCLOAK GROUPS
+ Add
+ Rename
+ Delete

## KEYCLOAK ROLE MAPPING
+ User
+ Group

## KEYCLOAK FINE GRAIN
Fine grain has not be implimented thus the following is applied to mimic it

+ Group: admin-user-mgmt-bcdc
    + Role mapping: 
        - Client Roles: realm-management
            - manage-users 
+ Users: Only grant those who are to use Keycloak to manage users.

[RETURN TO TOP][1]

[1]: #keycloak-management-for-bc-data-catalogue
