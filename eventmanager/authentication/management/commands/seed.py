from django.core.management.base import BaseCommand, CommandError
import random
from datetime import datetime
from authentication.models import ThemeConfig
from colorfield.fields import ColorField



class Command(BaseCommand):

    def add_arguments(self, parser):
        #parser.add_argument('path', type=str, help='randomize database')
        pass
    
    def handle(self, *args, **options):
        print("SEED")
        default_light = ThemeConfig()
        default_light.name = "Light default"
        default_light.navbar = ColorField('#27598E')
        default_light.save()
