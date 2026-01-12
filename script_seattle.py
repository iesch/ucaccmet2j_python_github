## Title

#Imports
import json

with open ('precipitation.json', encoding='utf-8') as file :
    data = json.load(file)

measurements_seattle = []
for measurement in data :
    if measurement['station'] == 'GHCND:US1WAKG0038' :
        print(measurement)


   