from django.urls import path,include
from . import views

app_name = "user"
urlpatterns = [
    path('dashboard',views.dashboard,name="dashboard"),
]