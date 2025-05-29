# 🎵 Concert Booking System

A comprehensive command-line application for managing concert bookings with full CRUD (Create, Read, Update, Delete) operations. Built with Python and SQLite.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [CRUD Operations](#crud-operations)
- [Requirements](#requirements)
- [Contributing](#contributing)

## ✨ Features

- **Artist Management**: Add, view, update, and delete artists
- **Customer Management**: Manage customer information including names and emails
- **Event Management**: Create and manage concert events with dates and assigned artists
- **Ticket Booking**: Book tickets for customers and manage reservations
- **Full CRUD Operations**: Complete Create, Read, Update, Delete functionality for all entities
- **Data Integrity**: Cascading deletes to maintain database consistency
- **User-friendly CLI**: Intuitive command-line interface with clear navigation
- **Input Validation**: Comprehensive validation for all user inputs
- **SQLite Database**: Lightweight, serverless database solution

## 📁 Project Structure

```
concert-booking-system/
├── cli.py                          # Main application entry point
├── concert_booking.db             # SQLite database (auto-generated)
├── lib/
│   └── project/
│       ├── __init__.py           # Package initialization
│       ├── artist.py             # Artist model and operations
│       ├── customer.py           # Customer model and operations
│       ├── event.py              # Event model and operations
│       └── ticket.py             # Ticket model and operations
└── README.md                     # This file
```

## 🚀 Installation

1. **Clone or download the project**:
   ```bash
   git clone <repository-url>
   cd concert-booking-system
   ```

2. **Ensure Python 3.6+ is installed**:
   ```bash
   python --version
   ```

3. **No additional dependencies required** - uses only Python standard library

## 💻 Usage

### Starting the Application

```bash
python cli.py
```

### Main Menu

The application presents a comprehensive menu organized by CRUD operations:

```
==================================================
CONCERT BOOKING SYSTEM - FULL CRUD
==================================================

📝 CREATE:
1. Add Artist
2. Add Customer
3. Add Event
4. Book Ticket

👀 READ:
5. View All Artists
6. View All Customers
7. View All Events
8. View All Tickets
9. View Customer Tickets

✏️  UPDATE:
10. Update Artist
11. Update Customer
12. Update Event

🗑️  DELETE:
13. Delete Artist
14. Delete Customer
15. Delete Event
16. Delete Ticket

17. Exit
==================================================
```

### Example Workflow

1. **Add Artists**:
   ```
   Enter choice: 1
   Enter artist name: Taylor Swift
   ✅ Artist 'Taylor Swift' added successfully.
   ```

2. **Add Customers**:
   ```
   Enter choice: 2
   Enter customer name: John Doe
   Enter customer email: john@example.com
   ✅ Customer 'John Doe' added successfully.
   ```

3. **Create Events**:
   ```
   Enter choice: 3
   Available artists:
     Artist 1: Taylor Swift
   Enter artist ID: 1
   Enter event name: Eras Tour - London
   Enter event date (YYYY-MM-DD): 2024-07-15
   ✅ Event 'Eras Tour - London' added successfully.
   ```

4. **Book Tickets**:
   ```
   Enter choice: 4
   Available customers:
     Customer 1: John Doe (john@example.com)
   Enter customer ID: 1
   Available events:
     Event 1: Eras Tour - London on 2024-07-15 by Taylor Swift
   Enter event ID: 1
   ✅ Ticket booked successfully.
   ```

## 🗄️ Database Schema

The application uses SQLite with the following schema:

### Artists Table
```sql
CREATE TABLE artists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

### Customers Table
```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);
```

### Events Table
```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artists(id)
);
```

### Tickets Table
```sql
CREATE TABLE tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    event_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (event_id) REFERENCES events(id)
);
```

## 🔄 CRUD Operations

### Create Operations
- ➕ **Add Artist**: Create new artists in the system
- ➕ **Add Customer**: Register new customers with email
- ➕ **Add Event**: Schedule concerts with specific dates and artists
- ➕ **Book Ticket**: Create ticket reservations for customers

### Read Operations
- 👁️ **View All Artists**: List all registered artists
- 👁️ **View All Customers**: Display all customer information
- 👁️ **View All Events**: Show all scheduled events with details
- 👁️ **View All Tickets**: List all booked tickets
- 👁️ **View Customer Tickets**: Show tickets for specific customers

### Update Operations
- ✏️ **Update Artist**: Modify artist name
- ✏️ **Update Customer**: Change customer name and/or email
- ✏️ **Update Event**: Modify event name, date, or assigned artist

### Delete Operations
- 🗑️ **Delete Artist**: Remove artist (cascades to delete their events)
- 🗑️ **Delete Customer**: Remove customer (cascades to delete their tickets)
- 🗑️ **Delete Event**: Remove event (cascades to delete associated tickets)
- 🗑️ **Delete Ticket**: Cancel individual ticket bookings

## 🔒 Data Integrity Features

- **Cascading Deletes**: Automatically maintains referential integrity
  - Deleting an artist removes all their events
  - Deleting a customer removes all their tickets
  - Deleting an event removes all associated tickets

- **Input Validation**:
  - Required field validation
  - Date format validation (YYYY-MM-DD)
  - ID existence validation
  - Email format requirements

- **Confirmation Prompts**: All delete operations require user confirmation

## 📋 Requirements

- **Python 3.6+**
- **SQLite3** (included with Python standard library)
- **Operating System**: Windows, macOS, or Linux

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📝 Code Examples

### Adding a New Model Method

```python
# Example: Adding a method to find events by date
@classmethod
def find_by_date(cls, date):
    conn = sqlite3.connect('concert_booking.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, date, artist_id FROM events WHERE date = ?', (date,))
    events = [cls(name=row[1], date=row[2], artist_id=row[3], id=row[0]) for row in cursor.fetchall()]
    conn.close()
    return events
```

### Extending the CLI

```python
# Example: Adding a new menu option
elif choice == '18':
    date = input("Enter date (YYYY-MM-DD): ").strip()
    events = Event.find_by_date(date)
    if events:
        print(f"Events on {date}:")
        for event in events:
            print(f"  {event}")
    else:
        print(f"No events found on {date}")
```

## 🐛 Troubleshooting

### Common Issues:

1. **"No such table" errors**: Delete `concert_booking.db` and restart the application
2. **Permission errors**: Ensure write permissions in the application directory
3. **Import errors**: Verify the `lib/` directory structure is correct

### Database Reset:

```bash
# Remove the database file to start fresh
rm concert_booking.db
python cli.py  # Will recreate the database
```

## 📊 Statistics

- **4 Main Entities**: Artists, Customers, Events, Tickets
- **17 Menu Options**: Complete CRUD coverage
- **4 Database Tables**: Properly normalized schema
- **Referential Integrity**: Foreign key constraints maintained

---

**Built with ❤️ using Python and SQLite**

*For support or questions, please open an issue in the repository.*