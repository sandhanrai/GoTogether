import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Open a file to write the SQL dump
with open('dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

# Close the connection
conn.close()
print("Export completed successfully.")
