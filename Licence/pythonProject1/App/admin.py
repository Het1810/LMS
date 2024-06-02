from django.contrib import admin
from .models import Client, Licence

# Register your models here.


class Showclient(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'address', 'created_at','updated_at', 'is_flagged']


admin.site.register(Client, Showclient)


class Showlicence(admin.ModelAdmin):
    list_display = ['client', 'license_key', 'expiration_date']


admin.site.register(Licence, Showlicence)

