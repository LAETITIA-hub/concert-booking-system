import sqlite3
from project.artist import Artist

class Event:
    def __init__(self, name, date, artist_id, id=None):
        self.id = id
        self.name = name
        self.date = date
        self.artist_id = artist_id

    def save(self):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO events (name, date, artist_id) VALUES (?, ?, ?)', (self.name, self.date, self.artist_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE events SET name = ?, date = ?, artist_id = ? WHERE id = ?', (self.name, self.date, self.artist_id, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        """Delete this event from the database"""
        if self.id is None:
            raise ValueError("Cannot delete event without ID")
        
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        
        # First delete all tickets associated with this event
        cursor.execute('DELETE FROM tickets WHERE event_id = ?', (self.id,))
        
        # Then delete the event
        cursor.execute('DELETE FROM events WHERE id = ?', (self.id,))
        
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, date, artist_id FROM events')
        events = [cls(name=row[1], date=row[2], artist_id=row[3], id=row[0]) for row in cursor.fetchall()]
        conn.close()
        return events

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, date, artist_id FROM events WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row[1], date=row[2], artist_id=row[3], id=row[0]) if row else None

    def get_artist(self):
        return Artist.find_by_id(self.artist_id)

    def __str__(self):
        artist = self.get_artist()
        return f"Event {self.id}: {self.name} on {self.date} by {artist.name}"