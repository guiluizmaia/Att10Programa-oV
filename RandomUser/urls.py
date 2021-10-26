from django.urls import path
from RandomUser.views import index

urlpatterns = [
    path('random/', index),
]
