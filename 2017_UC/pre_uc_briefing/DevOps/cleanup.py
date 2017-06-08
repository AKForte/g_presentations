# Script that creates a group in each of the City Enterprises then establishes a collaboration with the County enterprise.

from arcgis.gis import *
import os
from shutil import rmtree

#empty the config download path
# try:
#     rmtree('/Users/atma6951/Documents/temp/e_configs')
#     print("Removed temp directory")
#     os.mkdir('/Users/atma6951/Documents/temp/e_configs')
#     print("Created new temp directory")
# except:
#     pass

# Get the list of cities and an independent list of Enterprises established.
city_list = ['fire', 'public_works']
enterpise_list = ['https://dev005220.esri.com/portal',
                  'https://dev005223.esri.com/portal']
admin_username = 'admin'
admin_password = 'esri.agp'

county_gis = GIS("https://dev005219.esri.com/portal",admin_username, admin_password, verify_cert=False)

print("Clean up starting with county GIS")
# clean up collaboration in county GIS
county_collab_list = county_gis.collaborations.collaborations
for co in county_collab_list:
    print("   deleting collaboration" + co['name'], end=" | ")
    delete_result = co.delete()
    if delete_result:
        print(str(delete_result))

# Loop through each city and create a group meant for collaboration
for city_id in list(range(len(city_list))):
    city_name = city_list[city_id]
    city_url = enterpise_list[city_id]

    print("Cleaning up " + city_name + " GIS")

    #create a GIS connection
    city_gis = GIS(city_url, admin_username, admin_password, verify_cert=False)
    print("    Connected to the city's ArcGIS Enterprise")

    city_exist_collabs = city_gis.collaborations.collaborations
    for co in city_exist_collabs:
        print("    deleting collaboration" + co['name'], end=" | ")
        delete_result = co.remove_participation()
        if delete_result:
            print(str(delete_result))

    #delete the config file
    sr = city_gis.content.search('title:{} config'.format(city_name.replace("_"," ")))
    for i in sr:
        i.delete()
        print("    deleted config item: " + i.title)

    #reset the background file
    city_gis.ux.set_background(is_built_in=False)
    print("    reset Background")

    city_gis.ux.set_banner('banner-2',True)
    print("    reset Banner")

    city_gis.ux.set_name_description("ArcGIS Enterprise", " ")
    print("    reset name and description")

    city_gis.ux.set_logo(None)
    print("    reset logo")

    param_dict = {"homePageFeaturedContent": "id:",
                  "homePageFeaturedContentCount": 12}
    city_gis.update_properties(param_dict)
    print("    reset featured content")

print("========================================================================")
print("Finish up")
print("   Searching for collabs in county")
county_gis = GIS("https://dev005219.esri.com/portal",admin_username, admin_password, verify_cert=False)
county_collab_list = county_gis.collaborations.collaborations
print("   number of county collabs: " + str(len(county_collab_list)))

for city_id in list(range(len(city_list))):
    city_name = city_list[city_id]
    city_url = enterpise_list[city_id]

    print("Searching for collabs in " + city_name + " GIS")

    #create a GIS connection
    city_gis = GIS(city_url, admin_username, admin_password, verify_cert=False)
    print("    Connected to the city's ArcGIS Enterprise")

    city_exist_collabs = city_gis.collaborations.collaborations
    print("    number of city collabs: " + str(len(city_exist_collabs)))
