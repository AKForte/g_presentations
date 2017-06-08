# Script to read list of groups from a csv and create them on the portal.
print("RUNNING CREATE GROUPS")
print("---------------------")
from arcgis.gis import *
import pandas as pd
import csv

csv_path = ".\\groups.csv"

# connect to gis
gis = GIS("https://dev002346.esri.com/portal", "Admin", "esri.agp")

# create groups from csv
df = pd.read_csv(csv_path)
print(df[["title", "access", "sortField"]])
print("====================================================================== \n")

with open(csv_path, 'r') as csv_handle:
    reader = csv.DictReader(csv_handle)
    for row in reader:
        try:
            print(" Creating group: ", row['title'], end= "  ##  ")
            result = gis.groups.create_from_dict(row)
            if result:
                print("success")

        except Exception as create_ex:
            print("Error... ", str(create_ex))