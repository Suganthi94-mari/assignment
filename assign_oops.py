class Employee:
    def _init_(self, name, emp_id, title, department):
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}\nID: {self.emp_id}\nTitle: {self.title}\nDepartment: {self.department}")

    def _str_(self):
        return f"{self.name} (ID: {self.emp_id})"


class Department:
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


class Company:
    def _init_(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
        else:
            print("Department not found.")
