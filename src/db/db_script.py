import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

with sqlite3.connect('app.db') as db:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            login TEXT,
            password TEXT)
        """
    )
    conn.commit()
    # cursor.execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS urlLink(
    #         id INTEGER PRIMARY KEY,
    #         link TEXT)
    #     """
    # )
    cursor.execute(
        """
        INSERT INTO user VALUES(0, 'comm', 'sha256$eGb3ZQuFf7Ozz4fL$4a52e782d0e3e3c0aa34d66536385b4d071c8ea44743a68acef520132d326e9f')
        """
    )
    conn.commit()

    cursor.execute(
        """
        INSERT INTO user VALUES(1, 'admin', 'sha256$eGb3ZQuFf7Ozz4fL$4a52e782d0e3e3c0aa34d66536385b4d071c8ea44743a68acef520132d326e9f')
        """
    )
    conn.commit()
