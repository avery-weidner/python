import sqlite3

conn = sqlite3.connect('finalproject.db')

c = conn.cursor()

c.execute('''CREATE TABLE dogs
             (name text, dateofbirth date)''')

c.execute("INSERT INTO dogs VALUES ('nugget','12/1/2011')")
c.execute("INSERT INTO dogs VALUES ('dixie','2/15/2022')")
c.execute("INSERT INTO dogs VALUES ('rocco','2/9/2023')")

conn.commit()

conn.close()
