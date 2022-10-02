from django.contrib import admin
from django.urls import path 
from .views import home , login_user , logout_user , update_book ,create_book , delete_book

urlpatterns = [
    path('' , home , name= 'home'),
    path('login/' , login_user , name= 'login'),
    path("update/<uuid:id>", update_book , name='update'),
    path("create/", create_book , name='create'),
    path('delete/<uuid:id>', delete_book , name='delete'),
    path ('logout/', logout_user , name='logout'),
]
