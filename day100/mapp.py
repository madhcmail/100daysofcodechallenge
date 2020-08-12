from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3, random

app = Flask(__name__)

connection = sqlite3.connect('menu.db')
c = connection.cursor()


def get_items(table_name):
    items = []
    weights = []

    items.clear()
    weights.clear()
    if table_name == "breakfast_items":
        stmt = "SELECT breakfast_item,breakfast_weight from breakfast_items"
    elif table_name == "lunch_items":
        stmt = "SELECT lunch_item,lunch_weight from lunch_items"
    elif table_name == 'dinner_items':
        stmt = "SELECT dinner_item,dinner_weight from dinner_items"

    c.execute(stmt)
    results = c.fetchall()

    for entry in results:
        items.append(entry[0])
        weights.append(entry[1])

    return items, weights


BREAKFAST_MENU, BREAKFAST_WEIGHTS = get_items("breakfast_items")
print(f"Items: {BREAKFAST_MENU}, Weights:{BREAKFAST_WEIGHTS}")

LUNCH_MENU, LUNCH_WEIGHTS = get_items("lunch_items")
print(f"Items: {LUNCH_MENU}, Weights:{LUNCH_WEIGHTS}")

DINNER_MENU, DINNER_WEIGHTS = get_items("dinner_items")
print(f"Items: {DINNER_MENU}, Weights:{DINNER_WEIGHTS}")

#BREAKFAST_MENU = ['Idly', 'Dosa', 'Utappam', 'Upma', 'Poha', 'Noodles', 'Cereal','Bread and Peanut Butter']
#BREAKFAST_WEIGHTS = [1,2,1,1,1,1,1,1]
#LUNCH_MENU = ['Rice-rasam-okra', 'Rice-Sambar-Tindoor','Chapathi-Panner','Chapathi-Channa','Vegetable Pulao','Tomoto Rice -Raita','Rice-PalakDal-Fry']
#LUNCH_WEIGHTS= [1,1,1,1,1,1,1]
#DINNER_MENU= ['Dosa','Upma','Chapathi-BesanChutney','Rice-Dal-Salad','Vegetable Salad','MushroomSoup-Salad','Rice-rasam-Curry']
#DINNER_WEIGHTS= [2,1,1,1,1,1,1]

DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']



menu = {}

@app.route('/')
@app.route('/home')
def index():
    for day in DAYS:
        menu[day] = {"Breakfast": random.choices(BREAKFAST_MENU, weights=BREAKFAST_WEIGHTS),
                     "Lunch": random.choices(LUNCH_MENU, weights=LUNCH_WEIGHTS),
                     "Dinner": random.choices(DINNER_MENU, weights=DINNER_WEIGHTS)}
    return render_template("menu.html", menu=menu)


if __name__ == "__main__":

    app.run(debug=True)