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
