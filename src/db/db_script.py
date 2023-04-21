import sqlite3

conn = sqlite3.connect('../app.db')
cursor = conn.cursor()

with sqlite3.connect('../app.db') as db:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS admin(
            id INTEGER PRIMARY KEY,
            login TEXT,
            password TEXT)
        """
    )
    conn.commit()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS urlLink(
            id INTEGER PRIMARY KEY,
            link TEXT)
        """
    )
    cursor.execute(
        """
        INSERT INTO admin VALUES(0, 'admin', 'pass')
        """
    )
    conn.commit()
