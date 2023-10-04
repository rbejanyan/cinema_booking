from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from .models import Room, Schedule, Booking, Movie
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': rooms})


def booking(request, room_id, schedule_id):
    room = get_object_or_404(Room, pk=room_id)
    schedule = get_object_or_404(Schedule, pk=schedule_id, room=room)

    # Calculate booked seats for this schedule
    booked_seats_objs = Booking.objects.filter(schedule=schedule)
    booked_seats = [f"{seat.row_number}-{seat.seat_number}" for seat in booked_seats_objs]

    # Generate a list of all seats with their respective strings
    all_seats = [
        {
            "row": row,
            "seat": seat,
            "seat_str": f"{row}-{seat}"
        }
        for row in range(1, room.rows + 1)
        for seat in range(1, room.seats_per_row + 1)
    ]

    if request.method == "POST":
        selected_seats = [(int(seat.split('-')[0]), int(seat.split('-')[1])) for seat in request.POST.getlist('seats')]

        # Check if any of the selected seats are already booked
        for row, seat_num in selected_seats:
            existing_booking = Booking.objects.filter(schedule=schedule, row_number=row, seat_number=seat_num)
            if not existing_booking.exists():
                booking1 = Booking.objects.create(schedule=schedule, row_number=row, seat_number=seat_num, user=request.user)
                booking1.save()
            else:
                return HttpResponseBadRequest("One or more of the selected seats are already booked.")

        return redirect('confirm_booking', schedule_id=schedule.id)

    context = {
        'room': room,
        'schedule': schedule,
        'booked_seats': booked_seats,
        'all_seats': all_seats
    }
    return render(request, 'booking.html', context)






def confirm_booking(request, schedule_id):
    # Implement confirmation logic, potentially showing the selected seats, total cost, etc.
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    bookings = Booking.objects.filter(schedule=schedule, user=request.user)
    return render(request, 'confirmation.html', {'booking': bookings.first()})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': rooms})

def movie_list(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    now = timezone.now()
    movies = Movie.objects.filter(room=room).prefetch_related('schedule_set')

    movie_data = []
    for movie in movies:
        available_schedules = movie.schedule_set.filter(start_time__gt=now)
        movie_data.append({
            'movie': movie,
            'available_schedules': available_schedules,
        })

    context = {
        'room': room,
        'movie_data': movie_data,
        'now': now,
    }
    return render(request, 'movie_list.html', context)

