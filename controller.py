"""
The Controller class translates user actions into operations on the Model,
although it depends on command line interface to read keystrokes.
"""
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def run(self):
        self.model.init() # read all info from txt, and store it into storage.
        while True:
            self.view.entry_page()
            x = self.view.read_input()
            if x == '1':
                while True:
                    self.view.command_line()
                    which = self.view.read_input()
                    if which == '1':
                        id = self.view.id_validation()[0]
                        self.view.user_page()
                        user_manner = self.view.read_input()
                        if user_manner == 'a':
                            self.model.update_password()
                        elif user_manner == 'b':
                            return 0
                
            
        
        