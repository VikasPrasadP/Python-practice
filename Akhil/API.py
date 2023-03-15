import requests
import json
import pprint
url = "http://worldtimeapi.org/api/timezone/America/Argentina/Salta"
params = {'area' : 'America',
        'location' :'argentina' 
        }
response = requests.get(url,params)
if response.status_code == 200:
    data = json.loads(response.text)
    #pprint.print(data)
    Time = data['datetime']
    print("The time zone is",Time)
else:
    print(f"Error: {response.status_code}")