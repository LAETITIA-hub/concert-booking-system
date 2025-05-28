from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from concert_booking.database import Base, Session
from datetime import datetime

event_artists = Base.metadata.tables.get('event_artists', None)

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    genre = Column(String, nullable=False)
    tickets = relationship('Ticket', back_populates='event')
    artists = association_proxy('event_artists', 'artist')

    def __repr__(self):
        return f"<Event(name='{self.name}', date='{self.date}', genre='{self.genre}')>"

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Date must be a datetime object")
        self._date = value

    @classmethod
    def create(cls, name, date, genre):
        session = Session()
        try:
            event = cls(name=name, date=date, genre=genre)
            session.add(event)
            session.commit()
            return event
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, event_id):
        session = Session()
        try:
            event = session.query(cls).get(event_id)
            if event:
                session.delete(event)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            return session.query(cls).all()
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, event_id):
        session = Session()
        try:
            return session.query(cls).get(event_id)
        finally:
            session.close()

    @classmethod
    def find_by_genre(cls, genre):
        session = Session()
        try:
            return session.query(cls).filter_by(genre=genre).all()
        finally:
            session.close()