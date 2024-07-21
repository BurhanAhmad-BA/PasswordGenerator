import random
import string

def user_name():
    name = input("Enter Username: ")
    return name
def pw_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print ("Invalid input. Please enter a number.")
def generated_pw(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def display_password(password):
    print("Generated password:", password)

def main():
    print("Password Generator")
    username = user_name()
    length = pw_length()
    password = generated_pw(length)
    print (f"Username: {username}")
    display_password(password)

if __name__ == "__main__":
    main()