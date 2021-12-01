import sys
from model import Model
from view import View
from GUI import GUIv
"""
The Controller class translates user actions into operations on the Model.
"""
class Controller:
    def __init__(self, model : Model, view : View, GUIv: GUIv) -> None:
        self.model = model
        self.view = view
        self.GUIv = GUIv
    
    def run(self):
        if (self.model.init() == '0'): # read all info from txt, and store it into storage.
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
                                new = self.model.encode(self.view.new_pass())
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
                        suc = self.view.admin_id_valid()
                        if suc != '1':
                            continue
                        while True:
                            self.view.admin_page()
                            ad_ac = self.view.read_input()
                            if ad_ac == '1':
                                self.view.list_all()
                            elif ad_ac == '2':
                                self.view.list_all_nova()
                            elif ad_ac == '3':
                                self.view.show_dep('-1')
                            elif ad_ac == '4': # change the passowrd of administrator
                                secr = self.model.encode(self.view.new_pass())
                                self.model.update_admin(secr)
                                self.view.valid()
                            elif ad_ac == '5': # update the list of recognised vaccines
                                recg = self.view.new_vacc()
                                self.model.update_vacc(recg)
                                self.view.valid()
                            elif ad_ac == '6': # logout
                                break
                            elif ad_ac == '7':
                                return
                            else:
                                self.view.inv_info()
                                continue
                    elif which == '3': # user registration
                        u_id = self.view.get_id()
                        l_n, f_n = self.view.get_name()
                        dep = self.view.choose_dpt()
                        inj_info = self.view.get_inj_info()
                        who = self.view.get_who()
                        secret = self.model.encode(self.view.new_pass())
                        self.model.add_tuple(u_id, l_n, f_n, dep, inj_info, who, secret) # append all the information of this newly created user to model fileds
                        self.view.valid()
                    elif which == '4':
                        break
                    elif which == '5':
                        return
                    else:
                        self.view.inv_info()
                        continue
            elif x == '2': # GUI
                self.GUIv.main_page()
            elif x == '3':
                return
            else:
                self.view.inv_info()
                continue