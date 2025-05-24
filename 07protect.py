class Empolyee:
    def __init__(self, name, salary, ssn):
        self.name = name #public attribute
        # Private attribute
        self._ssn = ssn
        # Protected attribute
        self.__salary = salary
        # The underscore prefix indicates that this attribute is intended for internal use
        # and should not be accessed directly from outside the class.
        # However, it is still accessible from subclasses and within the class itself.
        #print("Employee salary:", self.__salary)
if __name__ == "__main__":
        emp = Empolyee("John Doe", 50000, "123-45-6789")
        print("public variabl: ", emp.name) # This will raise an AttributeError
        print("private variable: ", emp._ssn)   # This will work
        print("protected variable: ", emp.__salary) # This will raise an AttributeError       