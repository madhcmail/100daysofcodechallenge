import csv, sqlite3

connection = sqlite3.connect('addressbook.db')
c = connection.cursor()

# open csv file and read the data with dict reader
with open('address_list.csv', 'r') as al:
    info = []
    data = csv.DictReader(al)

    # appending the data into a list of tuples
    for row in data:
        info.append((row['name'], row['address'], row['phone_number']))


stmt = "INSERT INTO Details VALUES(?,?,?)"
# inserting bulk records into the table
c.executemany(stmt, info)
connection.commit()  # commit the data
connection.close()  # close the connection
