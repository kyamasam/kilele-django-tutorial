
from django.urls import path
from .views import ods, tennis_ods
urlpatterns = [
    path("", ods),
    path("tennis", tennis_ods)
]