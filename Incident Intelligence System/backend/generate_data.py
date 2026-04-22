import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import psycopg2

fake = Faker()

incident_types = ["Fire", "Medical", "Network", "Security", "System Failure"]
locations = ["Hyderabad", "Bangalore", "Chennai", "Mumbai", "Delhi"]
severities = ["low", "medium", "high"]
statuses = ["open", "closed"]
sources = ["sensor_A", "sensor_B", "mobile_app", "web_portal"]

def generate_data(n=100):
    data = []

    for _ in range(n):
        event_id = f"EVT{random.randint(1000, 1100)}"  # duplicates possible
        timestamp = fake.date_time_between(start_date="-10d", end_date="now")
        location = random.choice(locations)
        incident_type = random.choice(incident_types)
        severity = random.choice(severities)
        status = random.choice(statuses)
        response_time = random.randint(1, 120)
        source = random.choice(sources)

        data.append([
            event_id, timestamp, location, incident_type,
            severity, status, response_time, source
        ])

    df = pd.DataFrame(data, columns=[
        "event_id", "timestamp", "location", "incident_type",
        "severity", "status", "response_time", "source"
    ])

    return df

if __name__ == "__main__":
    df = generate_data(200)
    print(df.head())


def insert_into_db(df):
    conn = psycopg2.connect(
        dbname="incident_project",
        user="postgres",
        password="track@123",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO incidents_raw
            (event_id, timestamp, location, incident_type, severity, status, response_time, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    df = generate_data(200)
    insert_into_db(df)
    print("Data inserted successfully!")