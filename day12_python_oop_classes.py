class Restaurant:
    """ Modelling a restaurant"""

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The Restaurant Name is: {self.restaurant_name}")
        print(f"The Restaurant offers {self.cuisine_type} cuisines.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open!")


hotel1 = Restaurant('Annapurna', 'Indian')
print(f"Hotel Name: {hotel1.restaurant_name}")
print(f"Cuisine the hotel {hotel1.restaurant_name} offers: {hotel1.cuisine_type}")
hotel1.describe_restaurant()
hotel1.open_restaurant()

hotel2 = Restaurant('Chipotle', 'Mexican')
hotel2.describe_restaurant()

hotel3 = Restaurant('B-Spot', 'Italian')
hotel3.describe_restaurant()

hotel4 = Restaurant('Sweet Mango', 'Thai')
hotel4.describe_restaurant()


class User:

    def __init__(self, first_name, last_name, age, job_title, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job_title = job_title
        self.location = location

    def describe_user(self):
        print(f"User Name: {self.first_name}{self.last_name}")
        print(f"User Age: {self.age}")
        print(f"User's Job title: {self.job_title}")
        print(f"User's location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}. Welcome to learn OOPS concept!")


user1 = User("Scott", "Ghar", 23, "Engineer", "Kansas")
user1.describe_user()
user1.greet_user()

user2 = User("Tiger","Shiroff",32,"Actor","India")
user2.describe_user()
user2.greet_user()

user3 = User("Robert","Gosh",55,"Designer","Seattle")
user3.describe_user()
user3.greet_user()


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set a default value for an attribute.

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        print(f"This car  {self.make} has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot Roll back an odometer for  {self.make}" )


my_new_car = Car("Honda", "Civic", 2013)
print(my_new_car.get_descriptive_name())


my_car2 = Car("audi", "a4", 2019)
my_car2.get_descriptive_name()
my_car2.update_odometer(32)
my_car2.read_odometer()



