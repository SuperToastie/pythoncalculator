"""Basic Python Calculator"""
import math

def add(x, y):
    """
    Add two numbers.

    Parameters:
    x (float): First number.
    y (float): Second number.

    Returns:
    float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.

    Parameters:
    x (float): First number.
    y (float): Second number.

    Returns:
    float: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiply two numbers.

    Parameters:
    x (float): First number.
    y (float): Second number.

    Returns:
    float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide one number by another.

    Parameters:
    x (float): Numerator.
    y (float): Denominator.

    Returns:
    float or str: The quotient of x and y, or an error message if division by zero is attempted.
    """
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

def sin(x):
    """
    Calculate the sine of an angle.

    Parameters:
    x (float): The angle in degrees.

    Returns:
    float: The sine of x degrees.
    """
    return math.sin(math.radians(x))

def cos(x):
    """
    Calculate the cosine of an angle.

    Parameters:
    x (float): The angle in degrees.

    Returns:
    float: The cosine of x degrees.
    """
    return math.cos(math.radians(x))

def tan(x):
    """
    Calculate the tangent of an angle.

    Parameters:
    x (float): The angle in degrees.

    Returns:
    float: The tangent of x degrees.
    """
    return math.tan(math.radians(x))

def arcsin(x):
    """
    Calculate the arcsine of a value.

    Parameters:
    x (float): The value.

    Returns:
    float: The angle in degrees whose sine is x.
    """
    return math.degrees(math.asin(x))

def arccos(x):
    """
    Calculate the arccosine of a value.

    Parameters:
    x (float): The value.

    Returns:
    float: The angle in degrees whose cosine is x.
    """
    return math.degrees(math.acos(x))

def arctan(x):
    """
    Calculate the arctangent of a value.

    Parameters:
    x (float): The value.

    Returns:
    float: The angle in degrees whose tangent is x.
    """
    return math.degrees(math.atan(x))

print("Welcome to the Python Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Sine")
    print("6. Cosine")
    print("7. Tangent")
    print("8. Arcsine")
    print("9. Arccosine")
    print("10. Arctangent")
    print("11. Exit")

    choice = input("Enter choice (1-11): ")

    if choice == '11':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice in ['5', '6', '7', '8', '9', '10']:
        num1 = float(input("Enter the angle in degrees: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", sin(num1))
    elif choice == '6':
        print("Result:", cos(num1))
    elif choice == '7':
        print("Result:", tan(num1))
    elif choice == '8':
        print("Result:", arcsin(num1))
    elif choice == '9':
        print("Result:", arccos(num1))
    elif choice == '10':
        print("Result:", arctan(num1))
    else:
        print("Invalid input. Please enter a valid choice.")
