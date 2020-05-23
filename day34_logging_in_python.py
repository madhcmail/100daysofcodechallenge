import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname=lname

        logging.info(f"Create Employee: {self.fullname} and her email is {self.email}")
    @property
    def email(self):
        return f"{self.fname}_{self.lname}@testmail.com"

    @property
    def fullname(self):
        return f"{self.fname.title()}{self.lname.title()}"


emp_1 = Employee("john", "river")
emp_2 = Employee("mark","jackson")
emp_3 = Employee('smith', 'jain')
