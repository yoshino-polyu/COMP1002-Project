import sys
from model import Model
from view import View
from GUI import GUIv
"""
The Controller class translates user actions into operations on the Model
"""
class ControllerG:
    def __init__(self, model : Model, view : View, GUI : GUI) -> None:
        self.model = model
        self.view = view
        self.GUI = GUI
    
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
                        suc = self.view.admin_id_valid()
                        if suc != '1':
                            continue
                        while True:
                            self.view.admin_page()
                            ad_ac = self.view.read_input()
                            if ad_ac == '1': # list out all information with indentation
                                self.view.list_all()
                            elif ad_ac == '2': # list out all the teaching staffs and students, who haven't been vaccinated, in the faculty of Engineering.
                                self.view.list_all_nova()
                            elif ad_ac == '3':
                                self.view.show_dep('-1') # displays all the student and staff, together with the percentage of fully vaccinated and haven't vaccinated ones, of a specific department. 
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
                while True:
                    self.GUIv.command_line()
                    which = self.GUIv.read_input()
                    if which == '1': # user login
                        id = self.GUIv.id_validation()
                        if id == '0':
                            continue
                        while True:
                            self.GUIv.user_page()
                            manner = self.GUIv.read_input()
                            if manner == '1': # change password
                                new = self.model.encode(self.GUIv.new_pass()) # password analysis???
                                self.model.update_password(id, new)
                                self.GUIv.valid()
                            elif manner == '2': # check current vaccination record
                                self.GUIv.record(id)
                                self.GUIv.valid()
                            elif manner == '3': # update vaccination record
                                record = self.GUIv.update_record(id)
                                self.model.append_record(id, record)
                                self.GUIv.valid()
                            elif manner == '4':
                                break
                            elif manner == '5':
                                return
                            else:
                                self.GUIv.inv_info()
                                continue
                    elif which == '2': # admin login
                        suc = self.GUIv.admin_id_valid()
                        if suc != '1':
                            continue
                        while True:
                            self.GUIv.admin_page()
                            ad_ac = self.GUIv.read_input()
                            if ad_ac == '1': # list out all information with indentation
                                self.GUIv.list_all()
                            elif ad_ac == '2': # list out all the teaching staffs and students, who haven't been vaccinated, in the faculty of Engineering.
                                self.GUIv.list_all_nova()
                            elif ad_ac == '3':
                                self.GUIv.show_dep('-1') # displays all the student and staff, together with the percentage of fully vaccinated and haven't vaccinated ones, of a specific department. 
                            elif ad_ac == '4':
                                secr = self.model.encode(self.GUIv.new_pass())
                                self.model.update_admin(secr)
                                self.GUIv.valid()
                            elif ad_ac == '5':
                                recg = self.GUIv.new_vacc()
                                self.model.update_vacc(recg)
                                self.GUIv.valid()
                            elif ad_ac == '6': #add new recognised vaccines into the the of recognised vaccines
                                break
                            elif ad_ac == '7':
                                return
                            else:
                                self.GUIv.inv_info()
                                continue
                    elif which == '3': # registration
                        u_id = self.GUIv.get_id()
                        l_n, f_n = self.GUIv.get_name()
                        dep = self.GUIv.choose_dpt()
                        inj_info = self.GUIv.get_inj_info()
                        who = self.GUIv.get_who()
                        secret = self.model.encode(self.GUIv.new_pass())
                        self.model.add_tuple(u_id, l_n, f_n, dep, inj_info, who, secret) # append all the information of this user to model fileds
                        self.GUIv.valid()
                    elif which == '4':
                        break
                    elif which == '5':
                        return
                    else:
                        self.GUIv.inv_info()
                        continue
            elif x == '3':
                return
            else:
                self.view.inv_info()
                continue