from django.contrib import admin
from .models import ServiceCategory, Service, Subservice, PeopleCategory

# Register your models here.
admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(Subservice)
admin.site.register(PeopleCategory)