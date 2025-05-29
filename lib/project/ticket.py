### ticket.py
import sqlite3
from project.customer import Customer
from project.event import Event

class Ticket:
    def __init__(self, customer_id, event_id, id=None):
        self.id = id
        self.customer_id = customer_id
        self.event_id = event_id

    def save(self):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO tickets (customer_id, event_id) VALUES (?, ?)', (self.customer_id, self.event_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE tickets SET customer_id = ?, event_id = ? WHERE id = ?', (self.customer_id, self.event_id, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, customer_id, event_id FROM tickets')
        tickets = [cls(customer_id=row[1], event_id=row[2], id=row[0]) for row in cursor.fetchall()]
        conn.close()
        return tickets

    @classmethod
    def find_by_customer(cls, customer_id):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, customer_id, event_id FROM tickets WHERE customer_id = ?', (customer_id,))
        tickets = [cls(customer_id=row[1], event_id=row[2], id=row[0]) for row in cursor.fetchall()]
        conn.close()
        return tickets

    def get_customer(self):
        return Customer.find_by_id(self.customer_id)

    def get_event(self):
        return Event.find_by_id(self.event_id)

    def __str__(self):
        customer = self.get_customer()
        event = self.get_event()
        return f"Ticket {self.id}: {customer.name} for {event.name}"