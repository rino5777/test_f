from django.urls import path 
from . import views
from user.views import LoginView
app_name = 'user'


urlpatterns = [
    path('', views.account, name = 'account' ),  # главная  account-login.html
    
    path('authorization', views.authorization, name = 'authorization' ),
    path('login',  LoginView.as_view(), name = 'login'),
    

]