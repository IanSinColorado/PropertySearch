import requests
import json

# Set your API parameters here.
API_token = ''
format = 'JSON'
query = 'country:US AND city:(Boulder OR Lyons OR Longmont OR Denver OR Broomfield OR Erie) AND mostRecentStatus:("Short Term Rental" OR Rental) AND province:CO AND { prices.amountMax:1500 }'
num_records = 10
download = False

# Logic for prompting the user for data
useMenu = input("Would you like to use the interactive menu or current query? ('im' or 'cq') ")

menuFlag = False
whileFlag = True

while whileFlag:
    if useMenu == "im":
        whileFlag = False
        menuFlag = True
    elif useMenu == "cq":
        whileFlag = False
        print("Using current query.")
    else:
        useMenu = input("Enter 'im' for interactive menu or 'cq' for current query ")

if menuFlag == True:
    # Logic for menu
    # resetting the old query to add to it
    query = ''

    # Getting country
    countryFlag = True
    print("Would you like to search in a specific country?")
    countryInput = input("Enter the abbreviated country name (like US) or 'None' ")
    print()
    if countryInput == 'None':
        countryFlag = False
    else:
        query += 'country:' + countryInput

    # Getting cities
    cityFlag = True
    whileFlag = True

    cityInput = input("Enter a city you would like to search in or 's' to not add a city. ")
    cities = list()
    
    if cityInput == 's':
        whileFlag = False
        cityFlag = False

    while whileFlag:
        if cityInput == 's':
            whileFlag = False
        else:
            cities.append(cityInput)
            cityInput = input("Enter another city you would like to search in or 's' to stop adding cities. ")

    # Adding cities to query
    if cityFlag:
        if countryFlag:
            query += ' AND '

        if len(cities) == 1:
            query += 'city:(' + cities[0] + ')'
        elif len(cities) > 1:
            query += 'city:(' + cities[0]
            for i, city in enumerate(cities):
                if i == 0:
                    continue
                query += ' OR ' + city
            query += ')'
        else:
            print("No Cities")

    # Getting most recent statuses
    statusFlag = True
    whileFlag = True
    
    statusInput = input("What status to search? 'Rental', 'For Sale', 'Off Market', 'Pending', 'Rent To Own', 'Rental', 'Short Term Rental', 'Sold', or 'None' ")
    while whileFlag:
        if statusInput == 'None':
            whileFlag = False
            statusFlag = False
        elif statusInput in ['Rental', 'For Sale', 'Off Market', 'Pending', 'Rent To Own', 'Rental', 'Short Term Rental', 'Sold']:
            whileFlag = False
        else:
            input("Please enter one of the following inputs: 'Rental', 'For Sale', 'Off Market', 'Pending', 'Rent To Own', 'Rental', 'Short Term Rental', 'Sold', or 'None' ")

    if statusFlag:
        if countryFlag or cityFlag:
            query += ' AND '

        query += 'mostRecentStatus:"' + statusInput + '"'

    # Getting province (or State)
    provinceFlag = True
    provinceInput = input("Enter the abbreviated country name (like CO for Colorado) or 'None' ")

    if provinceInput == 'None':
        provinceFlag = False

    if provinceFlag:
        if countryFlag or cityFlag or statusFlag:
            query += ' AND '

        query += 'province:' + provinceInput

    # Price max 
    priceFlag = True
    priceInput = input("Enter the max price you wish to search for or 'None' ")

    if priceInput == 'None':
        priceFlag = False
        
    if priceFlag:
        if countryFlag or cityFlag or statusFlag or provinceFlag:
            query += ' AND '
        if priceInput.isdigit():
            query += '{ prices.amountMax:' + priceInput + ' }'
        else:
            print("Not a number, entering >1")
            query += '{ prices.maxAmount:>1 }'


    # Ask how many properties to search for
    searchNumInput = input("How many properties would you like to search? (Enter a number) ")

    while not searchNumInput.isdigit():
        searchNumInput = input("Enter the number of results to search for as a number. ")

    num_records = int(searchNumInput)

print(query)

request_headers = {
    'Authorization': 'Bearer ' + API_token,
    'Content-Type': 'application/json',
}

request_data = {
    'query': query,
    'format': format,
    'num_records': num_records,
    'download': download
}

# Make the API call.
r = requests.post('https://api.datafiniti.co/v4/properties/search',json=request_data,headers=request_headers)

addresses = list()
listingNames = list()
datesUpdated = list()
cities = list()
prices = list()

# Do something with the response.
if r.status_code == 200:
    # print(r.content)
    # print(type(r))
    try:
        print(r.json())
        try:
            records = r.json()["records"]
            for record in records:
                keys = list(record.keys())

                if 'address' in keys:
                    # print(record["address"])
                    addresses.append(record["address"])
                else:
                    addresses.append(None)

                if 'listingName' in keys:
                    # print(record["listingName"])
                    listingNames.append(record["listingName"])
                else:
                    listingNames.append(None)

                if 'dateUpdated' in keys:
                    datesUpdated.append(record["dateUpdated"])
                else:
                    datesUpdated.append(None)

                if 'city' in keys:
                    cities.append(record["city"])
                else:
                    cities.apped(None)

                try:
                   prices.append(record["prices"][0]["amountMax"])
                except:
                        prices.append(None)
        except:
            print("Could not read records")
    except:
        print("Could not read JSON")
else:
    print('Request failed')

# Make the dates human readable
humanDates = list()
for date in datesUpdated:
    humanDate = date[5:7] + "/" + date[8:10] + "/" + date[:4]
    humanDates.append(humanDate)

print()

# Print properties
for i, address in enumerate(addresses):
    print('*****************************************************************')
    try:
        print("Name: " + listingNames[i])
    except:
        print("Name: None")

    try:
        print("Address: " + addresses[i])
    except:
        print("Address: None")

    try:
        print("City: " + cities[i])
    except:
        print("City: None")

    try:
        print("Price: " + str(prices[i]))
    except:
        print("Price: None")

    try:
        print("Most Recent Update: " + humanDates[i])
    except:
        print("Most Recent Update: None")

    print('*****************************************************************')
    print()
