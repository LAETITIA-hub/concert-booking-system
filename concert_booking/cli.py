import click
from datetime import datetime
from concert_booking.models.customer import Customer
from concert_booking.models.event import Event
from concert_booking.models.artist import Artist
from concert_booking.models.ticket import Ticket
from concert_booking.database import init_db, Session
from sqlalchemy import Table, Column, Integer, ForeignKey

# Define association table for many-to-many relationship
event_artists = Table('event_artists', Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('artist_id', Integer, ForeignKey('artists.id'))
)

GENRES = ('Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop')

@click.group()
def cli():
    init_db()

def display_menu():
    click.echo("\nConcert Booking System")
    click.echo("1. Manage Customers")
    click.echo("2. Manage Events")
    click.echo("3. Manage Artists")
    click.echo("4. Manage Tickets")
    click.echo("5. Browse Events by Genre")
    click.echo("6. View Artists for Event")
    click.echo("7. View Customer Tickets")
    click.echo("8. Exit")

@cli.command()
def run():
    while True:
        display_menu()
        choice = click.prompt("Enter your choice (1-8)", type=int)
        if choice == 8:
            click.echo("Exiting...")
            break
        elif choice == 1:
            manage_customers()
        elif choice == 2:
            manage_events()
        elif choice == 3:
            manage_artists()
        elif choice == 4:
            manage_tickets()
        elif choice == 5:
            browse_events_by_genre()
        elif choice == 6:
            view_artists_for_event()
        elif choice == 7:
            view_customer_tickets()
        else:
            click.echo("Invalid choice. Please try again.")

def manage_customers():
    while True:
        click.echo("\nCustomer Management")
        click.echo("1. Create Customer")
        click.echo("2. Delete Customer")
        click.echo("3. List All Customers")
        click.echo("4. Find Customer by ID")
        click.echo("5. Find Customer by Email")
        click.echo("6. Back")
        choice = click.prompt("Enter your choice (1-6)", type=int)
        if choice == 6:
            break
        elif choice == 1:
            name = click.prompt("Enter name")
            email = click.prompt("Enter email")
            try:
                Customer.create(name, email)
                click.echo("Customer created successfully.")
            except Exception as e:
                click.echo(f"Error: {str(e)}")
        elif choice == 2:
            customer_id = click.prompt("Enter customer ID", type=int)
            if Customer.delete(customer_id):
                click.echo("Customer deleted successfully.")
            else:
                click.echo("Customer not found.")
        elif choice == 3:
            customers = Customer.get_all()
            for c in customers:
                click.echo(c)
        elif choice == 4:
            customer_id = click.prompt("Enter customer ID", type=int)
            customer = Customer.find_by_id(customer_id)
            click.echo(customer if customer else "Customer not found.")
        elif choice == 5:
            email = click.prompt("Enter email")
            customer = Customer.find_by_email(email)
            click.echo(customer if customer else "Customer not found.")
        else:
            click.echo("Invalid choice.")

def manage_events():
    while True:
        click.echo("\nEvent Management")
        click.echo("1. Create Event")
        click.echo("2. Delete Event")
        click.echo("3. List All Events")
        click.echo("4. Find Event by ID")
        click.echo("5. Back")
        choice = click.prompt("Enter your choice (1-5)", type=int)
        if choice == 5:
            break
        elif choice == 1:
            name = click.prompt("Enter event name")
            date_str = click.prompt("Enter event date (YYYY-MM-DD)")
            genre = click.prompt("Enter genre", type=click.Choice(GENRES))
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d')
                Event.create(name, date, genre)
                click.echo("Event created successfully.")
            except Exception as e:
                click.echo(f"Error: {str(e)}")
        elif choice == 2:
            event_id = click.prompt("Enter event ID", type=int)
            if Event.delete(event_id):
                click.echo("Event deleted successfully.")
            else:
                click.echo("Event not found.")
        elif choice == 3:
            events = Event.get_all()
            for e in events:
                click.echo(e)
        elif choice == 4:
            event_id = click.prompt("Enter event ID", type=int)
            event = Event.find_by_id(event_id)
            click.echo(event if event else "Event not found.")
        else:
            click.echo("Invalid choice.")

def manage_artists():
    while True:
        click.echo("\nArtist Management")
        click.echo("1. Create Artist")
        click.echo("2. Delete Artist")
        click.echo("3. List All Artists")
        click.echo("4. Find Artist by ID")
        click.echo("5. Back")
        choice = click.prompt("Enter your choice (1-5)", type=int)
        if choice == 5:
            break
        elif choice == 1:
            name = click.prompt("Enter artist name")
            genre = click.prompt("Enter genre", type=click.Choice(GENRES))
            try:
                Artist.create(name, genre)
                click.echo("Artist created successfully.")
            except Exception as e:
                click.echo(f"Error: {str(e)}")
        elif choice == 2:
            artist_id = click.prompt("Enter artist ID", type=int)
            if Artist.delete(artist_id):
                click.echo("Artist deleted successfully.")
            else:
                click.echo("Artist not found.")
        elif choice == 3:
            artists = Artist.get_all()
            for a in artists:
                click.echo(a)
        elif choice == 4:
            artist_id = click.prompt("Enter artist ID", type=int)
            artist = Artist.find_by_id(artist_id)
            click.echo(artist if artist else "Artist not found.")
        else:
            click.echo("Invalid choice.")

def manage_tickets():
    while True:
        click.echo("\nTicket Management")
        click.echo("1. Create Ticket")
        click.echo("2. Delete Ticket")
        click.echo("3. List All Tickets")
        click.echo("4. Find Ticket by ID")
        click.echo("5. Back")
        choice = click.prompt("Enter your choice (1-5)", type=int)
        if choice == 5:
            break
        elif choice == 1:
            customer_id = click.prompt("Enter customer ID", type=int)
            event_id = click.prompt("Enter event ID", type=int)
            price = click.prompt("Enter ticket price", type=float)
            try:
                Ticket.create(customer_id, event_id, price)
                click.echo("Ticket created successfully.")
            except Exception as e:
                click.echo(f"Error: {str(e)}")
        elif choice == 2:
            ticket_id = click.prompt("Enter ticket ID", type=int)
            if Ticket.delete(ticket_id):
                click.echo("Ticket deleted successfully.")
            else:
                click.echo("Ticket not found.")
        elif choice == 3:
            tickets = Ticket.get_all()
            for t in tickets:
                click.echo(t)
        elif choice == 4:
            ticket_id = click.prompt("Enter ticket ID", type=int)
            ticket = Ticket.find_by_id(ticket_id)
            click.echo(ticket if ticket else "Ticket not found.")
        else:
            click.echo("Invalid choice.")

def browse_events_by_genre():
    genre = click.prompt("Enter genre", type=click.Choice(GENRES))
    events = Event.find_by_genre(genre)
    if events:
        for event in events:
            click.echo(event)
    else:
        click.echo(f"No events found for genre {genre}.")

def view_artists_for_event():
    event_id = click.prompt("Enter event ID", type=int)
    event = Event.find_by_id(event_id)
    if event:
        artists = event.artists
        if artists:
            for artist in artists:
                click.echo(artist)
        else:
            click.echo("No artists found for this event.")
    else:
        click.echo("Event not found.")

def view_customer_tickets():
    customer_id = click.prompt("Enter customer ID", type=int)
    tickets = Ticket.find_by_customer(customer_id)
    if tickets:
        for ticket in tickets:
            click.echo(ticket)
    else:
        click.echo("No tickets found for this customer.")

if __name__ == '__main__':
    cli()