from flask import Flask, jsonify, request
import json
import sqlite3


app = Flask(__name__)


@app.route('/getbf', methods=['GET'])
def get_bfitems():
    results = []
    stmt = "SELECT * FROM breakfast_items"
    c.execute(stmt)
    rows = c.fetchall()
    for row in rows:
        results.append({'id':row[0],'item':row[1], 'weight':row[2]})
    return jsonify({"breakfast_items": results})

@app.route('/getlunch', methods=['GET'])
def get_lunchitems():
    results = []
    stmt = "SELECT * FROM lunch_items"
    c.execute(stmt)
    rows = c.fetchall()
    for row in rows:
        results.append({'id':row[0],'item':row[1], 'weight':row[2]})
    return jsonify({"lunch_items": results})


@app.route('/getdinner', methods=['GET'])
def get_dinneritems():
    results = []
    stmt = "SELECT * FROM dinner_items"
    c.execute(stmt)
    rows = c.fetchall()
    for row in rows:
        results.append({'id':row[0],'item':row[1], 'weight':row[2]})
    return jsonify({"dinner_items": results})


@app.route('/postbreakfast', methods=['POST'])
def add_item():
    info = []
    data = request.get_json()
    print(data)
    for entry in data:
        info.clear()
        info.append(entry['item'])
        info.append(entry['weight'])

        stmt = "INSERT INTO breakfast_items (breakfast_item, breakfast_weight) VALUES(?,?)"
        c.execute(stmt,info)

    connection.commit()
    #connection.close()
    return "successful"


@app.route('/postlunch', methods = ['POST'])
def add_lunchitem():
    info = []
    data = request.get_json()
    print(data)
    for entry in data:
        info.clear()
        info.append(entry['item'])
        info.append(entry['weight'])

        stmt = "INSERT INTO lunch_items (lunch_item, lunch_weight) VALUES(?,?)"
        c.execute(stmt,info)

    connection.commit()

    return "successful"


@app.route('/postdinner', methods = ['POST'])
def add_dinneritem():
    info = []
    data = request.get_json()
    print(data)
    for entry in data:
        info.clear()
        info.append(entry['item'])
        info.append(entry['weight'])

        stmt = "INSERT INTO dinner_items (dinner_item, dinner_weight) VALUES(?,?)"
        c.execute(stmt,info)

    connection.commit()
    #connection.close()
    return "successful"


if __name__=="__main__":
    connection = sqlite3.connect('menu.db', check_same_thread=False)
    c = connection.cursor()
    app.run(debug=True)
    connection.close()
