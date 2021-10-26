# KEYCLOAK MANAGEMENT FOR BC DATA CATALOGUE

|**AUDIENCE**|**ACCESS**|
|:---|:---|
| *Keycloak Administrators* |Ability to manage Keycloak Users, Groups, defined below, within Keycloak|
| *BCDC Administrators* | _TBD_|

## Table of Contents
+ [**RESOURCES**](#resources)
+ [**ROLE DEFINITIONS**](#role-definitions)
+ [**KEYCLOAK USERS**](#keycloak-users)
+ [**KEYCLOAK GROUPS**](#keycloak-groups)
+ [**KEYCLOAK ROLE MAPPING**](#keycloak-role-mapping)
+ [**KEYCLOAK FINE GRAIN**](#keycloak-fine-grain)

-----------------------

## RESOURCES
+	Keycloak User Management: https://www.keycloak.org/docs/9.0/server_admin/index.html#user-management
+	Keycloak Roles: https://www.keycloak.org/docs/9.0/server_admin/index.html#roles
+	Keycloak Groups: https://www.keycloak.org/docs/9.0/server_admin/index.html#groups
+ CKAN User Management: https://docs.ckan.org/en/ckan-2.7.3/maintaining/authorization.html

[RETURN TO TOP][1]

## ROLE DEFINITIONS

|Term|Definition|Role Impact|
|:---|:---|:---|
|Parent Org|Ministry or Highest level of Organization|Assigned User Role membership access to all Ministry's Branches/Divisions records (datasets)|
|Suborg|Branch/Division under Ministry or Organization|Assigned User Role membership access to all Suborg records (datasets)| 
|Group|Container of like records/datasets for quick viewing without searching|Assigned User Role membership access to associated group(s)| 



|User Role| Definition|Abilities|Implementation Status|
|:---:|:---|:---|:---:|
|Sysadmin| | | |
| | | | 
|Parent Org Admin|Parent granting will provide child or suborgs abilities|Ability to manage records and resources, and promote through the publishing and retirement process, at the Parent Org level.|Implemented|
|Parent Org Editor|Parent granting will provide child or suborgs abilities|Ability to manage records and resources, with limited promotion ability through the publishing and retirement process, at the Parent Org level.|Implemented|
|Parent Org Member|Parent granting will provide child or suborgs abilities|Ability to view (read only) Draft, Pending Publish and Archived datasets.  By nature of logging in, they will be able to see all Published and Pending Archive records at the Parent Org level.|Not Implemented|
| | | |
|Suborg Admin|Suborg granting will provide only suborg abilities|Ability to manage records and resources, and promote through the publishing and retirement process, at the Suborg level.|Implemented|
|Suborg Editor|Suborg granting will provide only suborg abilities|Ability to manage records and resources, with limited promotion ability through the publishing and retirement process, at the Suborg level.|Implemented|
|Suborg Member|Suborg granting will provide only suborg abilities|Ability to view (read only) Draft, Pending Publish and Archived datasets.  By nature of logging in, they will be able to see all Published and Pending Archive records regardless of Suborg.|Not Implemented|
| | | | 
|Group Admin| Full access role to manage data association, full group management, including membership to Group| Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s). Edit all Group properties (description, image and privacy checkbox) other than the Group Title and Name (URL)  _ENHANCEMENT_: Edit all Group properties (Group Title, Name (URL), Description, Image and Privacy checkbox), requires Keycloak Delegation Management  |  Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487.  Enhancement for Post-MVP. | 
|Group Editor| Partial access role to manage dataset association and partial Group administration | Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s).  _ENHANCEMENT_: Edit all Group properties (description, image and privacy checkbox) other than that the Group Title and Name (URL)  | Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487.  Enhancement for Post-MVP. |
|Group Member| Basic access role to manage dataset association to the group  | Ability to add/remove PUBLISHED and PENDING ARCHIVE Datasets to Group.  If an Editor or Admin of an Organization, include DRAFT and PENDING PUBLISH datasets for those Organization(s). | Currently requested for MVP, in PO Review - https://github.com/bcgov/ckan-ui/issues/487|

[RETURN TO TOP][1]

## KEYCLOAK USERS
+ Add
 
Adding users to Keycloak requires the following
    - Username*: lowercase <idir>@idir
    - Email
    - First Name
    - Last Name
+ Delete
    
Need to review at a later date the use of @ as it conflicts with ckan and thus it behaves like an invalid user.

 [RETURN TO TOP][1]
 
## KEYCLOAK GROUPS
+ Add
+ Rename
+ Delete
 
[RETURN TO TOP][1]

## KEYCLOAK ROLE MAPPING
+ User
+ Group
 
[RETURN TO TOP][1]

## KEYCLOAK FINE GRAIN
Fine grain has not be implimented thus the following is applied to mimic it

+ Group: admin-user-mgmt-bcdc
    + Role mapping: 
        - Client Roles: realm-management
            - manage-users 
+ Users: Only grant those who are to use Keycloak to manage users.

[RETURN TO TOP][1]

[1]: #keycloak-management-for-bc-data-catalogue
