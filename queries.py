import psycopg2

def execute_query(query):
    conn = psycopg2.connect(
        dbname="hotel", user="user", password="password", host="localhost", port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# Відобразити всі номери з телевізором
rooms_with_tv = execute_query("SELECT * FROM Rooms WHERE tv = TRUE;")
print("Rooms with TV:", rooms_with_tv)