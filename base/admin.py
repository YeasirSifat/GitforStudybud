from django.contrib import admin

# Register your models here.
from .models import Room, Topics, Messange, User

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topics)
admin.site.register(Messange)
