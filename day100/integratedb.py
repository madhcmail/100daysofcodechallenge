import sqlite3

connection = sqlite3.connect('menu.db')
c = connection.cursor()


c.execute("""CREATE TABLE breakfast_items
(id INTEGER PRIMARY KEY AUTOINCREMENT, breakfast_item TEXT, breakfast_weight INT)
""")
c.execute("""CREATE TABLE lunch_items 
(id INTEGER PRIMARY KEY AUTOINCREMENT,lunch_item TEXT, lunch_weight INT)
""")
c.execute("""CREATE TABLE dinner_items 
(id INTEGER PRIMARY KEY AUTOINCREMENT,dinner_item TEXT, dinner_weight INT)
""")
connection.close()

