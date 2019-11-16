from django.http import JsonResponse
from django.shortcuts import render


def index_api(request):
    """
    Simple api example.

    Parameters
    ----------
    request: a Request object

    Returns
    -------

    """
    data = {
        "is_online": True
    }
    return JsonResponse(data=data)


def optimise_market_food_waste(request):
    return JsonResponse(data={
        "store_list": [
            {
                "storeId": "C122",
                "optimisation_cost": 12.5,
                "items": [
                    {
                        "ean": "291828880199",
                        "name": "Coca-Cola"
                    }
                ]
            }
        ]
    })