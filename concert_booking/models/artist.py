from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from concert_booking.database import Base, Session

event_artists = Base.metadata.tables.get('event_artists', None)

class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    events = association_proxy('event_artists', 'event')

    def __repr__(self):
        return f"<Artist(name='{self.name}', genre='{self.genre}')>"

    @classmethod
    def create(cls, name, genre):
        session = Session()
        try:
            artist = cls(name=name, genre=genre)
            session.add(artist)
            session.commit()
            return artist
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, artist_id):
        session = Session()
        try:
            artist = session.query(cls).get(artist_id)
            if artist:
                session.delete(artist)
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
    def find_by_id(cls, artist_id):
        session = Session()
        try:
            return session.query(cls).get(artist_id)
        finally:
            session.close()