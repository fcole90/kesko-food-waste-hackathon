from django.http import JsonResponse
from django.shortcuts import render

from kesko_webapp.kmarket_api_calls import get_nearest_markets, get_available_markets, get_product_id


def frontend(request):
    return render(request, 'kesko_webapp/frontend.html')


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


def nearest_markets(request):
    lon = request.GET.get('lon', 0)
    lat = request.GET.get('lat', 0)
    distance = request.GET.get('distance', 0)
    return JsonResponse(get_nearest_markets(lon, lat, distance), safe=False)


def available_markets(request):
    ean = request.GET.get('ean', "0")
    return JsonResponse(get_available_markets(ean), safe=False)


def product_id(request):
    query = request.GET.get('query', "0")
    return JsonResponse(get_product_id(query), safe=False)
