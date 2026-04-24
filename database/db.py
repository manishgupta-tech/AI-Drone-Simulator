import psycopg2
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="drone_sim",      # change if needed
            user="postgres",
            password="2622",   # put your password
            host="localhost",
            port="5432"
        )
        self.cursor = self.conn.cursor()

    def insert_telemetry(self, position, velocity):
        self.cursor.execute("""
            INSERT INTO flight_logs
            (timestamp, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            datetime.now(),
            position.x_val,
            position.y_val,
            position.z_val,
            velocity.x_val,
            velocity.y_val,
            velocity.z_val
        ))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()