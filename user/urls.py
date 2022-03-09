from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('add_user/',views.add_user,name='add_user'),
    path('',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('poster/<int:pk>/',views.poster,name='poster'),
]