from django.contrib import admin
from .models import Game, Record, Location

# Register your models here.
admin.site.register(Game)
admin.site.register(Record)
admin.site.register(Location)