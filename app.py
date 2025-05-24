def main():
    print("Add 2 numbers!")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter second number: ")
    num2 : int = int(num2)
    # Add your main application logic here
    total : int = int(num1) + int(num2)
    print(f"The total is " + str(total) + ".")
    print("Thank you for using the app!")
    print("Goodbye!")
     
    # this provides a way to run the app as a script
    # or import it as a module in another script
    # python file to call the main() function
if __name__ == "__main__":
    main()