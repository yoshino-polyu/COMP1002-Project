from model import Model
"""
The View is an observer of the Mddel, and it can observe the state of Model and then display it to user. 
"""

class View:
    def __init__(self, model : Model) -> None:
        self.model = model
    
    def id_validation(self):
        while True:
            id = str(input("Please input your user id").split())
            if id not in self.model.password:
                print("id does not exist, please try again")
                continue
            secret = str(input("Please input your password").split())
            if secret != self.model.password[id]:
                print("Incorrect password, please try again")
                continue
            print("login successfully")
            return id
    
    def read_input(self):
        return str(input())
        
    def new_pass(self):
        return str(input("Please enter the new password: "))

    def entry_page(self):
        page = """
        Please input a number:
        1. using command line interface
        2. using graphic user interface
        3. exit program"""
        print(page)
    
    def command_line(self):
        page = """
        Please input a number:
        1. user login
        2. administrator login
        3. go back to the last page
        4. exit program
        """
        print(page)

    def user_page(self):
        page = """
        Please input a number:
        1. change the password
        2. see current vaccination record
        3. update vaccination record
        4. go back to the last page
        5. exit program"""
        print(page)

    def inv_info(self):
        print("invalid input, please try again!")
        
    def valid(self):
        print("action succeed!")