# 10.5 Show and Tell presentation for Scripting and Automation topic
Summary of the story is, an admin user executes a batch script every time
she/he creates a portal. This script will create a list of groups, users
and add the users to appropriate groups.

Then the list of users information is handed off to the team's publisher.
This person publishes a bunch of content and transfers ownership to each
of the user.

All this happens over night before any of the users can login. Once they
login, their content magically appears in their accounts. This process
can be repeated over and over.

## Real life application
Hurricane Matthew is devastating Haiti and pummelling the east coast right now (Oct 2016).
The FEMA crew stationed in Charlotte, NC has to be dispatched immediately to assess
damage and help with the rescue missions. Let us imagine Esri employees in `portaldev@esri.com`
alias are our rescue fighters. The GIS administrator was slacked overnight asking
to set up a portal immediately and populate it with appropriate user accounts, groups
and content for each users. When the following day dawns, users are log in to the portal
using their enterprise accounts on a field app such as **Collector for ArcGIS** or **Navigator for ArcGIS** 
and should have a map representing the places they need to attend to. Time is of
essence during such emergencies and the fighters are not to be required to use
a browser to sign in or to set up their work area.

How long will this task take? If the administrator did it by hand,
it depends on the number of rescue fighters. But since the admin uses **Chef for ArcGIS** 
to create a new **ArcGIS Enterprise** and **ArcGIS Python API** to 
perform the administrative tasks, she accomplishes it in a matter of minutes. 

