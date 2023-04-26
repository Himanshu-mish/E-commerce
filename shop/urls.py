from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path("" , views.index , name = "ShopHome"),
    path("shop/" , views.index),
    path("about/" , views.about),
    path("contact/" , views.contact),
    path("tracker/" , views.tracker),
    path("checkout/" , views.checkout),
    path("product/<int:myid>/" , views.products , name="productView"),
    # path("basic/" , views.basic)

    
]