# KEYCLOAK GROUPS

|**AUDIENCE**|**DESCRIPTION**|
|:---|:---|
|DataBC Catalogue Sysadmins|TBD|
|DataBC Catalogue Admins|TBD|

## Table of Contents
+ [**NOTES TO ADMINISTER GROUPS AND USERS**](#notes-to-administer-groups-and-users)
   + [**ADD A GROUP**](#add-a-group)
   + [**RENAME A GROUP**](#rename-a-group)
   + [**DELETE A GROUP**](#delete-a-group)
+ [**KEYCLOAK USERS**](#keycloak-users)
   + [**ADD A USER**](#add-a-user)
   + [**DELETE A USER**](#delete-a-user)
+ [**KEYCLOAK USER GROUP MEMBERSHIP**](#keycloak-user-group-membership)
   + [**ADD A GROUP TO A USER**](#add-a-group-to-a-user)
   + [**REMOVE A GROUP FROM A USER**](#remove-a-group-from-a-user)
+ [**KEYCLOAK FINE GRAIN**](#keycloak-fine-grain)

## NOTES TO ADMINISTER GROUPS AND USERS
+ Keycloak Groups are tied to the Catalogue or CKAN Organizations and Groups.
+ In CKAN there are 3 roles or level of privileges: Admin, Editor and Member, these are each defined as their own Keycloak Group.
+ Always search that a group does not already exist.
+ Search is case sensitive.
+ Keycloak Group **must** match that of a CKAN Organization or Group as is displayed in the CKAN **Name** field format, e.g., ministry-of-citizens-sevices/databc-program.
    - if not using the API to retrieve this, the easiset way is to copy from the URL when clicking on the CKAN Organization or Group.
+ CKAN Organizations and Groups are stored in the same field and thus must be unique.


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
**Things to note**:
+ Renaming a Keycloak Group happens when a Ministry/Org, Branch/Suborg or CKAN Group has changed.
+ Requires the renaming of all 3 levels of privileges for that same CKAN Organization or Group.

1. Under **Manage**, Click **Groups**
1. Search for the Group (case sensitve and all entries are lowercase)
1. Double click on the **Group**
1. Update the Group Name
1. Repeat the above for the other associated Groups with the different privileges.

### DELETE A GROUP
**Things to note**:
+ Deleting a Keycloak Group should only happen when a CKAN Organization or Group needs to be deleted and not renamed.
+ Requires the deletion of all 3 levels of privileges.

1. Under **Manage**, Click **Groups**
1. Search for the Group (case sensitve and all entries are lowercase)
1. Click on the **Group**
1. Click the **Delete** button
1. Click **Delete** again on the popup to confirm you want to delete this group
1. Repeat the above for the other Groups with the same name and different privileges.

## KEYCLOAK USERS

**Things to note**: 
+ Search is case sensitive.
+ Users will be automatically be added when they log into Catalogue if they are not already added during the intial population from ADAM.
+ If a user has been added but never logged in, only their **Username** will be popuated. Once they log in then the other fields will be populated automatically.

**_Future Enhancements_**: Delegation to account management is to be done via a front end management tool that will call Keycloak API.
 
### ADD A USER
1. Under **Manage**, click on **Users**
1. Click the **Add user** button on the top right
1. Populate only
    - Username*: \<idir>\@idir
        - e.g., bobross@idir
1. The following will be autopopulated once they log in to the catalogue
    - Email:
    - First Name: 
    - Last Name: 
 
### DELETE A USER
1. Search for their IDIR or name
1. Click
    1. The **Delete** button to far right of their entry
    2. On their **ID** and then the trashcan symbol - PREFERENCE
1. Click **Delete** on the popup to confirm you want to delete this user
    - The User's ID is what is displayed in this popup, therefore be sure this is the user you want to delete first.
    - Hence recommend deleting a user via Option 2 above. 

## KEYCLOAK USER GROUP MEMBERSHIP

The following is how to grant users to be Admin, Editors or Members of a CKAN Organization or Group.

**Things to note**:
+ Groups are assigned to Users, as Users cannot be assigned to Groups via the UI.
+ Removing Groups from Users, the Group does not highlight, but does when adding Groups.

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
    - This group will no longer be listed in the **Group Membership** list

## KEYCLOAK FINE GRAIN
Fine grain has not be implimented thus the following is applied to mimic it:

+ Group: **admin-user-mgmt-bcdc**
    + Role mapping: 
        - Client Roles: realm-management
            - manage-users 
+ Users: Only grant those who are identified as Catalogue Administartive staff to use Keycloak to manage users.

[RETURN TO TOP][1]

[1]: #keycloak_groups
