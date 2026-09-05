import sqlite3

DATABASE = "erp.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():

    conn = get_db()
    cursor = conn.cursor()

    # STUDENTS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # TEST STUDENT ACCOUNT
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-001", "student123"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-002", "student873"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-003", "student738"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-004", "student876"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-005", "dgdvdfr"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-006", "hrthtr"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-007", "rtyhrg"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-008", "grtt8eryhr"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
    """, ("2026-CS-009", "rgegtrh"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-010", "975574"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-011", "rghe"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-012", "reg"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-013", "gtfjnf"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-014", "hfjhdge"))
    cursor.execute("""
        INSERT OR IGNORE INTO students (student_id, password)
        VALUES (?, ?)
    """, ("2026-CS-015", "o6g5677"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-016", "ug879"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-017", "dc8677"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-018", "o6dyhjv7"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-019", "j77577"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-020", "09886bvb"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-021", "vgf66"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-022", "7tw5c7"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-023", "ihiv77"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-024", "g67c576"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-025", "875632"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-26", "7tytv76v7"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-027", "but777"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-028", "8g776xcu"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-029", "g66xq"))
    cursor.execute("""
            INSERT OR IGNORE INTO students (student_id, password)
            VALUES (?, ?)
        """, ("2026-CS-030", "89v670"))
    


    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database ready!")