import sqlite3

conn = sqlite3.connect('finalproject.db')

c = conn.cursor()

c.execute('drop table if exists dogs')
c.execute('drop table if exists pictures')

c.execute('''CREATE TABLE dogs
             (
             	name text, 
             	dateofbirth date,
             	icon_filename text
             )
             ''')

c.execute("INSERT INTO dogs VALUES ('nugget','12/1/2011','IMG_1693.png')")
c.execute("INSERT INTO dogs VALUES ('dixie','2/15/2022','IMG_1692.png')")
c.execute("INSERT INTO dogs VALUES ('rocco','2/9/2023','baddog_icon.jpg')")

c.execute('''CREATE TABLE pictures
             (dog text,
              descr text,
              filename text
             )''')

c.execute("INSERT INTO pictures VALUES ('nugget','nuggets birthday','nugget1.jpg')")
c.execute("INSERT INTO pictures VALUES ('nugget','nuggets with grandma','nugget2.jpg')")
#c.execute("INSERT INTO pictures VALUES ('nugget','nugget','IMG_1693.png')")
c.execute("INSERT INTO pictures VALUES ('dixie','dixie being fresh','IMG_1692.PNG')")


conn.commit()

conn.close()

