class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"Car Make: {self.brand}")

if __name__ == "__main__":
    my_car = Car("Toyota")
    my_car.start()  # Output: Car Make: Toyota