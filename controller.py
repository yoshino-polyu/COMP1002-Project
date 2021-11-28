import sys
from model import Model
from view import View
"""
The Controller class translates user actions into operations on the Model,
although it depends on command line interface to read keystrokes.
"""
class Controller:
    def __init__(self, model : Model, view : View) -> None:
        self.model = model
        self.view = view
    
    def run(self):
        self.model.init() # read all info from txt, and store it into storage.
        while True:
            self.view.entry_page()
            x = self.view.read_input()
            if x == '1': # CLI
                while True:
                    self.view.command_line()
                    which = self.view.read_input()
                    if which == '1': # user login
                        id = self.view.id_validation()
                        if id == '0':
                            continue
                        while True:
                            self.view.user_page()
                            manner = self.view.read_input()
                            if manner == '1': # change password
                                new = self.model.encode(self.view.new_pass()) # password analysis???
                                self.model.update_password(id, new)
                                self.view.valid()
                            elif manner == '2': # check current vaccination record
                                self.view.record(id)
                                self.view.valid()
                            elif manner == '3': # update vaccination record
                                record = self.view.update_record()
                                self.model.append_record(record)
                                self.view.valid()
                                return 0
                            elif manner == '4':
                                break
                            elif manner == '5':
                                return 0
                            else:
                                self.view.inv_info()
                    elif which == '2': # admin login
                        id = self.view.id_validation()
                        self.view.admin_page()
                        return 0
                    elif which == '3': # registration
                        u_id = self.view.get_id()
                        # format checking, 8 bits of number + 1 bit of alphabet
                        l_n, f_n = self.view.get_name()
                        # format checking
                        dep = self.view.choose_dpt()
                        # num of intejction is generated by injection information
                        inj_info = self.view.get_inj_info() # list of injection information
                        #n_inj = len(inj_info) # the len of inj_info is the number of injection
                        who = self.view.get_who()
                        secret = self.model.encode(self.view.new_pass())
                        self.model.add_tuple(u_id, l_n, f_n, dep, inj_info, who, secret) # append all the information of this user to model fileds
                        self.view.valid()
                    elif which == '4':
                        break
                    elif which == '5':
                        return
                    else:
                        self.view.inv_info()
            elif x == '2': # GUI
                return 0
            elif x == '3':
                return 0
            else:
                self.view.inv_info()
                
            
        
        