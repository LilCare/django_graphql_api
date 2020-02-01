from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('user/<str:username>/', views.userLookup, name='userLookup'),
  path('createUser/<str:username>/<str:password>', views.createUser, name='createUser'),
  path('userLogin/<str:username>/<str:password>', views.userLogin, name='userLogin')
]