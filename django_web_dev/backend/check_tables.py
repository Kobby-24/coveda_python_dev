import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")

# Check if blog_post table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='blog_post'")
blog_table = cursor.fetchone()
if blog_table:
    print("\nblog_post table exists!")
    # Check table schema
    cursor.execute("PRAGMA table_info(blog_post)")
    columns = cursor.fetchall()
    print("Columns in blog_post table:")
    for col in columns:
        print(f"  - {col[1]} ({col[2]})")
else:
    print("\nblog_post table does NOT exist!")

conn.close()
