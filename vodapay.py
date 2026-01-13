
attempts = 3
pin = 1234

while True:
    print("_____________________")
    print("Main Menu")
    print("1. Login")
    print("2. Forgot Password")
    print("3. Exit")
    print("_____________________")

    user_input = int(input("Enter your choice: "))

    if user_input == 1:
        attempts = 3

        while attempts > 0:
            user_pin = int(input("Please Enter Your PIN: "))
            if not isinstance(user_pin,(int)):
                raise ValueError("PIN must contain digits only")

            if user_pin == pin:
                print("Login Successfully")
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"You have {attempts} attempts left. Please Try Again!")
                else:
                    print("Your PIN has been blocked!")
                    break

    elif user_input == 2:
        print(f"Your PIN is {pin}")

    elif user_input == 3:
        user_response = input("are you sure you want to Exit? \n Yes or No?")
        user_response = user_response.strip().lower()
        if user_response.startswith("n"):
            continue
        elif user_response.startswith("y"):
            break
        else:
            print("Invalid choice, Please try again!!..")

    else:
        print("Invalid choice, please try again.!!..")
def main():
    pass
~                
