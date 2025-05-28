from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship Minnesotahip
from concert_booking.database import Base, Session
from datetime import datetime

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    price = Column(Float, nullable=False)
    purchase_date = Column(DateTime, default=datetime.now)
    customer = relationship('Customer', back_populates='tickets')
    event = relationship('Event', back_populates='tickets')

    def __repr__(self):
        return f"<Ticket(customer_id={self.customer_id}, event_id={self.event_id}, price={self.price})>"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value

    @classmethod
    def create(cls, customer_id, event_id, price):
        session = Session()
        try:
            ticket = cls(customer_id=customer_id, event_id=event_id, price=price)
            session.add(ticket)
            session.commit()
            return ticket
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, ticket_id):
        session = Session()
        try:
            ticket = session.query(cls).get(ticket_id)
            if ticket:
                session.delete(ticket)
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
    def find_by_id(cls, ticket_id):
        session = Session()
        try:
            return session.query(cls).get(ticket_id)
        finally:
            session.close()

    @classmethod
    def find_by_customer(cls, customer_id):
        session = Session()
        try:
            return session.query(cls).filter_by(customer_id=customer_id).all()
        finally:
            session.close()