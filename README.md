# My Django Cinema App

This is a Django-based application for booking cinema seats.

## Features

- User authentication and registration
- Browse available movies
- View movie details including start and end times
- Book cinema seats for a chosen movie
- View booked seats and avoid double-booking

## Installation

### Prerequisites
- Python 3.x
- pip

### Steps

1. **Clone the repository**:
    ```
    git clone [YOUR REPOSITORY URL HERE]
    ```

2. **Navigate to the directory**:
    ```
    cd [YOUR REPOSITORY NAME HERE]
    ```

3. **Set up a virtual environment (Optional but Recommended)**:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the requirements**:
    ```
    pip install -r requirements.txt
    ```

5. **Run migrations**:
    ```
    python manage.py migrate
    ```

6. **Start the development server**:
    ```
    python manage.py runserver
    ```

Now, you should be able to access the application at `http://127.0.0.1:8000/`.

## Usage

1. Register as a new user or log in.
2. Browse available movies.
3. Click on a movie to view details.
4. Book seats as desired.
5. View your bookings in your profile (or wherever applicable).
6. You can also create rooms, movies, schedules from or view and delete bookings from admin.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
