def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "ERROR:CANT DIVIDE BY ZERO"
    return a/b
def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator"
    
def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Perform Calculation")
        print("2. Clear")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                result = calculate(num1, operator, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == "2":
            print("Calculator cleared!")

        elif choice == "3":
            print("Exiting calculator...")
            break

        else:
            print("Invalid menu choice!")

calculator()