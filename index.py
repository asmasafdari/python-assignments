def main():
    print("Temperature Converter! :)")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
    print("Thank you for using the app!")
    print("Goodbye!")

    # Thi provides a way to run the app as a script
    #python file to call the main() function
if __name__ == "__main__":
    main()