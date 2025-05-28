Concert Booking System

A Python CLI application for browsing and booking tickets to live music events. Users can browse events by genre, view artist lineups, and purchase tickets. Data is persisted using SQLite and SQLAlchemy ORM.

Features





Browse upcoming concerts by genre.



View artists performing at each event.



Book tickets and view booking history.



Manage customers, events, artists, and tickets via CLI.



Input validation and informative error messages.

Installation





Clone the repository:

git clone <repository-url>
cd concert_booking



Install dependencies using Pipenv:

pipenv install



Activate the virtual environment:

pipenv shell



Run the application:

pipenv run start

Usage





Run the CLI with pipenv run start.



Follow the menu prompts to:





Create, delete, or view customers, events, artists, and tickets.



Browse events by genre.



View artists for an event or tickets for a customer.



Search for objects by attributes (e.g., event by name).

Data Model





Customer: Stores customer details (name, email).



Event: Stores event details (name, date, genre).



Artist: Stores artist details (name, genre).



Ticket: Links customers to events (price, purchase date).



Relationships:





One-to-many: Customer to Ticket.



Many-to-many: Event to Artist.



One-to-many: Event to Ticket.

Dependencies





Python 3.11



SQLAlchemy



Click

Project Structure

concert_booking/
├── Pipfile
├── README.md
├── concert_booking/
│   ├── __init__.py
│   ├── cli.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── artist.py
│   │   ├── customer.py
│   │   ├── event.py
│   │   └── ticket.py
│   └── database.py