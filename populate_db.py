import psycopg2
from faker import Faker

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="hotel", user="user", password="password", host="localhost", port="5432"
)
cursor = conn.cursor()

fake = Faker()

# Генерація даних гостей
for _ in range(7):
    cursor.execute(
        "INSERT INTO Guests (first_name, last_name, city) VALUES (%s, %s, %s)",
        (fake.first_name(), fake.last_name(), fake.city())
    )

# Генерація даних номерів
for _ in range(10):
    cursor.execute(
        "INSERT INTO Rooms (room_number, num_rooms, floor, tv, fridge, capacity, category, price_per_day) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (fake.random_int(min=100, max=999), fake.random_int(min=1, max=4), fake.random_int(min=1, max=3),
         fake.boolean(), fake.boolean(), fake.random_int(min=1, max=4),
         fake.random_element(elements=('standard', 'semi-lux', 'lux')),
         fake.random_number(digits=3))
    )

conn.commit()

# Закриття підключення
cursor.close()
conn.close()