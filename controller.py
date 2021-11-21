"""
The Controller class translates user actions into operations on the Model,
although it depends on command line interface to read keystrokes.
"""
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def run(self):
        while True:
            page_1 = """
            Please input a number
            1. using command line interface
            2. using graphic user interface
            3. go back to the last page
            4. exit program"""
            print(page_1)
            x = self.view.read_input()
            if x == '1':
                while True:
                    page_2 = """
                    Please input a number:
                    1. user login
                    2. administrator login
                    3. go back to the last page
                    4. exit program"""
                    print(page_2)
                    which = self.view.read_input()
                    if which == '1':
                        id = self.view.id_validation()[0]
                        page = """
                        Please input a number:
                        1. change the password
                        2. see current vaccination record
                        3. update vaccination record
                        4. go back to the last page
                        5. exit program"""
                        print(page)
                        user_manner = self.view.read_input()
                        if user_manner == 'a':
                            self.model.update_password()
                        elif user_manner == 'b':
                            return 0
                
            
        
        