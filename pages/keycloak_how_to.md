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
