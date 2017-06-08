#script to update the portal and create groups
from arcgis.gis import GIS
from zipfile import ZipFile
import json

county_gis = GIS("https://dev005219.esri.com/portal", "admin", "esri.agp", verify_cert=False)

# Get the list of cities and an independent list of Enterprises established.
city_list = ['pasadena', 'santa_monica']
enterpise_list = ['https://dev005220.esri.com/portal',
                  'https://dev005223.esri.com/portal']
admin_username = 'admin'
admin_password = 'esri.agp'
download_path = '/Users/atma6951/Documents/temp/e_configs'

# Loop through each city and create a group meant for collaboration
for city_id in list(range(len(city_list))):
    city_name = city_list[city_id]
    city_url = enterpise_list[city_id]

    print("Processing " + city_name.replace("_", " "))

    #create a GIS connection
    city_gis = GIS(city_url, admin_username, admin_password, verify_cert=False)
    print("    Connected to the city's ArcGIS Enterprise")

    #download the config archive from group that participates in collaboration
    gsr = city_gis.groups.search("title: LA county GIS collaboration", max_groups=1)
    city_collab_group = gsr[0]
    print("    Searching the collaboration group for content")

    config_item = [i for i in city_collab_group.content() if i.title.endswith("config")][0]
    config_file = config_item.download(download_path)
    print("    Downloaded the config archive")

    #extract the zip file
    zf = ZipFile(config_file)
    zf.extractall(download_path)
    config_str_path = [afile for afile in zf.filelist if afile.filename.endswith('/config.json')][0]
    config_str = zf.read(config_str_path)
    config_dict = json.loads(config_str)
    print("    Reading configurations")

    #Set logo
    # print(download_path + "/" + city_name + '/logo.png')
    city_gis.ux.set_logo(download_path + "/" + city_name + '/logo.png')
    print("    Set Enterprise logo")

    #set background
    city_gis.ux.set_background(download_path +"/" + city_name + "/background.png")
    print("    Set Enterprise background")

    # set banner
    city_gis.ux.set_banner(download_path + "/" + city_name + "/banner.png")
    print("    Set Enterprise banner")

    # set name
    city_gis.ux.set_name_description(city_name.replace("_", " ").title() + " city GIS",
                                     "Distributed GIS between county and city govt.")
    print("    Set Enterprise name")

    # set extent
    city_gis.update_properties({'defaultExtent':config_dict['extent']})
    print("    Set Enterprise extent")