import sqlite3

class Customer:
    def __init__(self, name, email, id=None):
        self.id = id
        self.name = name
        self.email = email

    def save(self):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', (self.name, self.email))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE customers SET name = ?, email = ? WHERE id = ?', (self.name, self.email, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        """Delete this customer from the database"""
        if self.id is None:
            raise ValueError("Cannot delete customer without ID")
        
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        
        # First delete all tickets associated with this customer
        cursor.execute('DELETE FROM tickets WHERE customer_id = ?', (self.id,))
        
        # Then delete the customer
        cursor.execute('DELETE FROM customers WHERE id = ?', (self.id,))
        
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM customers')
        customers = [cls(name=row[1], email=row[2], id=row[0]) for row in cursor.fetchall()]
        conn.close()
        return customers

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM customers WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row[1], email=row[2], id=row[0]) if row else None

    def __str__(self):
        return f"Customer {self.id}: {self.name} ({self.email})"