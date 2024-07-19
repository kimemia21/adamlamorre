from django.urls import re_path
from . import views

urlpatterns = [
   re_path("all",views.all),
   re_path("login",views.login),
   re_path('signup',views.signup),

   re_path("token",views.test_token)
    
]
