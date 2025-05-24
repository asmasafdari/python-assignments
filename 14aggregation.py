class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Department():
    def __init__(self, employee):
        self.employee = employee
    def show_employee(self):
        print(f"Employee Name: {self.employee.name}, Age: {self.employee.age}")
if __name__ == "__main__":
    emp = Employee("John Doe", 30)
    dept = Department(emp)
    dept.show_employee()
    # Output: Employee Name: John Doe, Age: 30