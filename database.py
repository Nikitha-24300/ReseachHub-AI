import sqlite3

def init_db():
    conn = sqlite3.connect("researchhub.db")
    c = conn.cursor()

    # Documents table
    c.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        content TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_document(name, content, date):
    conn = sqlite3.connect("researchhub.db")
    c = conn.cursor()

    c.execute("""
    INSERT OR REPLACE INTO documents (name, content, date)
    VALUES (?, ?, ?)
    """, (name, content, date))

    conn.commit()
    conn.close()


def load_documents():
    conn = sqlite3.connect("researchhub.db")
    c = conn.cursor()

    c.execute("SELECT name, content, date FROM documents")
    rows = c.fetchall()

    conn.close()

    documents = {}
    for row in rows:
        documents[row[0]] = {
            "content": row[1],
            "date": row[2]
        }

    return documents
