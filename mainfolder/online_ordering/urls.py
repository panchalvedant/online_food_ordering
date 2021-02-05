

from django.urls import path
from online_ordering import views

urlpatterns = [
    path('',views.index,name="index"),
]

