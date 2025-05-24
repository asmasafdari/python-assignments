class Dog:
    def __init__(self, name, breed):
        self.breed = breed # instance variable
        self.name = name # instance variable
        print(f"Dog {self.name} of breed {self.breed} created.")

    def bark(self): # instance method
        print(f"{self.name} of breed {self.breed} says Woof!")

if __name__ == "__main__":
    # Creating instances object of the Dog class
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "Bulldog")
    # Accessing / calling instance variables
    dog1.bark()  # Output: Buddy of this Golden Retriever says Woof!
    dog2.bark()  # Output: Max of this Bulldog says Woof!        