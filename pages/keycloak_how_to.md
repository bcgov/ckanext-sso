## KEYCLOAK USERS
Accounts will be added to Keycloak when they first log into the catalogue.

Always search if a user exists first, if they were added and have never logged in, only their IDIR will be searchable. Once the log in, it will sync with LDAP and populate;
+ Email, Last name, First Name.

Search is case sensitive.

### ADD A USER
1. Under **Manage**, click on **Users**
1. Click the **Add user** button on the top right
1. Populate only
    - Username*: <idir>@idir
        - e.g., bobross@idir
1. The following will be autopopulated when they log in
    - Email:
    - First Name: 
    - Last Name: 
 
### DELETE A USER
1. Search for there IDIR or name
1. Click
    1. The **Delete** button to far right of their entry
    2. On their **ID** and then the trashcan symbol - PREFERENCE
1. Click **Delete** on the popup to confirm you want to delete this user
    - The User's ID is what is displayed in this popup, therefore be sure this is the user you want to delete first.
    - Hence recommend deleting a user via Option 2 above. 


## KEYCLOAK GROUPS
Keycloak Groups are tied Catalogue or CKAN Orgs and Groups.

In CKAN there are 3 levels of abilities, Admin, Editor and Member.

Each of these levels then corresponds to a Keycloak Group.

Always search that a group does not already exist. Search is case sensitive.

If a Keycloak Group **must** match that of a CKAN Org, Suborg or Group as is displayed in the Name format, e.g., ministry-of-citizens-sevices/databc-program

CKAN Sysadmin privileges are required to update a CKAN Org, Suborg or Group and thus only those with this privilege as well as KeyCloak Mange-Users privileges should do this.

### ADD A GROUP
1. Under **Manage**, click on **Groups** 
1. Click **New** 
1. The follow is the format is to be used with each section particioned with a /:

|Ministry/Org or Group Level|Suborg/ Branch Level|Privilege|Kecloak Group|
|:---:|:---:|:---:|:---|
|ministry-of-citizens-sevices| |admin|ministry-of-citizens-sevices/admin|
|ministry-of-citizens-sevices| |editor|ministry-of-citizens-sevices/editor|
|ministry-of-citizens-sevices| |member|ministry-of-citizens-sevices/member|
|ministry-of-citizens-sevices|databc-program|admin|ministry-of-citizens-sevices/databc-program/admin|
|ministry-of-citizens-sevices|databc-program|editor|ministry-of-citizens-sevices/databc-program/editor|
|ministry-of-citizens-sevices|databc-program|member|ministry-of-citizens-sevices/databc-program/member|
|group|data-innovation-program|admin|group/data-innovation-program/admin|
|group|data-innovation-program|editor|group/data-innovation-program/editor|
|group|data-innovation-program|member|group/data-innovation-program/member|


### RENAME A GROUP
Renaming a Keycloak Group happens when a Ministry/Org, Branch/Suborg or CKAN Group has changed.
* Requires the renaming of all 3 levels of privileges for that same organization or group.

CKAN Sysadmin privileges are required to update a CKAN Org, Suborg or Group and thus only those with this privilege as well as KeyCloak Mange-Users privileges should do this.

### DELETE A GROUP
CKAN Sysadmin privileges are required to update a CKAN Org, Suborg or Group and thus only those with this privilege as well as KeyCloak Mange-Users privileges should do this.

Deleting a Keycloak Group should
* Only happen when a CKAN Org or Group needs to be deleted and not renamed.
* Requires the deletion of all 3 levels of privileges.

## KEYCLOAK USER GROUP MEMBERSHIP
The following is how to grant users to be Admin, Editors or Members of a CKAN Organization or Group.

### ADD A GROUP TO A USER
1. Search and click  the **User**'s ID
1. Click the **Groups** tab
1. Search **Available Groups** for the CKAN Organization or Group name (this is case sensitive)
1. Click the applicable group
    - This becomes highlighted
1. Click **Join**
    - This group **_will_** now be added to the Group Membership list

### REMOVE A GROUP FROM A USER
1. Search and click  the **User**'s ID
1. Click the **Groups** tab
1. Click the applicable group under the **Group Membership** list
    - This **_will not_** become highlighted
1. Click **Leave**
    - This group will no longer be listed in the Group Membership list

## KEYCLOAK FINE GRAIN
Fine grain has not be implimented thus the following is applied to mimic it

+ Group: admin-user-mgmt-bcdc
    + Role mapping: 
        - Client Roles: realm-management
            - manage-users 
+ Users: Only grant those who are to use Keycloak to manage users.
