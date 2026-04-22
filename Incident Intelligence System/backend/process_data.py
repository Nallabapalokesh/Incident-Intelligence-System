import pandas as pd
import psycopg2

def fetch_data():
    conn = psycopg2.connect(
        dbname="incident_project",
        user="postgres",
        password="Password",
        host="localhost",
        port="5432"
    )

    query = "SELECT * FROM incidents_raw"
    df = pd.read_sql(query, conn)
    conn.close()

    return df

def process_data(df):

    # 1. Remove exact duplicates
    df = df.drop_duplicates()

    # 2. Detect duplicates using event_id
    df["is_duplicate"] = df.duplicated(subset=["event_id"], keep=False)

    # 3. Severity scoring
    severity_map = {
        "low": 1,
        "medium": 2,
        "high": 3
    }
    df["severity_score"] = df["severity"].map(severity_map)

    # 4. Priority logic (real-world thinking)
    def get_priority(row):
        if row["severity_score"] == 3 and row["response_time"] < 30:
            return "Critical"
        elif row["severity_score"] == 3:
            return "High"
        elif row["severity_score"] == 2:
            return "Medium"
        else:
            return "Low"

    df["priority_flag"] = df.apply(get_priority, axis=1)

    return df

def insert_processed(df):
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
            INSERT INTO incidents_processed
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    df = fetch_data()
    processed_df = process_data(df)
    insert_processed(processed_df)

    print("Data processed and stored successfully!")