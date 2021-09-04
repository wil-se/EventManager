from django.db import models

# softdelete

category_choices = (('Seconda divisione maschile', 'Seconda divisione maschile'), 
                    ('Seconda divisione femminile', 'Seconda divisione femminile'),
                    ('MINIVOLLEY', 'MINIVOLLEY'))

class Team(models.Model):
    name = models.CharField(max_length=64)
    gym = models.ForeignKey('reservation.Gym', default=None, on_delete=models.SET_DEFAULT, null=True)
    image = models.ImageField(upload_to='teams/', default='/global_assets/images/placeholders/placeholder.jpg')
    logo = models.ImageField(upload_to='teams/', default='/logo.png')
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Squadra'
        verbose_name_plural = 'Squadre'

    

class Match(models.Model):
    home_team = models.ForeignKey('reservation.Team', default=None, on_delete=models.SET_DEFAULT, related_name="home_team")
    outside_team = models.ForeignKey('reservation.Team', default=None, on_delete=models.SET_DEFAULT, related_name="outside_team")
    date = models.DateTimeField(default=None)
    gym = models.ForeignKey('reservation.Gym', default=None, on_delete=models.SET_DEFAULT, null=True)
    category = models.CharField(verbose_name='Categoria', choices=category_choices, max_length=256, blank=True, null=True)
    tournament = models.CharField(verbose_name='Girone', max_length=1, blank=True, null=True)
    tournament_day = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    

    def __str__(self):
        return f'{self.home_team} vs {self.outside_team} il {self.date.strftime("%d/%m%Y")}'
    
    class Meta:
        verbose_name = 'Partita'
        verbose_name_plural = 'Partite'



class Reservation(models.Model):
    user = models.ForeignKey('authentication.User', default=None, on_delete=models.SET_DEFAULT, null=True)
    match = models.ForeignKey('reservation.Match', default=None, on_delete=models.SET_DEFAULT, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} per {self.match.date} {self.match.home_team} vs {self.match.outside_team}'    
    
    class Meta:
        verbose_name = 'Prenotazioni'
        verbose_name_plural = 'Prenotazioni'



class Gym(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    longitude = models.FloatField(verbose_name='Longitudine', max_length=1, blank=True, null=True)
    latitude = models.FloatField(verbose_name='Longitudine', max_length=1, blank=True, null=True)
    seats = models.IntegerField(verbose_name="Posti a sedere", default=0)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestre'
