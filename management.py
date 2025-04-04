import json
import csv

# Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


# Employee class (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = float(salary)

    def get_details(self):
        # Override the method to include employee-specific details
        return f"{super().get_details()}, Employee ID: {self.emp_id}, Department: {self.department}, Salary: ₹{self.salary}"

    def is_eligible_for_bonus(self):
        # Returns True if salary is less than 50,000
        return self.salary < 50000

    @classmethod
    def from_string(cls, data_string):
        # Create an Employee object from a formatted string
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, age, gender, emp_id, department, salary)

    @staticmethod
    def bonus_policy():
        # Print bonus policy description
        print("Bonus Policy: Employees with a salary less than ₹50,000 are eligible for a bonus.")


# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_average_salary(self):
        if len(self.employees) == 0:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]


# Data Persistence Functions
def save_to_json(employees):
    # Convert employee objects to dictionaries and save them to a JSON file
    employee_dicts = [vars(emp) for emp in employees]
    with open("employees.json", "w") as file:
        json.dump(employee_dicts, file, indent=4)

def load_from_json():
    # Load employee data from a JSON file and create employee objects
    with open("employees.json", "r") as file:
        employee_dicts = json.load(file)
    employees = []
    for emp_data in employee_dicts:
        emp = Employee(
            emp_data["name"], emp_data["age"], emp_data["gender"],
            emp_data["emp_id"], emp_data["department"], emp_data["salary"]
        )
        employees.append(emp)
    return employees


def save_to_csv(employees):
    # Save employee data to a CSV file
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["Name", "Age", "Gender", "Employee ID", "Department", "Salary"])
        
        # Write each employee's data
        for emp in employees:
            writer.writerow([emp.name, emp.age, emp.gender, emp.emp_id, emp.department, emp.salary])


def load_from_csv():
    # Load employee data from a CSV file and create employee objects
    employees = []
    with open("employees.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, age, gender, emp_id, department, salary = row
            emp = Employee(name, age, gender, emp_id, department, salary)
            employees.append(emp)
    return employees