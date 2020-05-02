class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # set a default value for an attribute.

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car  {self.make} has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot Roll back an odometer for  {self.make}" )

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f" This car is a petrol car")


class Battery:

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 230
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size >=75:
            self.battery_size = 100


class ElectricCar(Car): #  Inheritance
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color
        self.battery = Battery()

    def get_color(self):
        print(f"My tesla color is {self.color}")

    def fill_gas_tank(self):  # overriding the method from a parent class
        print("This is a battery operated car!")


my_tesla = ElectricCar("Tesla","model s",2020, "red")
print(my_tesla.get_descriptive_name())
my_tesla.get_color()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

*********************************************************************************

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


class Privileges:
    def __init__(self, privileges=["can add post", "can delete post","can ban user"]):
        self.privileges= privileges

    def show_privileges(self):
        print(f"The list of privileges an admin have: {self.privileges}")


class Admin(User):  # Inheritance
    def __init__(self, first_name, last_name, age, job_title, location):
        super().__init__(first_name, last_name, age, job_title, location)
        self.privileges = Privileges()


new_admin_user = Admin("Madhuri","Charugundla",23,"Engineer","USA")
new_admin_user.describe_user()
new_admin_user.privileges.show_privileges()