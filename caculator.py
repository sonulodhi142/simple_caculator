def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def floorValue(a,b):
    return a//b
def remainder(a,b):
    return a%b
def power(a,b):
    return a**b

check = 'y'

while check == 'y':

    print("\n\nSelect opration for two oprands:-")
    print("1. click '+' for adition")
    print("2. click '-' for substraction")
    print("3. click '*' for multiplication")
    print("4. click '/' for division")
    print("5. click '//' for for floor Value")
    print("6. click '%' for remainder")
    print("7. click '**' for exponential")
    choice = input("Please Enter your choise::")
    num1 = int(input("Enter the first number ::"))
    num2 = int(input("Enter the Second number ::"))

    if choice == '+':
        print(f"\nThe addition of {num1} and {num2} is {addition(num1,num2)}\n\n")
    elif choice == '-':
        print(f"\nThe Substraction of {num1} and {num2} is {addition(num1,num2)}\n\n")
    elif choice == '*':
        print(f"\nThe multiplication of {num1} and {num2} is {addition(num1,num2)}\n\n")
    elif choice == '/':
        print(f"\nThe division of {num1} and {num2} is {addition(num1,num2)}")
    elif choice == '//':
        print(f"\nThe floorvalue of when {num1} divided by {num2} is {addition(num1,num2)}\n\n")
    elif choice == '%':
        print(f"\nThe remainder of when {num1} divided by {num2} is {addition(num1,num2)}\n\n")
    elif choice == '**':
        print(f"\nThe result of {num1} to the power {num2} is {addition(num1,num2)}\n\n")
    else:
        print("\nplease Enter the vailed choise:-\n\n")



    check = input("Enter 'y' for more opration\nEnter 'n' for exit program::")

print("\n The program is succesfully exited :")