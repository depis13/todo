from django.contrib import admin

from organisation.models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'creation_timestamp')
