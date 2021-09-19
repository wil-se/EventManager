from django.db import models
from reservation.models import *
from authentication.models import User, Manager


category_choices = (('Seconda divisione maschile', 'Seconda divisione maschile'), 
                    ('Seconda divisione femminile', 'Seconda divisione femminile'),
                    ('MINIVOLLEY', 'MINIVOLLEY'))


class VolleyCoach(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.role = 4
        

    def __str__(self):
        if self.first_name and self.last_name:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.email

    class Meta:
        verbose_name = 'Allenatore pallavolo'
        verbose_name_plural = 'Allenatori pallavolo'


class VolleyManager(Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.role = 3

    class Meta:
        verbose_name = 'Manager palestra'
        verbose_name_plural = 'Manager palestra'


class VolleyGym(Place):
    class Meta:
        verbose_name = 'Palestre pallavola'
        verbose_name_plural = 'Palestre pallavolo'


class VolleyGymConf(PlaceConfig):
    class Meta:
        verbose_name = 'Configurazione palestre pallavolo'
        verbose_name_plural = 'Configurazioni palestre pallavolo'


class VolleyTeam(models.Model):
    coach = models.ForeignKey('volley.VolleyCoach', on_delete=models.CASCADE)
    gym = models.ForeignKey('volley.VolleyGym', default=None, on_delete=models.SET_DEFAULT, null=True)
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='teams/', default='/global_assets/images/placeholders/placeholder.jpg')
    logo = models.ImageField(upload_to='teams/', default='/logo.png')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Squadra'
        verbose_name_plural = 'Squadre'


class VolleyMatch(Event):
    home_team = models.ForeignKey('volley.VolleyTeam', default=None, on_delete=models.SET_DEFAULT, related_name="home_team")
    outside_team = models.ForeignKey('volley.VolleyTeam', default=None, on_delete=models.SET_DEFAULT, related_name="outside_team")
    category = models.CharField(verbose_name='Categoria', choices=category_choices, max_length=256, blank=True, null=True)
    tournament = models.CharField(verbose_name='Girone', max_length=1, blank=True, null=True)
    tournament_day = models.IntegerField(default=0)
    code = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.home_team} vs {self.outside_team} il {self.date.strftime("%d/%m%Y")}'
    
    class Meta:
        verbose_name = 'Partita pallavolo'
        verbose_name_plural = 'Partite pallavolo'


class VolleyReservation(Reservation):
    pass