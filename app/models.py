from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    users = relationship("UserCity", back_populates="city")
    cars = relationship("Car", back_populates="city")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    cities = relationship("UserCity", back_populates="user")
    cars = relationship("Car", back_populates="user")


class UserCity(Base):
    __tablename__ = "user_cities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))

    user = relationship("User", back_populates="cities")
    city = relationship("City", back_populates="users")


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))

    user = relationship("User", back_populates="cars")
    city = relationship("City", back_populates="cars")
