from django.urls import path
from . import views


urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.movie_list, name='movie_list'),
    path('booking/<int:room_id>/<int:schedule_id>/', views.booking, name='booking'),
    path('confirm_booking/<int:schedule_id>/', views.confirm_booking, name='confirm_booking'),
]
