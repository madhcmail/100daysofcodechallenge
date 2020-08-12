import random

BREAKFAST_MENU = ['Idly', 'Dosa', 'Utappam', 'Upma', 'Poha', 'Noodles', 'Cereal','Bread and Peanut Butter']
BREAKFAST_WEIGHTS = [2,2,1,1,1,1,1,1]
LUNCH_MENU = ['Rice-rasam-okra', 'Rice-Sambar-Tindoor','Chapathi-Panner','Chapathi-Channa','Vegetable Pulao','Tomoto Rice -Raita','Rice-PalakDal-Fry']
LUNCH_WEIGHTS= [1,2,1,1,1,1,1]
DINNER_MENU= ['Dosa','UPMA','Chapathi-BesanChutney','Rice-Dal-Salad','Vegetable Salad','MushroomSoup-Salad','Rice-rasam-Curry']
DINNER_WEIGHTS= [2,1,1,1,1,1,1]
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

menu = {}

for day in DAYS:
    menu[day] = {"Breakfast" : random.sample(BREAKFAST_MENU, weights=BREAKFAST_WEIGHTS), "Lunch":random.choices(LUNCH_MENU,weights=LUNCH_WEIGHTS),
                 "Dinner":random.choices(DINNER_MENU, weights=DINNER_WEIGHTS)}

print(menu)
