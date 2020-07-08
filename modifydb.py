import sqlite3


# To delete the data from the table
def data_delete():

    stmt = "DELETE FROM Details"
    c.execute(stmt)


# Adding a new column to the table
def data_modify():

    stmt = "ALTER TABLE Details ADD location"
    c.execute(stmt)


# update a specific record that satisfies the WHERE condition
def update_data(col_name, cond_col, column_values):

    stmt = f"UPDATE Details SET {col_name} = ? WHERE {cond_col} = ?"
    c.execute(stmt, column_values)
    print("Updated the column")


if __name__ == '__main__':
    connection = sqlite3.connect('addressbook.db')
    c = connection.cursor()

    update_data('name', 'name', ('winne', 'cookie'))

    connection.commit()
    connection.close()