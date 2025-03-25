from django.contrib import admin
from App.models import *


@admin.register(jus)#decorateur et permet de trier mes element dans ma base de donnée 
class jus_admin(admin.ModelAdmin):
    list_display =("name",)
    list_filter = ["name",]
    search_fields = ["name","date"]
    list_per_page = 5
#admin.site.register(jus, jus_admin)


@admin.register(Contact)
class contact_admin(admin.ModelAdmin):
    list_display =("name","email",)
    list_filter = ["name",]
    search_fields = ["name",]
    readonly_fields = ["email"]
#admin.site.register(Contact, contact_admin)

# Register your models here.

