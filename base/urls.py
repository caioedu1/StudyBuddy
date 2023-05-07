from django.urls import path
from .views import (home, room, createRoom, 
                    updateRoom, deleteRoom, loginUser, 
                    logoutUser, registerUser, deleteMessage, 
                    userProfile, updateUser, topicsPage, activityPage)

urlpatterns = [
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('register', registerUser, name='register'),
    path('profile/<str:pk>', userProfile, name='user_profile'),

    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    
    path('create_room/', createRoom, name='create_room'),
    path('update_room/<str:pk>/', updateRoom, name='update_room'),
    path('delete_room/<str:pk>/', deleteRoom, name='delete_room'),
    path('delete_message/<str:pk>/', deleteMessage, name='delete_message'),
    
    path('update_user/<str:pk>/', updateUser, name='update_user'),
    
    path('topics/', topicsPage, name='topics'),
    path('activity/', activityPage, name='activity')
    
]
