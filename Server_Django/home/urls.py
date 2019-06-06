from django.urls import path
from .views import home_visit


urlpatterns = [
    path('', home_visit),

]
