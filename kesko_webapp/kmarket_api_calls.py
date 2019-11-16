import requests
import json


key = "16e6175abde7464ba975ca6a63c532e7"


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
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    return json.loads(r.content)


def get_available_markets(ean):

    url = 'https://kesko.azure-api.net/v2/products?ean=' + ean
    payload = {}
    headers = {
        "Ocp-Apim-Subscription-Key": key
    }

    r = requests.get(url, data=json.dumps(payload), headers=headers)

    return json.loads(r.content)

