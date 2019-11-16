import numpy as np

def get_items_expiring_soon(market):
    return []

def get_distance(from_x, from_y, to_x, to_y):
    return np.sqrt((from_x - to_x)**2 + (from_y - to_y)**2)

def get_items_opt_cost(market, items_list):
    cost = 0
    for item in items_list:
        if item not in get_items_expiring_soon(market):
            cost += 1
    return cost / len(items_list)

def get_store_popularity(market):
    return 0


def get_market_coordinates(market):
    coords = market["Coordinate"]
    return coords["Latitude"], coords["Longitude"]


def get_total_stores_popularity():
    return 1

def get_item_selling_probability(market):
    return get_store_popularity(market=market) / get_total_stores_popularity()