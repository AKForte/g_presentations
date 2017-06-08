# Script to read account list from a csv file and create appropriate users in the portal.
# Admin persona.
print("RUNNING CREATE USERS")
print("--------------------")
import pandas as pd
from arcgis.gis import *

# Read CSV file
csv_path = r".\IWA_users_to_add.csv"

# Read as pandas dataframe
df = pd.read_csv(csv_path)
print(df[["Fullname", "email", "role"]].head(5))
print("=========================================================== \n")

# Connect to the GIS
gis = GIS("https://dev002783.esri.com:7443/arcgis", "admin", "esri.agp")

# loop through and create users
for index, row in df.iterrows():
    try:
        print("Creating user: ", row['Fullname'], end=" ## ")
        result = gis.users.create(username= row['username'],
                                  password = "",
                                  firstname= row['Firstname'],
                                  lastname= row['Lastname'],
                                  email= row['email'],
                                  role = row['role'],
                                  provider="enterprise",
                                  idpUsername=row['idpUsername'])
        if result:
            print("success  ##")
            # get group list
            print("\t Adding to groups: ", end=" # ")
            groups = row['groups']
            group_list = groups.split(",")

            # Search for the group
            for g in group_list:
                group_search = gis.groups.search(g)
                if len(group_search) > 0:
                    try:
                        group_obj = group_search[0]
                        groups_result = group_obj.add_users([row['username']])
                        if len(groups_result['notAdded']) == 0:
                            print(g, end =" # ")

                    except Exception as groups_ex:
                        print("\n \t Cannot add user to group ", g, str(groups_ex))
            print("\n")


    except Exception as add_ex:
        print("Cannot create user: " + row['username'])
        print(str(add_ex))