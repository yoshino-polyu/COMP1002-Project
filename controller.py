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
        if (self.model.init() == 0): # read all info from txt, and store it into storage.
            self.model.init()
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
                                record = self.view.update_record(id)
                                self.model.append_record(id, record)
                                self.view.valid()
                            elif manner == '4':
                                break
                            elif manner == '5':
                                return
                            else:
                                self.view.inv_info()
                                continue
                    elif which == '2': # admin login
                        admin_id = self.view.admin_id_valid()
                        print(admin_id)
                        if admin_id != 1:
                            continue
                        while True:
                            self.view.admin_page()
                            ad_ac = self.view.read_input()
                            if ad_ac == '1': # list out all information with indentation
                                self.view.list_all()
                            elif ad_ac == '2': # list out all the teaching staffs and students, who haven't been vaccinated, in the faculty of Engineering.
                                self.view.list_all_nova()
                            elif ad_ac == '3':
                                self.view.show_dep('-1') # displays the percentage of fully vaccinated, and non-vaccinated users in a specific department
                            elif ad_ac == '4':
                                secr = self.model.encode(self.view.new_pass())
                                self.model.update_admin(secr)
                                self.view.valid()
                            elif ad_ac == '5':
                                recg = self.view.new_vacc()
                                self.model.update_vacc(recg)
                                self.view.valid()
                            elif ad_ac == '6': #add new recognised vaccines into the the of recognised vaccines
                                break
                            elif ad_ac == '7':
                                return
                            else:
                                self.view.inv_info()
                                continue
                    elif which == '3': # registration
                        u_id = self.view.get_id()
                        l_n, f_n = self.view.get_name()
                        dep = self.view.choose_dpt()
                        inj_info = self.view.get_inj_info()
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
                        continue
            elif x == '2': # GUI
                return 0
            elif x == '3':
                return
            else:
                self.view.inv_info()
                continue