from django.db import models
from django.urls import reverse

# Create your models here.

class Attack(models.Model):
    name = models.CharField(max_length=25)
    damage = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('attack_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    TYPES = [
        ('NO', 'Normal'),
        ('FI', 'Fire'),
        ('WA', 'Water'),
        ('EL', 'Electric'),
        ('GR', 'Grass'),
        ('IC', 'Ice'),
        ('FG', 'Fighting'),
        ('PO', 'Poison'),
        ('GR', 'Ground'),
        ('FL', 'Flying'),
        ('PS', 'Psychic'),
        ('BU', 'Bug'),
        ('RO', 'Rock'),
        ('GH', 'Ghost'),
        ('DR', 'Dragon')
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default='NO'
    )
    level = models.IntegerField()
    hp = models.IntegerField()
    attacks = models.ManyToManyField(Attack)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'pokemon_id' : self.id})

class Training(models.Model):
    date = models.DateField()
    SESSIONS = [
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('E', 'Evening')
    ]
    session = models.CharField(
        max_length= 1,
        choices = SESSIONS,
        default='M'
    )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_session_display()} on {self.date}"
