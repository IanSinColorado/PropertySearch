# Illustrates an API call to Datafiniti's Product Database for hotels.
import requests
# import urllib.parse
import json

# Set your API parameters here.
API_token = ''
format = 'JSON'
query = 'country:US AND city:(Boulder OR Lyons OR Longmont OR Denver OR Broomfield OR Erie) AND mostRecentStatus:("Short Term Rental" OR Rental) AND province:CO AND { prices.amountMax:1500 }'
num_records = 10
download = False

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
r = requests.post('https://api.datafiniti.co/v4/properties/search',json=request_data,headers=request_headers);

addresses = list()
listingNames = list()

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
        except:
            print("Could not read records")
    except:
        print("Could not read JSON")
else:
    print('Request failed')

# Print properties
for i, address in enumerate(addresses):
    print(addresses[i])
    print(listingNames[i])
    print('***************')
    print()
