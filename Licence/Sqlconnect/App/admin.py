from .models import CustomUser, CreClients, CreClientLicense
from django.contrib import admin

# Register your models here.


class ShowCustomUser(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff')  # Customize displayed fields


admin.site.register(CustomUser, ShowCustomUser)

class showClient(admin.ModelAdmin):
    list_display = ('intid', 'nvarname', 'nvaremail', 'nvaraddress', 'nvarcontact', 'bitistrashed')


admin.site.register(CreClients, showClient)

class ShowClientlicense(admin.ModelAdmin):
    list_display = ('intid', 'intclientid', 'nvarkey', 'intvalidity', 'bitactive', 'nvarreference', 'bitistrashed')


admin.site.register(CreClientLicense, ShowClientlicense)
