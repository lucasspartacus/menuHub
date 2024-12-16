"""
URL configuration for menuhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from menus import views

urlpatterns = [
    path('', views.show_restaurants),
    path('new/', views.new_restaurant),
    path('edit/<int:restaurant_id>', views.edit_restaurant),
    path('delete/<int:restaurant_id>', views.delete_restaurant),
    # menu itens urls
    path('menus/<int:restaurant_id>', views.show_menu_itens, name="menu"),
    path('menus/<int:restaurant_id>/new/', views.new_menu_item, name="new"),
    path('menus/<int:restaurant_id>/edit/<int:item_id>/',
    views.edit_menu_item, name="edit"),
    path('menus/<int:restaurant_id>/delete/<int:item_id>/',
    views.delete_menu_item, name="delete")
]
