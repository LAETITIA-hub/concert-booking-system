import sys
import os
import sqlite3
from datetime import datetime

# Add 'lib' directory to the Python path so 'project' can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from project.artist import Artist
from project.customer import Customer
from project.event import Event
from project.ticket import Ticket


def init_db():
    conn = sqlite3.connect('concert_booking.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS artists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        artist_id INTEGER,
        FOREIGN KEY (artist_id) REFERENCES artists(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        event_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (event_id) REFERENCES events(id)
    )''')

    conn.commit()
    conn.close()


def main():
    init_db()

    while True:
        print("\nConcert Booking System")
        print("1. Add Artist")
        print("2. Add Customer")
        print("3. Add Event")
        print("4. Book Ticket")
        print("5. View All Events")
        print("6. View Customer Tickets")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        try:
            if choice == '1':
                name = input("Enter artist name: ").strip()
                if not name:
                    print("Artist name cannot be empty.")
                    continue
                artist = Artist(name)
                artist.save()
                print(f"Artist '{name}' added.")

            elif choice == '2':
                name = input("Enter customer name: ").strip()
                if not name:
                    print("Customer name cannot be empty.")
                    continue
                email = input("Enter customer email: ").strip()
                if not email:
                    print("Email cannot be empty.")
                    continue
                customer = Customer(name, email)
                customer.save()
                print(f"Customer '{name}' added.")

            elif choice == '3':
                artists = Artist.get_all()
                if not artists:
                    print("No artists available. Add an artist first.")
                    continue
                print("Available artists:")
                for artist in artists:
                    print(artist)
                artist_id = int(input("Enter artist ID: "))
                if not Artist.find_by_id(artist_id):
                    print("Invalid artist ID.")
                    continue
                name = input("Enter event name: ").strip()
                if not name:
                    print("Event name cannot be empty.")
                    continue
                date = input("Enter event date (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Use YYYY-MM-DD.")
                    continue
                event = Event(name, date, artist_id)
                event.save()
                print(f"Event '{name}' added.")

            elif choice == '4':
                customers = Customer.get_all()
                if not customers:
                    print("No customers available. Add a customer first.")
                    continue
                print("Available customers:")
                for customer in customers:
                    print(customer)
                customer_id = int(input("Enter customer ID: "))
                if not Customer.find_by_id(customer_id):
                    print("Invalid customer ID.")
                    continue

                events = Event.get_all()
                if not events:
                    print("No events available. Add an event first.")
                    continue
                print("Available events:")
                for event in events:
                    print(event)
                event_id = int(input("Enter event ID: "))
                if not Event.find_by_id(event_id):
                    print("Invalid event ID.")
                    continue

                ticket = Ticket(customer_id, event_id)
                ticket.save()
                print("Ticket booked.")

            elif choice == '5':
                events = Event.get_all()
                if not events:
                    print("No events available.")
                    continue
                print("All Events:")
                for event in events:
                    print(event)

            elif choice == '6':
                customers = Customer.get_all()
                if not customers:
                    print("No customers available.")
                    continue
                print("Available customers:")
                for customer in customers:
                    print(customer)
                customer_id = int(input("Enter customer ID: "))
                if not Customer.find_by_id(customer_id):
                    print("Invalid customer ID.")
                    continue
                tickets = Ticket.find_by_customer(customer_id)
                if not tickets:
                    print(f"No tickets found for customer {customer_id}.")
                    continue
                print(f"Tickets for customer {customer_id}:")
                for ticket in tickets:
                    print(ticket)

            elif choice == '7':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()