import math

import numpy as np
from geopy import distance

def get_geodesic_distance(lat1, long1, lat2, long2):
    return distance.geodesic((lat1, long1), (lat2, long2)).km

def get_items_expiring_soon(market):
    return [item["ean"] for item in market["availableProducts"] if item["amountOnCloseExpiry"] > 0]

def get_distance(from_x, from_y, to_x, to_y):
    return np.sqrt((from_x - to_x)**2 + (from_y - to_y)**2)

def get_items_opt_cost(market, items_list):
    needed_on_expiry = [it for it in items_list if it in get_items_expiring_soon(market)]
    completeness_frac = len(needed_on_expiry) / len(items_list)
    return (1 - completeness_frac) * 100

def get_store_popularity(market):
    return 0


def get_market_coordinates(market):
    coords = market["Coordinate"]
    return coords["Latitude"], coords["Longitude"]


def get_total_stores_popularity():
    return 1

def get_item_selling_probability(market):
    return get_store_popularity(market=market) / get_total_stores_popularity()