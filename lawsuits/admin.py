from lib2to3.pytree import Base
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Customer, Lawsuit, Movement

class CustomerInLine(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInLine,)

class LawsuitAdmin(admin.ModelAdmin):
    search_fields = ['number', 'description']

class MovementAdmin(admin.ModelAdmin):
    search_fields = ['description', 'date_added']


#teste

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Lawsuit, LawsuitAdmin)
admin.site.register(Movement, MovementAdmin)
