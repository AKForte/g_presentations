# Publisher persona
# Script to publish content for each user.

from arcgis.gis import *
import pandas as pd

# Read the csv containing user accounts and their territory info
print("======================================== \n")
df = pd.read_csv('.\\builtin_users_to_add.csv')
print(df[['username', 'assigned_state']])
print("======================================== \n")

# Connect to the GIS
gis = GIS("https://dev002346.esri.com/portal", "Admin", "esri.agp")

# Loop through each user and publish the content
for index, row in df.iterrows():
    try:
        data_to_publish = '.\\user_content\\' + row['assigned_state'] + ".csv"

        print("Publishing ", data_to_publish, end = "  ##  ")
        added_item = gis.content.add({}, data = data_to_publish)
        published_item = added_item.publish(publish_parameters= {"City":"City", "Region": "State"})

        if published_item:
            print ("success. Assigning to: ", end="  #  ")
            result = published_item.reassign_to(row['username'])
            if result:
                print(row['username'])
            else:
                print("error")

    except Exception as pub_ex:
        print("Error : ", str(pub_ex))
