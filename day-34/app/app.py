import os
import time
from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host='redis-cache', port=6379, decode_responses=True)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    
    # Connect to PostgreSQL
    try:
        conn = psycopg2.connect(
            host="postgres-db",
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        db_status = f"Connected successfully! Version: {db_version}"
    except Exception as e:
        db_status = f"Failed to connect. Error: {e}"

    return f"""
    <h1>Hello World!</h1>
    <p>Page views: {count}</p>
    <p><strong>Database Status:</strong> {db_status}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
