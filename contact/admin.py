from django.contrib import admin
from .models import Group, Job, Relationship, Contact

# Register your models here.
admin.site.register(Group)
admin.site.register(Job)
admin.site.register(Relationship)
admin.site.register(Contact)
