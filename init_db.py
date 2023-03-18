import sqlite3

conn = sqlite3.connect('url.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        short_url TEXT
    )
''')
conn.commit()
conn.close()
