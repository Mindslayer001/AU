
from django.urls import path
from .views import index, compare, forecast, dash
urlpatterns = [
    path("",index, name='index'),
    path('compare/',compare,name='compare'),
    path('forecast/',forecast,name='forecast'),
    path('dash/', dash, name='dash'),
]
