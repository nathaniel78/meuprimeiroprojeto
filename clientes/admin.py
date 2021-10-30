from django.contrib import admin
from .models import Person

# Adicionando classes ao admin
admin.site.register(Person)
