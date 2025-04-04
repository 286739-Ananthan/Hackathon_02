from management import Employee, Department, save_to_json, load_from_json, save_to_csv, load_from_csv

# Sample Data
data_strings = [
    "Alice,30,Female,E101,HR,48000",
    "Bob,28,Male,E102,IT,55000",
    "Charlie,35,Male,E103,HR,60000",
    "Diana,26,Female,E104,IT,47000",
    "Evan,40,Male,E105,Finance,53000"
]

# Create Employee objects from data strings
employees = [Employee.from_string(s) for s in data_strings]

# Create Departments and assign employees to them
departments = {}
for emp in employees:
    if emp.department not in departments:
        departments[emp.department] = Department(emp.department)
    departments[emp.department].add_employee(emp)

# Print Bonus Policy
Employee.bonus_policy()

# Print Employee Details
print("\nEmployee Details:")
for emp in employees:
    print(emp.get_details())

# Print Department Average Salaries
print("\nAverage Salaries by Department:")
for dept_name, dept in departments.items():
    print(f"{dept_name}: ₹{dept.get_average_salary():.2f}")

# Save Data to JSON
save_to_json(employees)

# Save Data to CSV
save_to_csv(employees)

# Load Data from JSON
print("\n📂 Loaded Data from JSON:")
loaded_emps_json = load_from_json()
for emp in loaded_emps_json:
    print(emp.get_details())

# Load Data from CSV
print("\n📂 Loaded Data from CSV:")
loaded_emps_csv = load_from_csv()
for emp in loaded_emps_csv:
    print(emp.get_details())
