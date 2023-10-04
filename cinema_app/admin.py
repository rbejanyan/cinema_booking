from django.contrib import admin
from .models import Room, Movie, Schedule, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'start_time', 'end_time']
    readonly_fields = ['poster_preview']

    def poster_preview(self, obj):
        return obj and f'<img src="{obj.poster.url}" width="200"/>'
    poster_preview.allow_tags = True
    poster_preview.short_description = "Poster Preview"

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['movie', 'room', 'start_time', 'end_time']

admin.site.register(Booking)

