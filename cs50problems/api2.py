import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
    for result in data["results"]:
        print("Track Name:", result["trackName"])
else:
    print("Error:", response.status_code)
