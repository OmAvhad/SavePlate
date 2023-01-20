from django.urls import path,include
from . import views

app_name = "user"
urlpatterns = [
    path('user/dashboard',views.dashboard,name="dashboard"),
]