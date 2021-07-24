from django.urls import path
from . import views

app_name = 'webkiosk'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.listfood, name='food-list'),
    path('food/new/', views.createfood, name='food-create'),
    path('food/<int:pk>', views.detailfood, name='food-detail'),
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),
]

#webkiosk/food/4
