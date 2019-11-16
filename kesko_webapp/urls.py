from django.urls import path

from . import views

app_name = "kesko_webapp"
urlpatterns = [
    path('', views.index_api, name='index'), # Root, we can just return 'True'
    path('optimise_market_food_waste', views.optimise_market_food_waste, name="optimise_market_food_waste"),
    path('nearest_markets', views.nearest_markets, name="nearest_markets"),
    path('frontend/', views.frontend, name="frontend"),
]