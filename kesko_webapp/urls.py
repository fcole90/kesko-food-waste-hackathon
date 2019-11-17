from django.urls import path

from . import views

app_name = "kesko_webapp"
urlpatterns = [
    path('', views.index_api, name='index'), # Root, we can just return 'True'
    path('optimise_market_food_waste', views.optimise_market_food_waste, name="optimise_market_food_waste"),
    path('nearest_markets', views.nearest_markets, name="nearest_markets"),
    path('frontend/', views.frontend, name="frontend"),
    path('available_markets', views.available_markets, name="available_markets"),
    path('product_id', views.product_id, name="product_id"),
    path('final_stores', views.final_stores, name="final_stores"),

]