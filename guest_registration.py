import psycopg2
from faker import Faker
from random import randint
from datetime import datetime, timedelta

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="hotel", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

fake = Faker()

# Отримати існуючі guest_id і room_id
cursor.execute("SELECT guest_id FROM Guests")
guest_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT room_id FROM Rooms")
room_ids = [row[0] for row in cursor.fetchall()]

# Генерація реєстрації гостей
for _ in range(10):
    guest_id = fake.random_element(elements=guest_ids)
    room_id = fake.random_element(elements=room_ids)
    arrival_date = fake.date_this_year()
    stay_duration = randint(1, 10)
    
    cursor.execute(
        "INSERT INTO GuestRegistration (guest_id, arrival_date, stay_duration, room_id) VALUES (%s, %s, %s, %s)",
        (guest_id, arrival_date, stay_duration, room_id)
    )

conn.commit()
cursor.close()
conn.close()

print("GuestRegistration data inserted successfully!")