## Title

#   Imports
import json

#   Opening and reading the file
with open ('precipitation.json', encoding='utf-8') as file :        
    data = json.load(file)          #reading in the JSON file

#   Filtering for values from Seattle
measurements_seattle = []       #creating an empty list to store the measurements from Seattle
for measurement in data :
    if measurement['station'] == 'GHCND:US1WAKG0038' :      #this if-statement checks which measurements are from Seattle
        measurements_seattle.append(measurement)        #adding the Seattle measurements to the list

#   Creating a dictionary and a list with the months and the total precipitation per month
monthly_precipitation = {}     #initializing an empty dictionary to store the months and their values
for measurement_type in measurements_seattle :
    date = measurement_type['date']     #selecting the dates in the data
    date_split = date.split('-')        #splitting the dates up by the dashes
    values = measurement_type['value']      #selecting the precipitation value 
    if date_split[1] not in monthly_precipitation : #selecting only the 2nd value (the month) and checking whether its in the dictionary
        monthly_precipitation[date_split[1]] = 0
    monthly_precipitation[date_split[1]] += values      #adding the values to the corresponding key (the month)

total_monthly_precipitation = []    #initializing a list to store the total monthly precipitation values
for month in monthly_precipitation :
    total_monthly_precipitation.append(monthly_precipitation[month]) #adding the values to the list
print(total_monthly_precipitation)


