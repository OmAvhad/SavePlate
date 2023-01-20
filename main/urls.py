from django.urls import path,include
from . import views

app_name = "main"
urlpatterns = [
    path('',views.home,name="index"),
    path('login/',views.login_template,name="login"),
    path('achievements/',views.achievements_template,name="achivements"),
    path('contributers/',views.contributers_template,name="contributers"),
    path('aboutus/',views.aboutus_template,name="aboutus"),
    path('register/<slug:slug>',views.register_template,name="register"),
    path('register2/<slug:user_id>',views.register2_template,name="register2"),
    path('logout',views.logout_url,name="logout"),
    path('apply-to-donate',views.apply_donate,name="apply_donate") 
]