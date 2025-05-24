class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person {self.name} created.")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the parent class
        self.subject = subject
        print(f"Teacher {self.name} teaches {self.subject}.")  

if __name__ == "__main__":
    teacher = Teacher("Alice", "Math")
    # Output: Person Alice created.
    #         Teacher Alice teaches Math.              

    