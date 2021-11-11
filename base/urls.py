from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("room/<str:pk>",views.room,name="room"),
    path("create/",views.createRoom,name="create_room"),
    path("update/<str:pk>",views.updateRoom,name="update_room"),
    path("delete/<str:pk>",views.deleteRoom,name="delete_room")

]