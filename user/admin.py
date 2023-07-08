from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','id','role','created_at','update_at')
    list_filter = ("role",)
    search_fields = ['name','email','id',]
    ordering = ('-created_at',)
admin.site.register(User,UserAdmin)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user_id','aparment','id','street','postal_code','city','country','created_at')
    list_filter = ('city','country','postal_code',)
    search_fields = ['aparment','street','postal_code','city','country','id',]
    ordering = ('-created_at',)
admin.site.register(UserAddress,AddressAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id','bio','id','avatar','created_at')
    list_filter = ("bio",)
    search_fields = ['bio','user_id','id',]
    ordering = ('-created_at',)
admin.site.register(UserProfiles,ProfileAdmin)

