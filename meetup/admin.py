from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    # The fields in the tuple are the fields you want to display
    list_display = ("title", "location", "date")
    # The fields in the tuple are the fields you filter by
    list_filter = ("location", "date")
    # slug is the field that should be prepopulated
    # ("title",) This is a tuple of all the fields that should be used to prepopulate the slug field
    # prepopulated_fields doesn't work with readonly_fields, so readonly_fields will have to be removed for this to work
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
