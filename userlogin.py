from functions import register, login


class UserLogin:
    def __init__(self, user_data):
        self.login_choice = input("Enter 1 to register or 2 to login : ")
        if self.login_choice == "1":
            self.login_status = register(user_data)
        elif self.login_choice == "2":
            self.login_status = login(user_data)
        else:
            print("Invalid Choice")

