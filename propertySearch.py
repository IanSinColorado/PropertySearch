# Illustrates an API call to Datafiniti's Product Database for hotels.
import requests
# import urllib.parse
import json

# Set your API parameters here.
API_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4b2JodDJqeDhycjJuZXp3djIwaW5ubGVpdG5scnZjNSIsImlzcyI6ImRhdGFmaW5pdGkuY28ifQ.u9TOuHOvcdMWbJT_g7li6t53Nwro1AEmWWNQVnx-9o4k7XqkE2j6XTxD5vgiKHkkILHKCDrsBoVy4at8I5Tgn3clB5YZLMC4XIGKmDr3RZWtRRWvICfg33y7bWVc8gD1A-r_fEvRGIb6b0DhdfNBLaJFQu26h038J6bYZJmSSjoBCcAwS_7Z8i7Wh2QckWj_Pwrzbti444YFZod2S_tRFivlM9YQ974CM6a9d-vjaO3gZjjALqWLWI-Qk4n3cYhb1w099ZQ4xqadXnKd2l8wkd7yqRZ4AqAsob5Rr4IKLZghccMkCD6Gvek5aJZ_AeLmgMO8hJ8eBhBOez0-CbbWLa0FzHsfjtrqxqxMFUKpLxJX89T60bnZMxAuzsY64D5xrLNETpvUsru_6v2qwHz0YyiZA3xZtz6ilgRnQ_xNN41cUMU7H5rHNHdCJRRDTVza2KYkFt0yjz8lnIumA2YxY0cf7RCS9fbwnnYDBv6Jl0hwb2JthDqtNVmMIlExb5EvoZJGiKgM7tF6-KVeqjRS7wofnkDMxkVheVrQqq9vzqUmDZNp9RN5ErRMAIFFmTMlwKs0wBjbqrswE9EiHQ6zV6O9jEfIoCZTImRynCtMsd9WZ1MNCcKiIiRbSTUOdVNgo9NI-de9388iD54cwgRcDP0GeyI_PEXrY3jLiM3kK_A'
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
