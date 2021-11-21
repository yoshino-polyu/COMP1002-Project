"""
The View is an observer of the Mddel.
"""

class View:
    def __init__(self, model):
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
            return [id, secret]
    
    def read_input(self):
        return str(input())