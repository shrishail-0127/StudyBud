from django.urls import path
from . import views


urlpatterns = [
    
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerPage, name='register'),

    path('',views.home,name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('profile/<int:pk>/', views.userProfile, name='user-profile'),

    path('create-room/',views.createRoom, name="create-room"),
    path('update-room/<int:pk>/',views.updateRoom, name='update-Room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-Room'),
    path('delete-message/<int:pk>/',views.deleteMessage, name='delete-Message'),
    path('update-user/',views.updateUser,name='update-user'),
]


