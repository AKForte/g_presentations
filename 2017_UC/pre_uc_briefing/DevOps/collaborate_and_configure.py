# Script that creates a group in each of the City Enterprises then establishes a collaboration with the County enterprise.

from arcgis.gis import *
import os
from zipfile import ZipFile
import json
download_path = '/Users/atma6951/Documents/temp/e_configs'

# Get the list of cities and an independent list of Enterprises established.
city_list = ['fire', 'public_works']
enterpise_list = ['https://dev005220.esri.com/portal',
                  'https://dev005223.esri.com/portal']
admin_username = 'admin'
admin_password = 'esri.agp'

county_gis = GIS("https://dev005219.esri.com/portal",admin_username, admin_password, verify_cert=False)

# Loop through each city and create a group meant for collaboration
for city_id in list(range(len(city_list))):
    city_name = city_list[city_id]
    city_url = enterpise_list[city_id]

    print("Processing " + city_name.replace("_", " "))

    #create a GIS connection
    city_gis = GIS(city_url, admin_username, admin_password, verify_cert=False)
    print("    Connected to the department's ArcGIS Enterprise")

    #create the group meant for collaboration
    title = 'LA city GIS collaboration'
    tags = 'data, sharing, open data, sync'
    description = 'Group enabling GIS collaboration with the city of Los Angeles'
    snippet = 'This group contains content shared by and with the GIS of city of Los Angeles'

    gsr = city_gis.groups.search("title: LA city GIS collaboration", max_groups=1)
    collab_group = gsr[0] if len(gsr) > 0 else city_gis.groups.create(title, tags, description, snippet, access='public', thumbnail='collab_group.png')
    if collab_group:
        print("    Created group for collaboration")
    else:
        raise RuntimeError("Error creating group")

    #region Establish collaboration
    # find collab group in county
    county_collab_group = county_gis.groups.search('title:City {} dept. collaboration'.format(city_name.replace("_"," ")))

    # create a collaboration with county as host
    collab_name = 'LA ' + city_name.replace("_", " ") + " collab"
    county_collab = None

    county_exist_collabs = county_gis.collaborations.collaborations
    if len(county_exist_collabs) > 0:
        matching_collab = [co for co in county_exist_collabs if co.name==collab_name]
        if len(matching_collab) > 0:
            county_collab = matching_collab[0]
    else:
        collab_description = "Distributed GIS and data sharing initiative between LA city and its constituent departments"
        collab_wksp = 'LA ' + city_name.replace("_", " ") + " wksp"
        collab_wksp_desc = 'Workspace to share data'
        county_collab = county_gis.collaborations.create(collab_name, collab_description, collab_wksp,
                                         collab_wksp_desc, county_collab_group[0].id,
                                         "Administrator", "Administrator", "admin@dmail.com")
    if county_collab:
        print("    Successfully initiated a collaboration from city GIS")
    else:
        raise RuntimeError("Error creating collaboration")

    # invite guest / dept GIS
    county_exist_invitations = county_collab.invitations
    county_collab_invite = None
    if len(county_exist_invitations) > 0:
        matching_invite = [ii for ii in county_exist_invitations if ii['guestPortalUrl'] == city_gis._url]
        if len(matching_invite) > 0:
            county_collab_invite = matching_invite[0]
    else:
        county_collab_wksp = county_collab.workspaces[0]
        config_json = [{county_collab_wksp['id']:"sendAndReceive"}]
        county_collab_invite = county_collab.invite_participant(city_gis._url, config_json, 24)

    if county_collab_invite:
        print("    Successfully created an invitation for {} dept. GIS".format(city_name.replace("_", " ")))
    else:
        raise RuntimeError("Error creating invite for guest")

    # accept invitation in city GIS
    city_accept_response = city_gis.collaborations.accept_invitation('Administrator', 'Administrator', "admin@domain.com",
                                              invitation_file=county_collab_invite)

    if city_accept_response:
        print("    Successfully accepted invitation in {} dept. GIS".format(city_name.replace("_"," ")))

    # export invitation response from city GIS
    city_collab = city_gis.collaborations.collaborations[0]
    invite_response_file = city_collab.export_invitation(os.getcwd())
    if invite_response_file:
        print("    Successfully created invite response file for city GIS")

    # add group in city gis to workspace
    city_collab_wksp = city_collab.workspaces[0]
    group_add_result = city_collab.add_group_to_workspace(collab_group, city_collab_wksp)
    if group_add_result:
        print("    Successfully added group to dept's collaboration")

    # import the response back in the county GIS portal
    county_accept_status = county_collab.import_invitation_response(invite_response_file)
    if county_accept_status:
        print("    Successfully accepted dept's response back in city GIS")

    print("    Successfully completed the collaboration handshake!")
    sync_status = city_collab._force_sync(city_collab_wksp)
    print("---------------------------------------------------------------------------")
    print(" ")
    #endregion

    #region styling

    print("Styling " + city_name.replace("_", " "))

    # download the config archive from group that participates in collaboration
    # gsr = city_gis.groups.search("title: LA county GIS collaboration", max_groups=1)
    # city_collab_group = gsr[0]
    print("    Searching the collaboration group for content")

    # config_item = [i for i in city_collab_group.content() if i.title.endswith("config")][0]
    # config_file = config_item.download(download_path)
    print("    Downloaded the config archive")

    # extract the zip file
    # zf = ZipFile(config_file)
    # zf.extractall(download_path)
    # config_str_path = [afile for afile in zf.filelist if afile.filename.endswith('/config.json')][0]
    # config_str = zf.read(config_str_path)
    # config_str = "config.json"
    # config_dict = json.loads(download_path + "/" + city_name + "/" + config_str)
    print("    Reading configurations")

    # Set logo
    # print(download_path + "/" + city_name + '/logo.png')
    city_gis.ux.set_logo(download_path + "/" + city_name + '/logo.png')
    print("    Set Enterprise logo")

    # set background
    city_gis.ux.set_background(download_path + "/" + city_name + "/background.png")
    print("    Set Enterprise background")

    # set banner
    city_gis.ux.set_banner(download_path + "/" + city_name + "/banner.png")
    print("    Set Enterprise banner")

    # set name
    city_gis.ux.set_name_description(city_name.replace("_", " ").title() + " dept. GIS",
                                     "Distributed GIS between city govt. and departments")
    print("    Set Enterprise name")

    # set extent
    ext = {"type": "extent","xmin": -13159633.604126614,"ymin": 4044388.6476039286,"xmax": -13145941.30675904,
        "ymax": 4053939.28118214, "spatialReference": {"wkid": 102100}
    }
    # city_gis.update_properties({'defaultExtent': config_dict['extent']})
    city_gis.update_properties({'defaultExtent': ext})
    print("    Set Enterprise extent")

    # set featured groups
    param_dict = {"homePageFeaturedContent":"id:{}".format(collab_group.groupid),
                  "homePageFeaturedContentCount":12}
    city_gis.update_properties(param_dict)
    print("    Set home page featured content")
    print("============================================================")
    print(" ")