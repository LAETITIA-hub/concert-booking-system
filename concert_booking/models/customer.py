from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from concert_booking.database import Base, Session

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    tickets = relationship('Ticket', back_populates='customer')

    def __repr__(self):
        return f"<Customer(name='{self.name}', email='{self.email}')>"

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @classmethod
    def create(cls, name, email):
        session = Session()
        try:
            customer = cls(name=name, email=email)
            session.add(customer)
            session.commit()
            return customer
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, customer_id):
        session = Session()
        try:
            customer = session.query(cls).get(customer_id)
            if customer:
                session.delete(customer)
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
    def find_by_id(cls, customer_id):
        session = Session()
        try:
            return session.query(cls).get(customer_id)
        finally:
            session.close()

    @classmethod
    def find_by_email(cls, email):
        session = Session()
        try:
            return session.query(cls).filter_by(email=email).first()
        finally:
            session.close()