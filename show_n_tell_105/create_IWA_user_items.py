# Publisher persona
# Script to publish content for each user.

from arcgis.gis import *
import pandas as pd
import json
# os.chdir(os.path.dirname(__file__))

# Read the csv containing user accounts and their territory info
print("======================================== \n")
df = pd.read_csv('.\\IWA_users_to_add.csv')
print(df[['username', 'assigned_state']])
print("======================================== \n")

# Read template web map
template_webmap_dict = dict()
with open('.\\user_content_new\\web_map_simple.json', 'r') as webmap_file:
            template_webmap_dict = json.load(webmap_file)

# Connect to the GIS
gis = GIS("https://dev002783.esri.com/portal")

# Loop through each user and publish the content
for index, row in df.iterrows():
    try:
        data_to_publish = '.\\user_content_new\\' + row['assigned_state'] + ".csv"

        print("Publishing ", data_to_publish, end = " # ")
        added_item = gis.content.add({}, data = data_to_publish)
        published_item = added_item.publish()

        if published_item is not None:
            # publish web map
            print('webmaps', end= " ## ")
            user_webmap_dict = template_webmap_dict
            user_webmap_dict['operationalLayers'][0]['itemId'] = published_item.itemid
            user_webmap_dict['operationalLayers'][0]['layerType'] = "ArcGISFeatureLayer"
            user_webmap_dict['operationalLayers'][0]['title'] = published_item.title
            user_webmap_dict['operationalLayers'][0]['url'] = published_item.url + r"/0"

            web_map_properties = {'title': '{0} response locations'.format(row['Fullname']),
                                  'type': 'Web Map',
                                  'snippet': 'Areas affected by hurricane Mathew under the supervision of' +\
                                             '{0}'.format(row['Fullname']),
                                  'tags': 'ArcGIS Python API',
                                  'typeKeywords' : "Collector, Explorer Web Map, Web Map, Map, Online Map",
                                  'text': json.dumps(user_webmap_dict)}

            web_map_item = gis.content.add(web_map_properties)

            print("success. Assigning to: ", end="  #  ")
            result1 = published_item.reassign_to(row['username'])
            result2 = web_map_item.reassign_to(row['username'])
            if (result1 and result2) is not None:
                print(row['username'])
            else:
                print("error")
        else:
            print(" error publishing csv")

    except Exception as pub_ex:
        print("Error : ", str(pub_ex))
