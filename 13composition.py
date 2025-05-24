class Engine:
    def start(self):
        print("Engine started. ")

class Car:
    def __init__(self):
        self.engine = Engine() #composition 
    def start_car(self):
        self.engine.start()

if __name__ == "__main__":
    car = Car()
    car.start_car()
    # Output: Engine started.               