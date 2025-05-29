import sqlite3

class Artist:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def save(self):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO artists (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE artists SET name = ? WHERE id = ?', (self.name, self.id))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM artists')
        artists = [cls(name=row[1], id=row[0]) for row in cursor.fetchall()]
        conn.close()
        return artists

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('concert_booking.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name FROM artists WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row[1], id=row[0]) if row else None

    def __str__(self):
        return f"Artist {self.id}: {self.name}"