import requests
import json


def get_nearest_markets(lon, lat, distance):

    url = 'https://kesko.azure-api.net/v1/search/stores'
    payload = {
        "filters": {
            "locationDistance": {
                "location": {
                    "lon": lon,
                    "lat": lat
                },
                "distance": distance
            }
        }
    }

    headers = {
        "Ocp-Apim-Subscription-Key": "16e6175abde7464ba975ca6a63c532e7",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    return json.loads(r.content)
