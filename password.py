
import random
import string

def generate_password(length,complexity):
    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer greater than zero.")
                continue

            complexity = int(input("enter the complexity level:"))
            if complexity < 1 or complexity >3:
                print("compexity must be 1,2, or 3\n")
                continue
                
            password=generate_password(length,complexity)
            print("Generate password:",password)
            break
            
        except ValueError:
            print("Please enter a valid integer.")
            break

if __name__ == "__main__":
    main()
