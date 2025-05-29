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

 CRUD Operations
Create: Add artists, customers, events, and book tickets.
Read: View all artists, customers, events, tickets, or customer-specific tickets.
Update: Modify artist names, customer details, or event details.
Delete: Remove artists, customers, events, or tickets (with cascading deletes).

Installation
Clone the repository: git clone <repository-url>.
Ensure Python 3.6+ is installed: python --version.
No additional dependencies required.

Usage
Run: python cli.py.
Navigate via a menu with 17 options (e.g., add artist, book ticket, view events).
Example: Add an artist, create an event, book a ticket for a customer.

Requirements
Python 3.6+.
SQLite (included in Python standard library).
Compatible with Windows, macOS, Linux.

Contributing
Fork the repo, create a feature branch, commit changes, and submit a pull request.

Troubleshooting
Database Issues: Delete concert_booking.db and restart to reset.
Permissions: Ensure write access to the project directory.
Import Errors: Verify lib/ directory structure.