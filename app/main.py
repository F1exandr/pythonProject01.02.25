from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import faker
import random
from models import Base, City, User, UserCity, Car
from database import engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()
fake = faker.Faker()


@app.get("/cars/city/{city_id}")
def get_cars_by_city(city_id: int, db: Session = Depends(get_db)):
    cars = db.query(Car).filter(Car.city_id == city_id).all()
    if not cars:
        raise HTTPException(status_code=404, detail="Cars not found for this city")
    return cars



@app.post("/generate-data")
def generate_fake_data(db: Session = Depends(get_db)):
    # Создаем города
    cities = []
    for a in range(5):
        city = City(name=fake.city())
        db.add(city)
        cities.append(city)


users = []
    for b in range(10):
        user = User(
            name=fake.name(),
            email=fake.email()
        )
        db.add(user)
        users.append(user)


for user in users:
        for c in range(random.randint(1, 3)):  # У каждого пользователя 1-3 города
            city = random.choice(cities)
            user_city = UserCity(user=user, city=city)
            db.add(user_city)

car_models = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi"]
for x in range(20):
    user = random.choice(users)
    city = random.choice(cities)
    car = Car(
        model=random.choice(car_models),
        user=user,
        city=city
    )
    db.add(car)

db.commit()
return {"message": "Data generated successfully"}
