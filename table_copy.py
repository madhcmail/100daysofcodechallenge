import sqlite3

connection = sqlite3.connect('addressbook.db')
c = connection.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS New_details
(name TEXT,address TEXT, phone_number INT, location TEXT, zipcode INT)
""")

# Copy data from one table to another
c.execute("""INSERT INTO New_details(name,address,phone_number,location)
SELECT name, address, phone_number, location FROM Details""")

connection.commit()  # if you want to commit the changes you did above, then this stmt is must!!
connection.close()