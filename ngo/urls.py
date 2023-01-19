from django.urls import path,include
from . import views

app_name = "ngo"
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
]