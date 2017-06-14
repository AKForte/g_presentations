# ArcGIS API for Python - for developers
Demo material used for pre-UC director's briefing on Wed Jun 7, 2017.

## Story
For this demo, let us consider this case. I am a GIS officer for the city of Los Angeles. I am tasked to empower each of the city departments with GIS. The initiative is to encourage setting up an instance of ArcGIS Enterprise in every department and to join them in a collaboration, creating a distributed GIS. For this demo we will be considering Fire and Public works depts.

As an admin, I want to automate this process of deploying a fully functional departmental GIS. I have decided to use a combination of Chef cookbooks and the Python API to install the ARcGIS Enterprise and configure including creating a collaboration, styling and theming the website and seeding it with initial content.

This is my sequence of steps
 - Use Chef to install the full stack single node ArcGIS Enterprise for the fire and public works departments
 - then kick off a python script which uses the python api to do a sequence of things needed for the collaboration
 - it creates a group in each of the dept gis
 - initiates a collab from city GIS
 - accept collab and completes the handshake
 - gets config package
 - configures the dept GIS with approved styling and content.


## Files
This repo consists of the following files

 - Cleanup scripts
   - cleanup_styling.py - just to undo the theming
   - cleanup.py - undos everything including theming and removing collaboration
 - Worker scripts
   - collaborate_and_configure.py - single script performs collaboration and styling
   - establish_collaboration.py - script that only performs collaboration
   - style_portal.py - script that only performs theming
 - helper files
   - helper_files/fire_config - folder with banner, background, config.json, logo images for fire dept
   - helper_files/pwd_config - similar for pwd dept.
 - collaborate_and_configure_nb.ipynb - notebook that walks through the scripts.

All other files are helper files.

## Portals used for this demo
  - https://dev005219.esri.com/portal - the fully configured City GIS
  - https://dev005229.esri.com/portal - GIS for fire dept.
  - https://dev005223.esri.com/portal - GIS for Public Works dept.

## Running the demo
To run the full demo,
 - execute cleanup.py which will bring the portals to base state
 - execute collaborate_and_configure.py which will establish collaboration and perform the theming.

To only perform either collaboration or theming, run the appropriate scripts separately.