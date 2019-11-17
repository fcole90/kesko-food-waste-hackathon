import json
import os

from kesko_food_waste import settings
from optimisation import optimise

def get_some_ean():
    items_json_filename = os.path.join(settings.PRIVATE_DATA_ROOT, "products_all.json")

    with open(items_json_filename) as items_json_file:
        items_json_data = json.load(items_json_file)

    return [item["ean"] for item in items_json_data[:15]]

def get_ranked_markets_interface(ean_items_list, user_position, max_time=None):
    data_market_id_item_ean_filename = os.path.join(settings.PRIVATE_DATA_ROOT, "data_market_id_item_ean_all.json")

    with open(data_market_id_item_ean_filename) as data_market_id_item_ean_file:
        data_market_id_item_ean = json.load(data_market_id_item_ean_file)

    best_rank, best_rank_costs = optimise.get_best_ranked_markets(
        market_list=data_market_id_item_ean,
        items_list=ean_items_list,
        user_position=user_position,
        distance_weight=100,
        completeness_weight=10,
        threshold_cost=None,
        max_iterations=500,
        max_survival_probability=0.9,
        population_max_size=12,
        retain_parents=True,
        max_time=max_time
    )
    return best_rank, best_rank_costs,

if __name__ == "__main__":
    print(json.dumps(get_ranked_markets_interface(ean_items_list=get_some_ean(), user_position=(60.1618222, 24.737745), max_time=1),
                     indent=4))