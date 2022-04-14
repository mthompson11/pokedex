from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('pokemon/', views.pokemon_index, name = 'index'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name = 'detail'),
    path('pokemon/create/', views.PokemonCreate.as_view(), name = 'pokemon_create'),
    path('pokemon/<int:pk>/update/', views.PokemonUpdate.as_view(), name = 'pokemon_update'),
    path('pokemon/<int:pk>/delete/', views.PokemonDelete.as_view(), name = 'pokemon_delete'),
    path('pokemon/<int:pokemon_id>/add_training/', views.add_training, name = 'add_training'),
    path('attack/', views.AttackList.as_view(), name = 'attack_index'),
    path('attack/<int:pk>/', views.AttackDetail.as_view(), name = 'attack_detail'),
    path('attack/create/', views.AttackCreate.as_view(), name = 'attack_create'),
    path('attack/<int:pk>/update', views.AttackUpdate.as_view(), name = 'attack_update'),
    path('attack/<int:pk>/delete', views.AttackDelete.as_view(), name = 'attack_delete'),
    path('pokemon/<int:pokemon_id>/assoc_attack/<int:attack_id>/', views.assoc_attack, name = 'assoc_attack')
]