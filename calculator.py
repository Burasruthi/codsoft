

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "can't divisible by zero."
    else:
        return x / y
def get_operation():
    print("Select operation:\n"
          "1.Add\n" \
          "2.Subtrat\n" \
          "3.multiply\n" \
          "4.Divide\n" \
          "5.exit\n")
    while True:
        choice =input("Enter choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4', '5'):
            return choice
        else:
            print("\n Invalid number")

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1,num2

def main():
        while True:
            choice = get_operation()
            if(choice=='5'):
                break
            num1,num2=get_numbers()


            if (choice == '1'):
                print("Result:", add(num1, num2))


            elif (choice == '2'):
                print("Result:", subtract(num1, num2))


            elif (choice == '3'):
                print("Result:", multiply(num1, num2))


            elif (choice == '4'):
                print("Result:", divide(num1, num2))

        
main()
