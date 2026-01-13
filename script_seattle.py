### Does it always rain in Seattle? ###

# Imports
import json

# Opening and reading the files
with open ('precipitation.json', encoding='utf-8') as data_file :        
    data = json.load(data_file)          #reading in the JSON file

stations_data = {}
total_precipitation = 0 

with open ('stations.csv') as stations_csv :
    stations_csv.readline()
    for line in stations_csv:
        stations_split = line.split(',')
        stations_data[stations_split[0]] = {
            'state': stations_split[1],
            'station': stations_split[2]
        }

for location in stations_data :
    # Filtering for values from location
    measurements_location = []       #creating an empty list to store the measurements from Seattle
    for measurement in data :
        if measurement['station'] == stations_split[2] :      #this if-statement checks which measurements are from Seattle
            measurements_location.append(measurement)        #adding the Seattle measurements to the list

    # Creating a dictionary and a list with the months and the total precipitation per month
    monthly_precipitation = {}     #initializing an empty dictionary to store the months and their values
    for measurement_type in measurements_location :
        date = measurement_type['date']         #selecting the dates in the data
        date_split = date.split('-')            #splitting the dates up by the dashes
        values = measurement_type['value']          #selecting the precipitation value 
        if date_split[1] not in monthly_precipitation :     #selecting only the 2nd value (the month) and checking whether its in the dictionary
            monthly_precipitation[date_split[1]] = 0
        monthly_precipitation[date_split[1]] += values      #adding the values to the corresponding key (the month)

    total_monthly_precipitation = []        #initializing a list to store the total monthly precipitation values
    for month in monthly_precipitation :
        total_monthly_precipitation.append(monthly_precipitation[month])            #adding the values to the list
    total_yearly_precipitation = sum(total_monthly_precipitation)    
    total_precipitation += total_yearly_precipitation
    relative_monthly_precipitation = []         #initializing a list to store the relative monthly values
    for monthly_value in total_monthly_precipitation :
        relative_monthly_precipitation.append(monthly_value/total_yearly_precipitation)     #calculating the relative values and adding them to the list   

    # Formatting and saving the results in a JSON file
    results_json = {stations_split[0] : {        
            'station': stations_split[2],
            'state': stations_split[1],
            'total_monthly_precipitation': total_monthly_precipitation, 
            'total_yearly_precipitation' : total_yearly_precipitation,
            'relative_monthly_precipitation' : relative_monthly_precipitation}
            }
    
    # Calculating the relative yearly precipitation and adding it to the results dictionary
    for stations_split[0] in results_json :
        relative_yearly_precipitation = results_json[stations_split[0]]['total_yearly_precipitation']/total_precipitation
        results_json[stations_split[0]]['relative yearly precipitation'] = relative_yearly_precipitation

print(total_precipitation)
with open('results.json', 'a', encoding='utf-8') as results: 
    json.dump(results_json, results, indent=4)