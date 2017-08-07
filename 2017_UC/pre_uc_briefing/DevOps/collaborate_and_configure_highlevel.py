# Script that creates a group in each of the City Enterprises then establishes a collaboration with the County enterprise.

from arcgis.gis import *
import os

host_gis = GIS("https://dev005219.esri.com/portal/", "admin",'esri.agp')
guest_gis = GIS("https://dev005223.esri.com/portal/", "admin", "esri.agp")


result = host_gis.admin.collaborations.collaborate_with(guest_gis, 'high_level_collab', 'auto collaborations')
print(str(result))