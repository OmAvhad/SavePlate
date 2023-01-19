from django.urls import path,include
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home,name="index"),
    path('login/',views.login_template,name="login"),
    path('register/<slug:slug>',views.register_template,name="register"),
    path('register2/<slug:user_id>',views.register2_template,name="register2"),
    path('logout',views.logout_url,name="logout")
]