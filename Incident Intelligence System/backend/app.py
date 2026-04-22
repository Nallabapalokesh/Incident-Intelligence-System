from fastapi import FastAPI
import psycopg2
import pandas as pd
import subprocess
import requests

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        dbname="incident_project",
        user="postgres",
        password="Password",
        host="localhost",
        port="5432"
    )

def get_access_token():
    tenant_id = "Tenant_id"
    client_id = "Client_id"
    client_secret = "Client_Secret"

    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": "https://analysis.windows.net/powerbi/api/.default"
    }

    response = requests.post(url, data=data)
    token = response.json().get("access_token")

    return token

def trigger_powerbi_refresh():
    workspace_id = "Workspace_id"
    dataset_id = "Dataset_id"

    access_token = get_access_token()

    url = f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/refreshes"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)

    return response.status_code, response.text

@app.get("/")
def home():
    return {"message": "Incident Intelligence API is running"}

@app.get("/generate-data")
def generate_data_api():
    subprocess.run(["python", "generate_data.py"])
    return {"status": "Data generated successfully"}


@app.get("/incidents")
def get_incidents():
    conn = get_connection()
    query = "SELECT * FROM incidents_processed"
    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_dict(orient="records")

@app.get("/critical")
def get_critical():
    conn = get_connection()
    query = """
        SELECT * FROM incidents_processed
        WHERE priority_flag = 'Critical'
    """
    df = pd.read_sql(query, conn)
    conn.close()

    return df.to_dict(orient="records")

@app.get("/run-processing")
def run_processing():
    subprocess.run(["python", "process_data.py"])
    return {"status": "Processing completed"}

@app.get("/refresh-powerbi")
def refresh_powerbi():
    status, msg = trigger_powerbi_refresh()
    return {
        "status": "Power BI refresh triggered",
        "powerbi_status": status,
        "details": msg
    }

@app.delete("/delete-processed")
def delete_processed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE incidents_processed")

    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "Processed table cleared"}