from django.urls import path,include
from . import views

app_name = "org"
urlpatterns = [
    path('org/dashboard',views.dashboard,name="dashboard"),
]