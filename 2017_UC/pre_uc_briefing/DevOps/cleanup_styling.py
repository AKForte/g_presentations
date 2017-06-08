# Clean up script to undo the styling changes

from arcgis.gis import *
import os
from shutil import rmtree

#empty the config download path
rmtree('/Users/atma6951/Documents/temp/e_configs')
print("Removed temp directory")
os.mkdir('/Users/atma6951/Documents/temp/e_configs')
print("Created new temp directory")

# Get the list of cities and an independent list of Enterprises established.
city_list = ['pasadena', 'santa_monica']
enterpise_list = ['https://dev005220.esri.com/portal',
                  'https://dev005223.esri.com/portal']
admin_username = 'admin'
admin_password = 'esri.agp'


# Loop through each city and create a group meant for collaboration
for city_id in list(range(len(city_list))):
    city_name = city_list[city_id]
    city_url = enterpise_list[city_id]

    print("Cleaning up " + city_name + " GIS")

    try:
        #create a GIS connection
        city_gis = GIS(city_url, admin_username, admin_password, verify_cert=False)
        print("    Connected to the city's ArcGIS Enterprise")

        #reset the background file
        city_gis.ux.set_background(is_built_in=False)
        print("    reset Background")

        city_gis.ux.set_banner('banner-2',True)
        print("    reset Banner")

        city_gis.ux.set_name_description("ArcGIS Enterprise", " ")
        print("    reset name and description")

        city_gis.ux.set_logo(None)
    except:
        continue