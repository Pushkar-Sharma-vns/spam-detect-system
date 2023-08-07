from django.contrib import admin

from .models import ContactList, SpamDatabase

admin.site.register(ContactList)
admin.site.register(SpamDatabase)