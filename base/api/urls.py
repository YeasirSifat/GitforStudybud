from django.urls import path
from .import views

urlpatterns = [

 path('',views.getRoute),
 path('rooms/',views.getRooms),
 path('users/',views.getUsers),
 path('room/<str:pk>/',views.getRoom),
path('user/<str:pk>/',views.getUser),
]