from django.urls import path 
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.main_paeg, name = 'main_page' ),
    path('create-skill/',  views.create_skill, name = 'skill'),
    
    path('logout/',  views.logoutuser, name = 'logout'),
    
    path('skills/',  views.addskill, name = 'addskills'),
    path('celect/',  views.post_single, name = 'celectskills'),
 
    path('favourite_add/',  views.post_single, name = 'favourite_add'),
    path('favourite_list/',  views.post_single, name = 'favourite_list'),
    path('create/',  views.createSkill, name = 'cretenew'),
]