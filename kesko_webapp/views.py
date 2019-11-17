import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from kesko_webapp.kmarket_api_calls import get_nearest_markets, get_available_markets, get_product_id
from optimisation.optimise_interface import get_ranked_markets_interface


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
    data = request.GET
    return JsonResponse(data=data)
    # return JsonResponse(data=get_nearest_markets(23.55, 23.66, 5))

@csrf_exempt
def optimise_market_food_waste(request):
    # return HttpResponseBadRequest()
    data = json.loads(request.body)
    print(type(data))
    print(data)
    print(request.GET)
    print()
    print(data.keys())
    ean_items_list = data.get("items", None)
    user_lat = data.get("user_lat", None)
    user_lon = data.get("user_lon", None)
    max_time = data.get("max_time", None)

    if ean_items_list is None:
        return HttpResponseBadRequest("Missing required parameter 'items':"
                                      " Should contain a list of dictionaries\n"
                                      "containing valid 'ean' keys.")
    if None in [user_lat, user_lon]:
        return HttpResponseBadRequest("Missing required parameters 'user_lat', 'user_lon'")

    try:
        best_rank, best_rank_costs = get_ranked_markets_interface(ean_items_list, (user_lat, user_lon), max_time)
        return JsonResponse({"best_ranked_markets": best_rank, "best_ranked_costs": best_rank_costs})
    except Exception as e:
        return HttpResponseBadRequest(f"Something went wrong: {e.__repr__()}")


def nearest_markets(request):
    lon = request.GET.get('lon', 0)
    lat = request.GET.get('lat', 0)
    distance = request.GET.get('distance', 0)
    return JsonResponse(get_nearest_markets(lon, lat, distance), safe=False)


def available_markets(request):
    ean = request.GET.get('ean', "0")
    return JsonResponse(get_available_markets(ean))


def product_id(request):
    query = request.GET.get('query', "0")
    return JsonResponse(get_product_id(query), safe=False)
