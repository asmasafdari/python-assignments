class Logger:
    def __init__(self):
      print("Logger initialized")

    def __del__(self):
        # Destructor
        # This method is called when the object is about to be destroyed
        # You can perform cleanup tasks here    

        print("Logger destroyed")
if __name__ == "__main__":
     log = Logger()
     del log #this deletes the object
     # The destructor will be called here
          