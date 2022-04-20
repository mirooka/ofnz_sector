from django.contrib import admin

# Register your models here.

from .models import OfnzUser, Profile

admin.site.site_header = 'OfnzSector Administration'


class OfnzUserAdmin(admin.ModelAdmin):
    # fields = ('__all__',)
    exclude = ('password', )

admin.site.register(OfnzUser, OfnzUserAdmin)
admin.site.register(Profile)
