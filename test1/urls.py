from django.urls import path

from test1 import views

urlpatterns =[
    path('',views.home,name="home"),
    path('team',views.team,name="team"),
]