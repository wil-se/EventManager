from django.db import models

# softdelete

class Team(models.Model):
    name = models.CharField(max_length=64)
    gym = models.ForeignKey('reservation.Gym', default=None, on_delete=models.SET_DEFAULT, null=True)
    image = models.ImageField(upload_to='teams/', default='/global_assets/images/placeholders/placeholder.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Squadra'
        verbose_name_plural = 'Squadre'

    

class Match(models.Model):
    home_team = models.ForeignKey('reservation.Team', default=None, on_delete=models.SET_DEFAULT, related_name="home_team")
    outside_team = models.ForeignKey('reservation.Team', default=None, on_delete=models.SET_DEFAULT, related_name="outside_team")
    date = models.DateField(default=None)
    gym = models.ForeignKey('reservation.Gym', default=None, on_delete=models.SET_DEFAULT, null=True)

    def __str__(self):
        return f'{self.home_team} vs {self.outside_team} il {self.date.strftime("%d/%m%Y")}'
    
    class Meta:
        verbose_name = 'Partita'
        verbose_name_plural = 'Partite'



class Reservation(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    match = models.ForeignKey('reservation.Match', default=None, on_delete=models.SET_DEFAULT, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} per {self.match.date} {self.match.home_team} vs {self.match.outside_team}'    
    
    class Meta:
        verbose_name = 'Prenotazioni'
        verbose_name_plural = 'Prenotazioni'



class Gym(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestre'
