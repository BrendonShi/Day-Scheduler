import psycopg2


def get_db_connection():
    try:
        conn = psycopg2.connect(
            database="mydatabase1",
            user="postgres",
            password="1234",
            host="127.0.0.1",
            port="5432",
        )
        print("Successfully connected")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting: {e}")
        return None

def init_db():
    conn = get_db_connection()
    if conn is None:
        print("Couldn't initialize db because connection failed.")
        return

    try:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                color TEXT NOT NULL
            );
            """)
            conn.commit()
            print("Successfull")
    except psycopg2.Error as e:
        print(f"Error initializing table: {e}")
    finally:
        if conn:
            conn.close()