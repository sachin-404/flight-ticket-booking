# Flight Ticket Booking

This repository contains the codes for flight booking system built using django.

## Features
- **User Authentication**: Token-based authentication system to ensure secure user access.
- **Flight Search**: Users can search for available flights based on date and time.
- **Flight Booking**: Users can book flights based on seat availability 
- **Booking Management**: Users can view and manage their flight bookings.
- **Admin Privileges**: Admins have the ability to add and remove flights through the Django admin panel.


## Tech Used
- **Backend**: Django
- **Frontend**: Bootstrap
- **Database**: SQL

## Database
- Django Default Auth_system and access control
### Flights Table
- flight_name
- departure_time
- seats

### Users
- it has two types of users: **admin** and **regular user**
- User(SignUp, Login, Logout),  Admin[Login, create using django-admin]
- admins can:
    - add new flight details
    - remove flights
    

- regular users can:
    - View all available flights and details
    - book flights
    - view their bookings