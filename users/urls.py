"""
@author: Thomason
@contact: ThomasonZhao@outlook.com 
@create: 2020/4/25 12:32 PM 
"""
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('add/', views.add, name='add'),
    # path('view/', views.view, name='veiw'),
    path('get-img/', views.get_img),
]
