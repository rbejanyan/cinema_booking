from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rows = models.IntegerField()
    seats_per_row = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.name} at {self.start_time} in {self.room.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    seat_number = models.IntegerField()

    class Meta:
        unique_together = [['schedule', 'row_number', 'seat_number']]

    def __str__(self):
        return f"{self.user.username} - {self.schedule} - Row: {self.row_number}, Seat: {self.seat_number}"
