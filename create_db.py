import sqlite3

def create_db():
    # Connect to the database (or create if it doesn't exist)
    con = sqlite3.connect("srms.db")
    cur = con.cursor()

    # Create Course Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)

    # Create Student Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            course TEXT,
            adm_date TEXT,
            state TEXT,
            city TEXT,
            pin TEXT,
            address TEXT
        )
    """)

    # Create Result Table with total column
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks TEXT,
            full_marks TEXT,
            total INTEGER
        )
    """)

    # Commit changes and close connection
    con.commit()
    con.close()

# Call the function to create the database
if __name__ == "__main__":
    create_db()
    print("Database and tables created successfully.")
