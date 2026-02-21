"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('', views.games_page_redirector),
    path('games/', views.get_all_games, name='games'),
    path('games/<int:game_id>/', views.game_view, name='game'),
    path('games/edit/<int:game_id>/', views.edit_game, name='edit-game'),
    path('games/add/', views.add_game, name='add-game'),
    path('company/<slug:slug>/', views.company_view, name='company-view'),
    path('category/<int:category_id>/', views.category_view, name='category-view'),
    path('category/add/', views.add_category, name='add-category'),
]