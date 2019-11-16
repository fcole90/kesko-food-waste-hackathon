import json
import os

import requests
import pandas as pd

from kesko_food_waste import settings

__API_KEY__ = "Ocp-Apim-Subscription-Key"
__API_SECRET__ = "16e6175abde7464ba975ca6a63c532e7"

def main():
    # print(test_get().json())
    # print(get_all_stores().json().keys())
    print(products_to_dataset())

def test_get():
    url = "https://kesko.azure-api.net/ingredients/departments"
    response = requests.get(
        url=url,
        headers={
            __API_KEY__: __API_SECRET__
        }
    )
    return response

def test_post():
    url = "https://kesko.azure-api.net/v1/search/stores"
    response = requests.post(
        url=url,
        headers={
            __API_KEY__: __API_SECRET__,
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
            __API_KEY__: __API_SECRET__,
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
            __API_KEY__: __API_SECRET__,
            "content-type": "application/json",
            "accept": "application/json"
        },
        # json={
        #     "filters": {
        #         "locationDistance": {
        #             "location": {
        #                 "lon": 24.933,
        #                 "lat": 60.164
        #             },
        #             "distance": 100000
        #         }
        #     }}
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
        dataframe.to_json(path_or_buf=os.path.join(settings.PRIVATE_DATA_ROOT, dataframe_file_name + ".json"))
    except Exception as e:
        print(e)
        return False
    return True


if __name__ == "__main__":
    main()