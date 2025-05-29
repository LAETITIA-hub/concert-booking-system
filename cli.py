import sys
import os
import sqlite3
from datetime import datetime


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
        print("\n" + "="*50)
        print("CONCERT BOOKING SYSTEM - FULL CRUD")
        print("="*50)
        
        # CREATE operations
        print("\n📝 CREATE:")
        print("1. Add Artist")
        print("2. Add Customer")
        print("3. Add Event")
        print("4. Book Ticket")
        
        # READ operations
        print("\n👀 READ:")
        print("5. View All Artists")
        print("6. View All Customers")
        print("7. View All Events")
        print("8. View All Tickets")
        print("9. View Customer Tickets")
        
        # UPDATE operations
        print("\n✏️  UPDATE:")
        print("10. Update Artist")
        print("11. Update Customer")
        print("12. Update Event")
        
        # DELETE operations
        print("\n🗑️  DELETE:")
        print("13. Delete Artist")
        print("14. Delete Customer")
        print("15. Delete Event")
        print("16. Delete Ticket")
        
        print("\n17. Exit")
        print("="*50)

        choice = input("Enter choice (1-17): ").strip()

        try:
            # CREATE OPERATIONS
            if choice == '1':
                name = input("Enter artist name: ").strip()
                if not name:
                    print("❌ Artist name cannot be empty.")
                    continue
                artist = Artist(name)
                artist.save()
                print(f"✅ Artist '{name}' added successfully.")

            elif choice == '2':
                name = input("Enter customer name: ").strip()
                if not name:
                    print("❌ Customer name cannot be empty.")
                    continue
                email = input("Enter customer email: ").strip()
                if not email:
                    print("❌ Email cannot be empty.")
                    continue
                customer = Customer(name, email)
                customer.save()
                print(f"✅ Customer '{name}' added successfully.")

            elif choice == '3':
                artists = Artist.get_all()
                if not artists:
                    print("❌ No artists available. Add an artist first.")
                    continue
                print("\nAvailable artists:")
                for artist in artists:
                    print(f"  {artist}")
                artist_id = int(input("Enter artist ID: "))
                if not Artist.find_by_id(artist_id):
                    print("❌ Invalid artist ID.")
                    continue
                name = input("Enter event name: ").strip()
                if not name:
                    print("❌ Event name cannot be empty.")
                    continue
                date = input("Enter event date (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(date, "%Y-%m-%d")
                except ValueError:
                    print("❌ Invalid date format. Use YYYY-MM-DD.")
                    continue
                event = Event(name, date, artist_id)
                event.save()
                print(f"✅ Event '{name}' added successfully.")

            elif choice == '4':
                customers = Customer.get_all()
                if not customers:
                    print("❌ No customers available. Add a customer first.")
                    continue
                print("\nAvailable customers:")
                for customer in customers:
                    print(f"  {customer}")
                customer_id = int(input("Enter customer ID: "))
                if not Customer.find_by_id(customer_id):
                    print("❌ Invalid customer ID.")
                    continue

                events = Event.get_all()
                if not events:
                    print("❌ No events available. Add an event first.")
                    continue
                print("\nAvailable events:")
                for event in events:
                    print(f"  {event}")
                event_id = int(input("Enter event ID: "))
                if not Event.find_by_id(event_id):
                    print("❌ Invalid event ID.")
                    continue

                ticket = Ticket(customer_id, event_id)
                ticket.save()
                print("✅ Ticket booked successfully.")

            
            elif choice == '5':
                artists = Artist.get_all()
                if not artists:
                    print("❌ No artists found.")
                else:
                    print(f"\n📋 All Artists ({len(artists)} found):")
                    for artist in artists:
                        print(f"  {artist}")

            elif choice == '6':
                customers = Customer.get_all()
                if not customers:
                    print("❌ No customers found.")
                else:
                    print(f"\n📋 All Customers ({len(customers)} found):")
                    for customer in customers:
                        print(f"  {customer}")

            elif choice == '7':
                events = Event.get_all()
                if not events:
                    print("❌ No events found.")
                else:
                    print(f"\n📋 All Events ({len(events)} found):")
                    for event in events:
                        print(f"  {event}")

            elif choice == '8':
                tickets = Ticket.get_all()
                if not tickets:
                    print("❌ No tickets found.")
                else:
                    print(f"\n📋 All Tickets ({len(tickets)} found):")
                    for ticket in tickets:
                        print(f"  {ticket}")

            elif choice == '9':
                customers = Customer.get_all()
                if not customers:
                    print("❌ No customers available.")
                    continue
                print("\nAvailable customers:")
                for customer in customers:
                    print(f"  {customer}")
                customer_id = int(input("Enter customer ID: "))
                if not Customer.find_by_id(customer_id):
                    print("❌ Invalid customer ID.")
                    continue
                tickets = Ticket.find_by_customer(customer_id)
                if not tickets:
                    print(f"❌ No tickets found for customer {customer_id}.")
                else:
                    print(f"\n🎫 Tickets for Customer {customer_id} ({len(tickets)} found):")
                    for ticket in tickets:
                        print(f"  {ticket}")

            # UPDATE OPERATIONS
            elif choice == '10':
                artists = Artist.get_all()
                if not artists:
                    print("❌ No artists available to update.")
                    continue
                print("\nAvailable artists:")
                for artist in artists:
                    print(f"  {artist}")
                artist_id = int(input("Enter artist ID to update: "))
                artist = Artist.find_by_id(artist_id)
                if not artist:
                    print("❌ Invalid artist ID.")
                    continue
                print(f"Current name: {artist.name}")
                new_name = input("Enter new artist name (or press Enter to keep current): ").strip()
                if new_name:
                    artist.name = new_name
                    artist.save()
                    print(f"✅ Artist updated successfully.")
                else:
                    print("ℹ️  No changes made.")

            elif choice == '11':
                customers = Customer.get_all()
                if not customers:
                    print("❌ No customers available to update.")
                    continue
                print("\nAvailable customers:")
                for customer in customers:
                    print(f"  {customer}")
                customer_id = int(input("Enter customer ID to update: "))
                customer = Customer.find_by_id(customer_id)
                if not customer:
                    print("❌ Invalid customer ID.")
                    continue
                print(f"Current name: {customer.name}")
                print(f"Current email: {customer.email}")
                new_name = input("Enter new customer name (or press Enter to keep current): ").strip()
                new_email = input("Enter new customer email (or press Enter to keep current): ").strip()
                if new_name:
                    customer.name = new_name
                if new_email:
                    customer.email = new_email
                if new_name or new_email:
                    customer.save()
                    print(f"✅ Customer updated successfully.")
                else:
                    print("ℹ️  No changes made.")

            elif choice == '12':
                events = Event.get_all()
                if not events:
                    print("❌ No events available to update.")
                    continue
                print("\nAvailable events:")
                for event in events:
                    print(f"  {event}")
                event_id = int(input("Enter event ID to update: "))
                event = Event.find_by_id(event_id)
                if not event:
                    print("❌ Invalid event ID.")
                    continue
                print(f"Current name: {event.name}")
                print(f"Current date: {event.date}")
                print(f"Current artist: {event.get_artist().name}")
                
                new_name = input("Enter new event name (or press Enter to keep current): ").strip()
                new_date = input("Enter new event date YYYY-MM-DD (or press Enter to keep current): ").strip()
                
                if new_date:
                    try:
                        datetime.strptime(new_date, "%Y-%m-%d")
                    except ValueError:
                        print("❌ Invalid date format. Update cancelled.")
                        continue
                
                print("\nAvailable artists:")
                artists = Artist.get_all()
                for artist in artists:
                    print(f"  {artist}")
                new_artist_input = input("Enter new artist ID (or press Enter to keep current): ").strip()
                new_artist_id = None
                if new_artist_input:
                    new_artist_id = int(new_artist_input)
                    if not Artist.find_by_id(new_artist_id):
                        print("❌ Invalid artist ID. Update cancelled.")
                        continue
                
                if new_name:
                    event.name = new_name
                if new_date:
                    event.date = new_date
                if new_artist_id:
                    event.artist_id = new_artist_id
                
                if new_name or new_date or new_artist_id:
                    event.save()
                    print(f"✅ Event updated successfully.")
                else:
                    print("ℹ️  No changes made.")

           
            elif choice == '13':
                artists = Artist.get_all()
                if not artists:
                    print("❌ No artists available to delete.")
                    continue
                print("\nAvailable artists:")
                for artist in artists:
                    print(f"  {artist}")
                artist_id = int(input("Enter artist ID to delete: "))
                artist = Artist.find_by_id(artist_id)
                if not artist:
                    print("❌ Invalid artist ID.")
                    continue
                confirm = input(f"Are you sure you want to delete '{artist.name}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    artist.delete()
                    print(f"✅ Artist '{artist.name}' deleted successfully.")
                else:
                    print("ℹ️  Deletion cancelled.")

            elif choice == '14':
                customers = Customer.get_all()
                if not customers:
                    print("❌ No customers available to delete.")
                    continue
                print("\nAvailable customers:")
                for customer in customers:
                    print(f"  {customer}")
                customer_id = int(input("Enter customer ID to delete: "))
                customer = Customer.find_by_id(customer_id)
                if not customer:
                    print("❌ Invalid customer ID.")
                    continue
                confirm = input(f"Are you sure you want to delete '{customer.name}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    customer.delete()
                    print(f"✅ Customer '{customer.name}' deleted successfully.")
                else:
                    print("ℹ️  Deletion cancelled.")

            elif choice == '15':
                events = Event.get_all()
                if not events:
                    print("❌ No events available to delete.")
                    continue
                print("\nAvailable events:")
                for event in events:
                    print(f"  {event}")
                event_id = int(input("Enter event ID to delete: "))
                event = Event.find_by_id(event_id)
                if not event:
                    print("❌ Invalid event ID.")
                    continue
                confirm = input(f"Are you sure you want to delete '{event.name}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    event.delete()
                    print(f"✅ Event '{event.name}' deleted successfully.")
                else:
                    print("ℹ️  Deletion cancelled.")

            elif choice == '16':
                tickets = Ticket.get_all()
                if not tickets:
                    print("❌ No tickets available to delete.")
                    continue
                print("\nAvailable tickets:")
                for ticket in tickets:
                    print(f"  {ticket}")
                ticket_id = int(input("Enter ticket ID to delete: "))
                ticket = Ticket.find_by_id(ticket_id)
                if not ticket:
                    print("❌ Invalid ticket ID.")
                    continue
                confirm = input(f"Are you sure you want to delete this ticket? (y/N): ").strip().lower()
                if confirm == 'y':
                    ticket.delete()
                    print(f"✅ Ticket deleted successfully.")
                else:
                    print("ℹ️  Deletion cancelled.")

            elif choice == '17':
                print("👋 Goodbye! Thanks for using the Concert Booking System.")
                break

            else:
                print("❌ Invalid choice. Please enter a number between 1-17.")

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
