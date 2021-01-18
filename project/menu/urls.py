from django.urls import path, include
from .views import menu_

urlpatterns = [
    path('', menu_.as_view(), name = 'menu')
]