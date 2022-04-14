from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Attack
from .forms import TrainingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon' : pokemon})

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    id_list = pokemon.attacks.all().values_list('id')
    attacks_pokemon_doesnt_have = Attack.objects.exclude(id__in=id_list)
    training_form = TrainingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon' : pokemon,
        'training_form' : training_form,
        'attacks' : attacks_pokemon_doesnt_have
        })

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'type', 'level', 'hp']

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = '__all__'

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon/'

def add_training(request, pokemon_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.pokemon_id = pokemon_id
        new_training.save()
    return redirect('detail', pokemon_id = pokemon_id)

class AttackList(ListView):
    model = Attack

class AttackDetail(DetailView):
    model = Attack

class AttackUpdate(UpdateView):
    model = Attack
    fields = '__all__'

class AttackDelete(DeleteView):
    model = Attack
    success_url = '/attack/'

def assoc_attack(request, pokemon_id, attack_id):
    Pokemon.objects.get(id=pokemon_id).attacks.add(attack_id)
    return redirect('detail', pokemon_id=pokemon_id)

class AttackCreate(CreateView):
    model = Attack
    fields = '__all__'