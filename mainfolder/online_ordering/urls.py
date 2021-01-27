from django.contrib import path
from online_ordering import views

urlpatterns = [
    path('',views.index,name="index"),
]
