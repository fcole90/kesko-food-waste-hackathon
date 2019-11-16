import json
import os

import requests
import pandas as pd

from kesko_food_waste import settings

__API_KEY__ = "Ocp-Apim-Subscription-Key"

def main():
    # print(test_get().json())
    # print(get_all_stores().json().keys())
    print(products_to_dataset())


def test_get():
    url = "https://kesko.azure-api.net/ingredients/departments"
    response = requests.get(
        url=url,
        headers={
            __API_KEY__: settings.KESKO_API_KEY
        }
    )
    return response

def test_post():
    url = "https://kesko.azure-api.net/v1/search/stores"
    response = requests.post(
        url=url,
        headers={
            __API_KEY__: settings.KESKO_API_KEY,
            "content-type": "application/json",
            "accept": "application/json"
        },
        json={
        "filters": {
            "locationDistance": {
                "location": {
                    "lon": 24.933,
                    "lat": 60.164
                },
                "distance": 1
            }
        }}
    )
    return response

def get_all_stores():
    url = "https://kesko.azure-api.net/v1/search/stores"
    response = requests.post(
        url=url,
        headers={
            __API_KEY__: settings.KESKO_API_KEY,
            "content-type": "application/json",
            "accept": "application/json"
        },
        json={
            "filters": {
                "locationDistance": {
                    "location": {
                        "lon": 24.933,
                        "lat": 60.164
                    },
                    "distance": 100000
                }
            }}
    )
    return response


def get_all_products():
    url = "https://kesko.azure-api.net/v1/search/products"
    response = requests.post(
        url=url,
        headers={
            __API_KEY__: settings.KESKO_API_KEY,
            "content-type": "application/json",
            "accept": "application/json"
        }
    )
    return response


def stores_to_dataset():
    stores_response = get_all_stores().json()
    store_amount = stores_response['totalHits']
    store_data = stores_response['results']

    dataframe = pd.DataFrame(store_data)
    dataframe_file_name = "kmarket_all"
    try:
        dataframe.to_csv(path_or_buf=os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".csv"))
        dataframe.to_json(path_or_buf=os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".json"))
        with open(os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".json"), "w") as products_file:
            json.dump(obj=store_data, fp=products_file)
    except Exception as e:
        print(e)
        return False
    return True

def products_to_dataset():
    stores_response = get_all_products().json()
    store_amount = stores_response['totalHits']
    store_data = stores_response['results']

    dataframe = pd.DataFrame(store_data)
    dataframe_file_name = "products_all"
    try:
        dataframe.to_csv(path_or_buf=os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".csv"))
        with open(os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".json"), "w") as products_file:
            json.dump(obj=store_data, fp=products_file)
    except Exception as e:
        print(e)
        return False
    return True


def add_mock_data():
    kmarkets_json_filename = os.path.join(settings.PRIVATE_DATA_ROOT, "kmarket_all.json")
    items_json_filename = os.path.join(settings.PRIVATE_DATA_ROOT, "products_all.json")

    with open(kmarkets_json_filename) as kmarkets_json_file:
        kmarkets_data = json.load(kmarkets_json_file)

    with open(items_json_filename) as items_json_file:
        items_json_data = json.load(items_json_file)

    for i, market in enumerate(kmarkets_data):
        if market["Municipality"] in ["HELSINKI", "ESPOO", "VANTAA"]:
            print(i, json.dumps(market, indent=4, sort_keys=True))


    # print(json.dumps([(i, items_json_data[i]["labelName"]["english"]) for i in range(len(items_json_data))],
    #                  indent=4,
    #                  sort_keys=True))
    # for i, item in enumerate(items_json_data):
    #     if item["category"]["finnish"] in ["Maitokaappi", "Tuoretori"]:
    #         print((i, json.dumps(item["labelName"]["english"], indent=4, sort_keys=True)))
    #
    # print(json.dumps(items_json_data[88]["labelName"]["english"], indent=4, sort_keys=True))
    # print(json.dumps(items_json_data[88]["category"], indent=4, sort_keys=True))






if __name__ == "__main__":
    # main()
    # stores_to_dataset()
    # products_to_dataset()
    add_mock_data()