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

|Term|Definition|Role Impact|
|:---|:---|:---|
|Parent Org|Ministry or Highest level of Organization|Assigned user role membership access to all Ministry's Branches/Divisions records (datasets)|
|Suborg|Branch/Division under Ministry or Organizaiton|Assigned user role membership access to all Suborg records (datasets)| 
|Group|Container of like records/datasets for quick viewing without searching|Assigned user role membership access to associated group(s)| 

|User Role| Definition|Abilities|Implemented|
|:---:|:---|:---|:---|
|Sysadmin| | | |
| | | | 
|Parent Org Admin|Parent granting will provide child or suborgs abilities| |
|Parent Org Editor|Parent granting will provide child or suborgs abilities | |Not at this time|
|Parent Org Member|Parent granting will provide child or suborgs abilities | |Not at this time|
| | | |
|Suborg Admin| | | |
|Suborg Editor| | | |
|Suborg Member|Basic access role to view suborg's dataset(s) in any state - read only | Ability to view (read only) Draft, Pending Publish and Archived datasets.  By nature of logging in, they will be able to see all Published and Pending Archive records regardless of Suborg|Not at this time|
| | | | 
|Group Admin| Full access role to manage data association, full group management, including membership to Group| Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s). Edit all Group properties (description, image and privacy checkbox) other than the Group Title and Name (URL)  _ENHANCEMENT_: Edit all Group properties (Group Title, Name (URL), Description, Image and Privacy checkbox), requires Keycloak Delegation Management  |  Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487.  Enhancement for Post-MVP. | 
|Group Editor| Partial access role to manage dataset association and partial Group administration | Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s).  _ENHANCEMENT_: Edit all Group properties (description, image and privacy checkbox) other than that the Group Title and Name (URL)  | Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487.  Enhancement for Post-MVP. |
|Group Member| Basic access role to manage dataset association to the group  | Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s). | Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487|


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
