import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# bajar de itunes 50 nombres de canciones de weezer
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))     te imprime todo el registro

# queremos solo unas partes del registro
o = response.json()
for result in o["results"]:
    print(result["trackName"])