## Files:
  - [create_IWA_groups.py](create_IWA_groups.py) will create groups and uses
    - [groups.csv]('.\groups.csv') for data
  
  - [create_IWA_users50.py](create_IWA_users50.py) will create 50 builtin users
    - [IWA_users_to_add.csv](IWA_users_to_add.csv) is the data for it.
  
  - [create_IWA_user_items.py](create_IWA_user_items.py) will publish and transfer ownership to each user
    - [user_content_new](https://devtopia.esri.com/atma6951/geosaurus_scripts/tree/master/presentations/show_n_tell_105/user_content_new) contains the data for each user
    
  - [cleanup.py]('.\cleanup.py') run this before every time this is rerun. it removes
  all old content, deletes groups and users.
  
# Running
## Administrator
The administrator runs the batch file titled [admin_persona_IWA.bat](admin_persona_IWA.bat). 
This results in a output as shown below:

```
$ admin_persona_IWA.bat

echo "Portal administration scripts"
"Portal administration scripts"

REM python cleanup.py

python create_IWA_groups.py
RUNNING CREATE GROUPS
---------------------
                                               title   access sortField
0                                           Basemaps   public     title
1                                   Central Services      org     title
2                                         Compliance  private  modified
3  Customer Service, Finance, Billing and Accounting      org     title
4                                Demographic Content  private     title
======================================================================

 Creating group:  Basemaps  ##  success
 Creating group:  Central Services  ##  success
 Creating group:  Compliance  ##  success
 Creating group:  Customer Service, Finance, Billing and Accounting  ##  success
 Creating group:  Demographic Content  ##  success

python create_IWA_users50.py
RUNNING CREATE USERS
--------------------
          Fullname              email       role
0     Aniket Patil    apatil@esri.com  org_admin
1     Anne Reuland  areuland@esri.com  org_admin
2  Ashwini Ramesha  ARamesha@esri.com  org_admin
3        Atma Mani     AMani@esri.com  org_admin
4     Aysar Khalid   AKhalid@esri.com  org_admin
===========================================================

Creating user:  Aniket Patil ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Anne Reuland ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Ashwini Ramesha ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Atma Mani ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Aysar Khalid ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Bill Major ## success  ##
         Adding to groups:  # Basemaps #  Central Services #

Creating user:  Blake Stearman ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Caroline Wright ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Catherine Hynes ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Cherry Lin ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Chris Whitmore ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Dan OLeary ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  David Cordes ## success  ##
         Adding to groups:  # Basemaps #  Compliance #  Central Services #

Creating user:  Derek Weatherbe ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Eric Miller ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Eva Mui ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Fumi Klemski ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Garima Tiwari ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Gary Sheppard ## success  ##
         Adding to groups:  # Basemaps #  Compliance #

Creating user:  Gayathri Alallasundaram ## success  ##
         Adding to groups:  # Basemaps #  Customer Service #

Creating user:  Javier Gutierrez ## success  ##
         Adding to groups:  # Basemaps #  Customer Service #

Creating user:  Jay Theodore ## success  ##
         Adding to groups:  # Basemaps #  Customer Service #

Creating user:  Jeff Smith ## success  ##
         Adding to groups:  # Basemaps #  Customer Service #

Creating user:  Jianbo Li ## success  ##
         Adding to groups:  # Basemaps #  Customer Service #  Central Services #

Creating user:  Jose Thomas ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Julia Yunzhu Shi ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Julio Andrade ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Kanika Kumar ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Kim Peter ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Laurence Clinton ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Manoj Kulkarni ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Marley Geddes ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Moginraj Mohandas ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Monoj Kumar Raja ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Compliance #

Creating user:  Nalika Amarasinghe ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Nathan Diep ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Niccole Murphy ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Norbert Piega ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Pathik Thakkar ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Peixuan Jiang ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Peter DSouza ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Philip Heede ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Central Services #

Creating user:  Rajkumar Padmanabhan ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Customer Service #

Creating user:  Ravi Narayanan ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Customer Service #

Creating user:  Rohit Singh ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Customer Service #

Creating user:  Sara Sanchez ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Customer Service #

Creating user:  Satish Malipeddi ## success  ##
         Adding to groups:  # Basemaps #  Demographic Content #  Customer Service #

Creating user:  Shreyas Shinde ## success  ##
         Adding to groups:  # Cannot create user: shre5185@AVWORLD
```

## Publisher
Once users and groups are created, the publisher takes over and runs the batch
file titled [publisher_persona_IWA.bat](publisher_persona_IWA.bat). This results
in items being published for each user. The output is shown below:
````
$ publisher_persona_IWA.bat

echo "Portal administration scripts"
"Portal administration scripts"

python create_IWA_user_items.py
========================================

             username assigned_state
0    anik7857@AVWORLD             KS
1     reuland@AVWORLD             NV
2    ashw8450@AVWORLD             IN
3    atma6951@AVWORLD             NC
4    aysa8100@AVWORLD             AR
5    robe5155@AVWORLD             FL
6    blak3408@AVWORLD             NH
7    caro3510@AVWORLD             ID
8    cath7852@AVWORLD             AZ
9    cher3495@AVWORLD             LA
10   chri4732@AVWORLD             NY
11    dan4937@AVWORLD             MS
12   davi3690@AVWORLD             WI
13   dere2810@AVWORLD             WA
14   eric4490@AVWORLD             MI
15    eva4456@AVWORLD             VA
16       fumi@AVWORLD             TX
17   gari0000@AVWORLD             MA
18   gary4620@AVWORLD             AL
19   gaya6337@AVWORLD             IL
20   javi5947@AVWORLD             NJ
21       jayt@AVWORLD             DE
22   jeff6111@AVWORLD             PA
23   jian4992@AVWORLD             CT
24   jona6782@AVWORLD             FM
25    jthomas@AVWORLD             MT
26   juli5163@AVWORLD             OH
27      julio@AVWORLD             IA
28  cont_kani@AVWORLD             KY
29    kim4476@AVWORLD             GA
30   laur5745@AVWORLD             WV
31      manoj@AVWORLD             MD
32   marl8798@AVWORLD             VT
33   mogi7192@AVWORLD             AK
34   mono6373@AVWORLD             ME
35   nali8821@AVWORLD             SC
36   nath8842@AVWORLD             WY
37   nicc7851@AVWORLD             UT
38   norb7760@AVWORLD             NE
39   path4507@AVWORLD             PR
40   peix8580@AVWORLD             SD
41   pete3937@AVWORLD             CA
42   phil5223@AVWORLD             NM
43   rajk3142@AVWORLD             TN
44   ravi3531@AVWORLD             MO
45   rohi3999@AVWORLD             ND
46   sara5787@AVWORLD             OR
47     satish@AVWORLD             MN
48   serg0000@AVWORLD             CO
49   shre5185@AVWORLD            NaN
========================================

Publishing  .\user_content_new\KS.csv  ##  success. Assigning to:   #  anik7857@AVWORLD
Publishing  .\user_content_new\NV.csv  ##  success. Assigning to:   #  reuland@AVWORLD
Publishing  .\user_content_new\IN.csv  ##  success. Assigning to:   #  ashw8450@AVWORLD
Publishing  .\user_content_new\NC.csv  ##  success. Assigning to:   #  atma6951@AVWORLD
Publishing  .\user_content_new\AR.csv  ##  success. Assigning to:   #  aysa8100@AVWORLD
Publishing  .\user_content_new\FL.csv  ##  success. Assigning to:   #  robe5155@AVWORLD
Publishing  .\user_content_new\NH.csv  ##  success. Assigning to:   #  blak3408@AVWORLD
Publishing  .\user_content_new\ID.csv  ##  success. Assigning to:   #  caro3510@AVWORLD
Publishing  .\user_content_new\AZ.csv  ##  success. Assigning to:   #  cath7852@AVWORLD
Publishing  .\user_content_new\LA.csv  ##  success. Assigning to:   #  cher3495@AVWORLD
Publishing  .\user_content_new\NY.csv  ##  success. Assigning to:   #  chri4732@AVWORLD
Publishing  .\user_content_new\MS.csv  ##  success. Assigning to:   #  dan4937@AVWORLD
Publishing  .\user_content_new\WI.csv  ##  success. Assigning to:   #  davi3690@AVWORLD
Publishing  .\user_content_new\WA.csv  ##  success. Assigning to:   #  dere2810@AVWORLD
Publishing  .\user_content_new\MI.csv  ##  success. Assigning to:   #  eric4490@AVWORLD
Publishing  .\user_content_new\VA.csv  ##  success. Assigning to:   #  eva4456@AVWORLD
Publishing  .\user_content_new\TX.csv  ##  success. Assigning to:   #  fumi@AVWORLD
Publishing  .\user_content_new\MA.csv  ##  success. Assigning to:   #  gari0000@AVWORLD
Publishing  .\user_content_new\AL.csv  ##  success. Assigning to:   #  gary4620@AVWORLD
Publishing  .\user_content_new\IL.csv  ##  success. Assigning to:   #  gaya6337@AVWORLD
Publishing  .\user_content_new\NJ.csv  ##  success. Assigning to:   #  javi5947@AVWORLD
Publishing  .\user_content_new\DE.csv  ##  success. Assigning to:   #  jayt@AVWORLD
Publishing  .\user_content_new\PA.csv  ##  success. Assigning to:   #  jeff6111@AVWORLD
Publishing  .\user_content_new\CT.csv  ##  success. Assigning to:   #  jian4992@AVWORLD
Publishing  .\user_content_new\FM.csv  ##  Error :  File(.\user_content_new\FM.csv) not found.
Publishing  .\user_content_new\MT.csv  ##  success. Assigning to:   #  jthomas@AVWORLD
Publishing  .\user_content_new\OH.csv  ##  success. Assigning to:   #  juli5163@AVWORLD
Publishing  .\user_content_new\IA.csv  ##  success. Assigning to:   #  julio@AVWORLD
Publishing  .\user_content_new\KY.csv  ##  success. Assigning to:   #  cont_kani@AVWORLD
Publishing  .\user_content_new\GA.csv  ##  success. Assigning to:   #  kim4476@AVWORLD
Publishing  .\user_content_new\WV.csv  ##  success. Assigning to:   #  laur5745@AVWORLD
Publishing  .\user_content_new\MD.csv  ##  success. Assigning to:   #  manoj@AVWORLD
Publishing  .\user_content_new\VT.csv  ##  success. Assigning to:   #  marl8798@AVWORLD
Publishing  .\user_content_new\AK.csv  ##  success. Assigning to:   #  mogi7192@AVWORLD
Publishing  .\user_content_new\ME.csv  ##  success. Assigning to:   #  mono6373@AVWORLD
Publishing  .\user_content_new\SC.csv  ##  success. Assigning to:   #  nali8821@AVWORLD
Publishing  .\user_content_new\WY.csv  ##  success. Assigning to:   #  nath8842@AVWORLD
Publishing  .\user_content_new\UT.csv  ##  success. Assigning to:   #  nicc7851@AVWORLD
Publishing  .\user_content_new\NE.csv  ##  success. Assigning to:   #  norb7760@AVWORLD
Publishing  .\user_content_new\PR.csv  ##  success. Assigning to:   #  path4507@AVWORLD
Publishing  .\user_content_new\SD.csv  ##  success. Assigning to:   #  peix8580@AVWORLD
Publishing  .\user_content_new\CA.csv  ##  success. Assigning to:   #  pete3937@AVWORLD
Publishing  .\user_content_new\NM.csv  ##  success. Assigning to:   #  phil5223@AVWORLD
Publishing  .\user_content_new\TN.csv  ##  success. Assigning to:   #  rajk3142@AVWORLD
Publishing  .\user_content_new\MO.csv  ##  success. Assigning to:   #  ravi3531@AVWORLD
Publishing  .\user_content_new\ND.csv  ##  success. Assigning to:   #  rohi3999@AVWORLD
Publishing  .\user_content_new\OR.csv  ##  success. Assigning to:   #  sara5787@AVWORLD
```
## Field crew
On the following day, the crew opens the **Navigator for ArcGIS** app on their mobile device,
connect to the portal url and their content loads up.

![Navigator home page](https://devtopia.esri.com/atma6951/geosaurus_scripts/blob/master/presentations/show_n_tell_105/Navigator_1.png)

Each rescue fighter can then visualize the POI they need to visit:
![web map on navigator](https://devtopia.esri.com/atma6951/geosaurus_scripts/blob/master/presentations/show_n_tell_105/Navigator_2.png)

When the rescue fighters login to their portal, their my content page contains the following items:
![my contents](https://devtopia.esri.com/atma6951/geosaurus_scripts/blob/master/presentations/show_n_tell_105/portal_my_contents.PNG)

## Clean up the portal
The portal can be reverted back to its original state by running the
[clean_up.bat](clean_up.bat) file. This retuns the following output

```
$ clean_up.bat

echo "Cleaning up portal"
"Cleaning up portal"

python cleanup.py
RUNNING CLEANUP
---------------

Deleting groups
---------------
Deleting  Basemaps  ##  success
Deleting  Central Services  ##  success
Deleting  Compliance  ##  success
Deleting  Customer Service, Finance, Billing and Accounting  ##  success
Deleting  Demographic Content  ##  success

Deleting user content
---------------------
User :  Administrator # skipped
User :  Aniket Patil # Deleting :  KS # True | Deleting :  KS # True | empty
User :  Ashwini Ramesha # Deleting :  IN # True | Deleting :  IN # True | empty
User :  Atma Mani # Deleting :  NC # True | Deleting :  NC # True | empty
User :  Atma Mani # empty
User :  Aysar Khalid # Deleting :  AR # True | Deleting :  AR # True | empty
User :  Blake Stearman # Deleting :  NH # True | Deleting :  NH # True | empty
User :  Caroline Wright # Deleting :  ID # True | Deleting :  ID # True | empty
User :  Catherine Hynes # Deleting :  AZ # True | Deleting :  AZ # True | empty
User :  Cherry Lin # Deleting :  LA # True | Deleting :  LA # True | empty
User :  Chris Whitmore # Deleting :  NY # True | Deleting :  NY # True | empty
User :  Kanika Kumar # Deleting :  KY # True | Deleting :  KY # True | empty
User :  Dan OLeary # Deleting :  MS # True | Deleting :  MS # True | empty
User :  David Cordes # Deleting :  WI # True | Deleting :  WI # True | empty
User :  Derek Weatherbe # Deleting :  WA # True | Deleting :  WA # True | empty
User :  Eric Miller # Deleting :  MI # True | Deleting :  MI # True | empty
User :  Esri # skipped
User :  Esri # skipped
User :  Esri # skipped
User :  Esri Navigation # skipped
User :  Eva Mui # Deleting :  VA # True | Deleting :  VA # True | empty
User :  Fumi Klemski # Deleting :  TX # True | Deleting :  TX # True | empty
User :  Garima Tiwari # Deleting :  MA # True | Deleting :  MA # True | empty
User :  Gary Sheppard # Deleting :  AL # True | Deleting :  AL # True | empty
User :  Gayathri Alallasundaram # Deleting :  IL # True | Deleting :  IL # True | empty
User :  Javier Gutierrez # Deleting :  NJ # True | Deleting :  NJ # True | empty
User :  Jay Theodore # Deleting :  DE # True | Deleting :  DE # True | empty
User :  Jeff Smith # Deleting :  PA # True | Deleting :  PA # True | empty
User :  Jianbo Li # Deleting :  CT # True | Deleting :  CT # True | empty
User :  Jonathan Quinn # empty
User :  Jose Thomas # Deleting :  MT # True | Deleting :  MT # True | empty
User :  Julia Yunzhu # Deleting :  OH # True | Deleting :  OH # True | empty
User :  Julio Andrade # Deleting :  IA # True | Deleting :  IA # True | empty
User :  Kim Peter # Deleting :  GA # True | Deleting :  GA # True | empty
User :  Laurence Clinton # Deleting :  WV # True | Deleting :  WV # True | empty
User :  Manoj Kulkarni # Deleting :  MD # True | Deleting :  MD # True | empty
User :  Marley Geddes # Deleting :  VT # True | Deleting :  VT # True | empty
User :  Moginraj Mohandas # Deleting :  AK # True | Deleting :  AK # True | empty
User :  Monoj Kumar # Deleting :  ME # True | Deleting :  ME # True | empty
User :  Nalika Amarasinghe # Deleting :  SC # True | Deleting :  SC # True | empty
User :  Nathan Diep # Deleting :  WY # True | Deleting :  WY # True | empty
User :  Niccole Murphy # Deleting :  UT # True | Deleting :  UT # True | empty
User :  Norbert Piega # Deleting :  NE # True | Deleting :  NE # True | empty
User :  Pathik Thakkar # Deleting :  PR # True | Deleting :  PR # True | empty
User :  Peixuan Jiang # Deleting :  SD # True | Deleting :  SD # True | empty
User :  Peter DSouza # Deleting :  CA # True | Deleting :  CA # True | empty
User :  Philip Heede # Deleting :  NM # True | Deleting :  NM # True | empty
User :  Rajkumar Padmanabhan # Deleting :  TN # True | Deleting :  TN # True | empty
User :  Ravi Narayanan # Deleting :  MO # True | Deleting :  MO # True | empty
User :  Anne Reuland # Deleting :  NV # True | Deleting :  NV # True | empty
User :  Bill Major # Deleting :  FL # True | Deleting :  FL # True | empty
User :  Rohit Singh # Deleting :  ND # True | Deleting :  ND # True | empty
User :  Sara Sanchez # Deleting :  OR # True | Deleting :  OR # True | empty
User :  Suganya Baskaran # empty

Deleting users
--------------
Deleting  anik7857@AVWORLD  ##  success
Deleting  ashw8450@AVWORLD  ##  success
Deleting  atma6951@AVWORLD  ##  success
Deleting  aysa8100@AVWORLD  ##  success
Deleting  blak3408@AVWORLD  ##  success
Deleting  caro3510@AVWORLD  ##  success
Deleting  cath7852@AVWORLD  ##  success
Deleting  cher3495@AVWORLD  ##  success
Deleting  chri4732@AVWORLD  ##  success
Deleting  cont_kani@AVWORLD  ##  success
Deleting  dan4937@AVWORLD  ##  success
Deleting  davi3690@AVWORLD  ##  success
Deleting  dere2810@AVWORLD  ##  success
Deleting  eric4490@AVWORLD  ##  success
Deleting  eva4456@AVWORLD  ##  success
Deleting  fumi@AVWORLD  ##  success
Deleting  gari0000@AVWORLD  ##  success
Deleting  gary4620@AVWORLD  ##  success
Deleting  gaya6337@AVWORLD  ##  success
Deleting  javi5947@AVWORLD  ##  success
Deleting  jayt@AVWORLD  ##  success
Deleting  jeff6111@AVWORLD  ##  success
Deleting  jian4992@AVWORLD  ##  success
Deleting  jona6782@AVWORLD  ##  success
Deleting  jthomas@AVWORLD  ##  success
Deleting  juli5163@AVWORLD  ##  success
Deleting  julio@AVWORLD  ##  success
Deleting  kim4476@AVWORLD  ##  success
Deleting  laur5745@AVWORLD  ##  success
Deleting  manoj@AVWORLD  ##  success
Deleting  marl8798@AVWORLD  ##  success
Deleting  mogi7192@AVWORLD  ##  success
Deleting  mono6373@AVWORLD  ##  success
Deleting  nali8821@AVWORLD  ##  success
Deleting  nath8842@AVWORLD  ##  success
Deleting  nicc7851@AVWORLD  ##  success
Deleting  norb7760@AVWORLD  ##  success
Deleting  path4507@AVWORLD  ##  success
Deleting  peix8580@AVWORLD  ##  success
Deleting  pete3937@AVWORLD  ##  success
Deleting  phil5223@AVWORLD  ##  success
Deleting  rajk3142@AVWORLD  ##  success
Deleting  ravi3531@AVWORLD  ##  success
Deleting  reuland@AVWORLD  ##  success
Deleting  robe5155@AVWORLD  ##  success
Deleting  rohi3999@AVWORLD  ##  success
Deleting  sara5787@AVWORLD  ##  success
Deleting  suga7159@AVWORLD  ##  success
Deleting  system_publisher  ##  success

 All clean
```
