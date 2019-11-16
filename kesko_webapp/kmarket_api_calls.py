import requests
import json

from kesko_food_waste import settings


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
        "Ocp-Apim-Subscription-Key": settings.KESKO_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    data = []
    for result in json.loads(r.content)["results"]:
        temp = {"id": result["Id"], "name": result["Name"], "coordinates": result["Coordinate"]}
        data.append(temp)

    return data


def get_available_markets(ean):
    url = 'https://kesko.azure-api.net/v2/products?ean=' + ean
    payload = {}
    headers = {
        "Ocp-Apim-Subscription-Key": settings.KESKO_API_KEY
    }

    r = requests.get(url, data=json.dumps(payload), headers=headers)


    data = []
    for store in json.loads(r.content)[0]["stores"]:
        temp = {"id": store["id"]}
        data.append(temp)

    return data


def combine(inside_circle, available):
    my_map = {}
    common_markets = []

    for market in inside_circle:
        my_map[market["id"]] = True

    for market in available:
        if market["id"] in my_map:
            common_markets.append(market)

    return common_markets


def get_product_id(query):

    url = 'https://kesko.azure-api.net/v1/search/products'
    payload = {
        "query": query
    }
    headers = {
        "Ocp-Apim-Subscription-Key": settings.KESKO_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)

    data = []
    for result in json.loads(r.content)["results"]:
        temp = {"ean": result["ean"], "pictureUrls": result["pictureUrls"], "labelName": result["labelName"]}
        data.append(temp)

    return data
