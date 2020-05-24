import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname=lname

        logger.info(f"Create Employee: {self.fullname} and her email is {self.email}")
    @property
    def email(self):
        return f"{self.fname}_{self.lname}@testmail.com"

    @property
    def fullname(self):
        return f"{self.fname.title()}{self.lname.title()}"


emp_1 = Employee("john", "river")
emp_2 = Employee("mark","jackson")
emp_3 = Employee('smith', 'jain')
