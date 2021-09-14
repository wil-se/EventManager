from django.contrib import admin
from .models import Match, Team, Reservation, Gym, Seat, SeatGymConfig

# Register your models here.
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Reservation)
admin.site.register(Gym)
admin.site.register(Seat)
admin.site.register(SeatGymConfig)