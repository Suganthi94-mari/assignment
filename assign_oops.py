##############Installing require package ##############
import json


####### Creating Employee class################################

class Employee:

    """Create the class for adding ,displaying employee details
    for user """
    def _init_(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}\nID: {self.emp_id}\nTitle: {self.title}\nDepartment: {self.department}")

    def _str_(self):
        return f"{self.name} (ID: {self.emp_id})"

employee1 = Employee("suganthi", 1001, "Software Engineer", "Engineering")
employee1.display_details()
print(str(employee1))

############################# Department class ####################

class Department:

    """Create the class for adding ,removing,displyinmg departments
    for user """
    def _init_(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return
        print("Employee not found in this department.")

    def list_employees(self):
        print(f"Employees in {self.name}:")
        for employee in self.employees:
            print(employee)

    def _str_(self):
        return f"Department: {self.name}"

department = Department("Engineering")

emp_1 = Employee("Parthee", 1001, "Software Engineer", "Engineering")
emp_2 = Employee("John", 1002, "Manager", "Engineering")

department.add_employee(emp_1)
department.add_employee(emp_2)

department.list_employees()

department.remove_employee(emp_1)

department.list_employees()


########################### Company Details#############################
class Company:
    """Create the class for adding ,removing,displyinmg departments
    for user """
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"{department_name} department added successfully.")
        else:
            print(f"{department_name} department already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"{department_name} department removed successfully.")
        else:
            print(f"{department_name} department does not exist.")

    def display_departments(self):

        print("Departments in the company:")
        for department_name, department_obj in self.departments.items():
            print(department_name)



company = Company()

company.add_department("Engineering")
company.add_department("HR")

company.display_departments()

company.remove_department("Finance")

company.display_departments()


####################Functions for employee managements system#######################
def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. Exit")


def add_employee(company):
    """Create the function for adding employee
    for user"""
    department_name = input("Enter department name: ")
    if department_name in company.departments:
        name = input("Enter employee name: ")
        employee_id = input("Enter employee ID: ")
        title = input("Enter employee title: ")
        department = company.departments[department_name]
        employee = Employee(name, employee_id, title, department_name)
        department.add_employee(employee)
        print("Employee added successfully.")
    else:
        print("Department does not exist.")


def remove_employee(company):
    """Create the function for removing employee
    for user"""
    department_name = input("Enter department name: ")
    if department_name in company.departments:
        department = company.departments[department_name]
        employee_name = input("Enter employee name to remove: ")
        for employee in department.employees:
            if employee.name == employee_name:
                department.remove_employee(employee)
                return
        print(f"{employee_name} not found in {department_name}")
    else:
        print("Department does not exist.")


def display_department(company):
    """Create the function for showing departments
    for user"""
    department_name = input("Enter department name: ")
    if department_name in company.departments:
        company.departments[department_name].list_employees()
    else:
        print("Department does not exist.")


def add_department(company):
    """Create the function for adding departments
    for user"""
    department_name = input("Enter new department name: ")
    company.add_department(department_name)


def remove_department(company):
    """Create the function for removing departments
    from company data"""
    department_name = input("Enter department name to remove: ")
    company.remove_department(department_name)

############################saving company data into a json file ##################
def save_company_data(company):
    """Create the function for dumb data into json file"""
    with open("company_data.json", "w") as file:
        json.dump(company.departments, file, default=lambda x: x.__dict__)

def load_company_data():
    """Create the function for load data into json file"""
    try:
        with open("company_data.json", "r") as file:
            data = json.load(file)
            departments = {}
            for department_name, employees in data.items():
                department = Department(department_name)
                department.employees = [Employee(**employee) for employee in employees]
                departments[department_name] = department
            return departments
    except FileNotFoundError:
        return {}
def employee_management_system():

    """Create main function """
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(company)
        elif choice == "2":
            remove_employee(company)
        elif choice == "3":
            display_department(company)
        elif choice == "4":
            add_department(company)
        elif choice == "5":
            remove_department(company)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")



employee_management_system()

