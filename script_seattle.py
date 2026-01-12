## Title

#Imports
import json

with open ('precipitation.json', encoding='utf-8') as file :        
    data = json.load(file)          #reading in the JSON file

measurements_seattle = []       #creating an empty list to store the measurements from Seattle
for measurement in data :
    if measurement['station'] == 'GHCND:US1WAKG0038' :      #this if-statement checks which measurements are from Seattle
        measurements_seattle.append(measurement)        #adding the Seattle measurements to the list

months = {}
value = []
for measurement_type in measurements_seattle :
    date = measurement_type['date']
    date_split = date.split('-')
    value = measurement_type['value']
    if date_split[1] not in months :
        months[date_split[1]] = True
          