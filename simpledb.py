import sqlite3

# connecting to the database addressbook if exists. If not, it will create dteh db automatically
connection = sqlite3.connect('addressbook.db')

# creating a cursor object to parse the database. Using this cursor, we can execute all the sql commands
c = connection.cursor()

# here we execute all sql commands
c.execute("""CREATE TABLE Details
(name TEXT, address TEXT, phone_number INT)
""")
connection.close()