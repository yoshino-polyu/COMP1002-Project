#from os import _EnvironCodeFunc
from typing import Tuple
from model import Model
"""
The View is an observer of the Mddel, and it can observe the state of Model and then display it to user. 
"""

class View:
    def __init__(self, model : Model) -> None:
        self.model = model
    
    def id_validation(self):
        """
        Ask the user to input id and password, conduct the process of authentication.
        Return: 
        1. '0' when user want to exit this manu. 
        2. the string of id when the user login successfully.
        """
        res = ""
        while True:
            print("Please input your user id: (input 0 for exit this manu)")
            ID = input()
            if ID == '0':
                return '0'
            elif ID not in self.model.password:
                print("id does not exist, please try again")
                continue
            else:
                res = ID
                break
        while True:
            print("Please input your password: ")
            secret = self.model.encode(input())
            if secret != self.model.password[ID]:
                print("Incorrect password, please try again")
                continue
            else:
                print("\nlogin successfully\n")
                return res
    
    def admin_id_valid(self):
        """
        Check whether the user is the admin, and we only have one admin in this system, so we only need to check the password.
        Return:
        1. '0' when user want to exit this manu.
        2. '1' when user login successfully.
        """
        while True:
            secret = input("please input the password: (input -1 to return to last page) \n")
            if(secret == '-1'):
                break
            if(self.model.encode(secret) == self.model.admin_password):
                print("Login Successfully")
                return '1'
            print("Incorret password, please try again\n")
        return '0'
        # returns 0 if the user want to exit this manu
        # do not return anything, only allow at most 3 tries

    def list_all(self):
        """
        lists out all information, sorted by department with alphabetical order and proper indentation.
        indicates the percentage of fully vaccinated users, and that of ones who haven't been vaccinated, in a specific Department of Engineering faculty.
        """
        for i in ['AAE', 'BME', 'COMP','EE', 'EIE', 'ISE', 'ME']:
            self.show_dep(i)

    def list_all_nova(self):
        """
        lists out all the teaching staffs and students, who haven't been vaccinated, in the faculty of Engineering.
        """
        cnt = len(self.model.info) - 1
        ncnt = 0
        for i in self.model.isInjected[0]:
            ncnt += 1
            if(i[6] == 1):
                print("Student", end = ' ')
            else:
                print("Stuff", end = ' ')
            print(i[1] + " " + i[2] + " ("+ i[0]+") haven't been vaccinated.")
        print(str(ncnt/cnt * 100) + "%" + " students/stuffs haven't been vaccinated.")


    def show_dep(self, dep):
        """
        # displays all the student and staff, together with the percentage of 
        # those fully vaccinated and haven't vaccinated, of a specific department. 
        """
        if(dep == '-1'):
            while(1):
                print("Which department are you from?\nPlease input a number\n1. AAE 2. BME 3. COMP 4. EE 5. EIE 6. ISE 7. ME : ")
                c = input()
                if c == '1':
                    dep = "AAE"
                elif c == '2':
                    dep = "BME"
                elif c == '3':
                    dep = "COMP"
                elif c == '4':
                    dep = "EE"
                elif c == '5':
                    dep = "EIE"
                elif c == '6':
                    dep = "ISE"
                elif c == '7':
                    dep = "ME"
                else:
                    self.inv_info()
                    continue
                break
        print("Department: "+dep.upper())
        cnt = 0
        vcnt = 0
        ncnt = 0
        if(dep.lower() not in self.model.dpt):
            print("---------------------------------")
            return 
        for j in self.model.dpt[dep.lower()]:
            if(str(j[6]) == '1'):
                print("    Student", end = ' ')
            else:
                print("    Stuff", end = ' ')
            print(j[1].upper()+" "+j[2]+" ("+j[0]+")"+" has the vaccination record ", end = '')
            for k in j[5]:
                print(k, end=', ')
            cnt += 1
            if(str(j[4]) == '-1'):
                vcnt += 1
                print(" (Fully vaccinated)")
            elif(str(j[4]) == '0'):
                ncnt += 1
                print(" (Haven't been vaccinated)")
            else:
                print(" (Have "+str(j[4])+" vaccinations)")
        print(str(vcnt/cnt * 100)+"%"+" students/stuffs have been fully vaccinated")
        print(str(ncnt/cnt * 100)+"%"+" students/stuffs haven't been vaccinated")
        print("---------------------------------")
    
    def new_vacc(self):
        """
        ask admin to add some recognised vaccines newly issued by gov
        Return: the list of the added recognised vaccines
        """
        vac = self.model.rec_vac
        while True:
            print("Current recognised vaccines: ")
            for i in enumerate(vac[1:]):
                print(str(i[0]+1)+". "+i[1])
            print("----------------------")
            s = input("1. add a new recognised vaccines\n2. delete one vaccines\n3. quit\n")
            if(s == '1'):
                vac.append(input("Add Vaccination: ").upper())
            elif (s == '2'):
                try:
                    vac.remove(input("Delete Vaccination: ").upper())
                except Exception:
                    self.inv_info()
            elif (s == '3'):
                break
            else:
                self.inv_info()
        return vac

    
    
    def read_input(self):
        """ read input from user. """
        return str(input())

    def get_name(self):
        print("Last Name: ")
        last_n = input()
        print("First Name: ")
        first_n = input()
        return [last_n.lower(), first_n.lower()]

    def get_id(self):
        """
        gets a valid id from user.
        Note: a id is valid when it consists of 8 bits leading numbers and 1 bit of alphabet.
        """
        enums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        while True:
            id = input("pealse input your identity card number formed by 8 bits of number and 1 bit of alphabet.")
            if (len(id) != 9):
                self.inv_info()
                continue
            ok = 1
            for i, item in enumerate(id):
                if (i <= 7):
                    if (item not in enums):
                        ok = 0
                        break
                elif (ord(item) < ord('a') or ord(item) > ord('z')):
                    ok = 0
            if (ok == 0):
                self.inv_info()
                continue
            if(id in self.model.password):
                print("ID is already exist, please try again.\n")
                continue
            return id

    def get_who(self):
        """
        return a str indicating the user type, 1 -> student, 0 -> staff
        """
        res = ""
        while True:
            print("are you a student or staff?, 1 -> student, 0 -> staff: ")
            who = input()
            if who == '1':
                res = who
            elif who == '0':
                res = who
            else:
                self.inv_info()
                continue
            return res

    def choose_dpt(self):
        """
        returns a string of department name with upper case
        """
        res = ""
        while True:
            print("Which department are you from?\nPlease input a number\n1. AAE 2. BME 3. COMP 4. EE 5. EIE 6. ISE 7. ME : ")
            c = input()
            if c == '1':
                res = "AAE"
            elif c == '2':
                res = "BME"
            elif c == '3':
                res = "COMP"
            elif c == '4':
                res = "EE"
            elif c == '5':
                res = "EIE"
            elif c == '6':
                res = "ISE"
            elif c == '7':
                res = "ME"
            else:
                self.inv_info()
                continue
            break
        return res


    def get_inj_info(self):
        """
        returns number of injection and the vaccination information in the format of string.
        """
        num_inj = input("Please input how many injections you have received: ")
        print("Below are some of the vaccines recognized by the Hong Kong government:")
        for i in enumerate(self.model.rec_vac[1:]):
                print(str(i[0])+'. '+i[1])
        record = []
        while(1):
            print("\nCurrent Record: \n")
            for i in enumerate(record):
                print(str(i[0]+1)+'. '+i[1])
            print("-------------------\n")
            s = input("1. create a new record\n2. delete the last record\n3. stop editing\n")
            if(s == '3'):
                break
            elif(s == '1'):
                rc = input("Please input the vaccination record: (vaccination_day_month_year, example: AZ_01_09_2021)\n").upper()
                ck = rc.split('_')
                if(len(ck) != 4):
                    self.inv_info()
                    continue
                ligal = 0
                for i in self.model.rec_vac[1: ]:
                    if(i == ck[0]):
                        ligal = 1
                if(ligal == 0):
                    print("Vaccine is not recognized by Hong Kong government\n")
                    continue
                record.append(rc)
            elif(s == '2'):
                if(len(record) > 0):
                    record.pop()
            else:
                self.inv_info()
            # get a list of recognised vaccines from model, and print it out one by one
            # self.model.vaccines
            # e.g., print("1.   2. BTN 3. MOD")
        return [num_inj,record]

    
    def new_pass(self):
        """
        Ask user to input a valid password for creating or updating password.
        """
        a = ''
        ifligal = 0
        while(ifligal == 0):
            print("Please enter the password formed by 6 ~ 20 bits of numbers and letters: ")
            a = input()
            if(len(a) < 6 or len(a) > 20):
                print("Password is too Short or too long, please ensure it only contains 6 ~ 20 bits of numbers or letters")
                continue
            ifligal = 1
            for i in a:
                if (i.lower() > 'z' or i.lower() < 'a') and (i > '9' or i < '0'):
                    print("Password has unexpected characters, please ensure it only contains 6 ~ 20 bits of numbers or letters")
                    ifligal = 0
                    break
        return a
        
    def entry_page(self):
        """
        shows the entry page. 
        """
        print("Please input a number:")
        print("1. using command line interface")
        print("2. using graphic user interface")
        print("3. exit program")

    def command_line(self):
        """
        shows the login page.
        """
        print("Please input a number:")
        print("1. user login")
        print("2. administrator login")
        print("3. register an account")
        print("4. go back to the last page")
        print("5. exit program")

    def user_page(self):
        """
        shows the user manual.
        """
        print("Please input a number:")
        print("1. change the password")
        print("2. see current vaccination record")
        print("3. update vaccination record")
        print("4. logout")
        print("5. exit program")
    
    def admin_page(self):
        """
        shows the admin manual. 
        """
        print("Please input a number:")
        print("1. list out all information, sorted by department with alphabetical order and proper indentation.")
        print("2. list out all the teaching staffs and students, who haven't been vaccinated, in the faculty of Engineering.")
        print("3. displays the percentage of fully vaccinated, and non-vaccinated users in a specific department")
        print("4. change password of administrator")
        print("5. add new recognised vaccines into the the of recognised vaccines")
        print("6. logout")
        print("7. exit program")

    def inv_info(self):
        """ alert the user that an illegal string has been entered, and ask user to re-enter it. """
        print("\ninvalid input, please try again!\n")
        
    def valid(self):
        """ Prompt the user that the operation was successful. """
        print("\naction succeed!\n")
    
    def update_record(self, ID):
        """
        Param: id of the user that change his or her vaccination record.
        Return:
        1. the updated number of injection of the user
        2. the updated vaccination record of the user
        returns the string of vaccination record input by user
        """
        self.record(ID)
        num_inj = self.model.id[ID][4]
        rd = self.model.id[ID][5]
        if(input("Edit the number of injections? [y/n]: ").lower() == 'y'):
            print("Please input how many injections you have received:")
            num_inj = input()
            print()
        if(input("Edit the record of injections? [y/n]: ").lower() == 'n'):
            return [num_inj,rd]
        print("Below are some of the vaccines recognized by the Hong Kong government:")
        for i in enumerate(self.model.rec_vac[1:]):
                print(str(i[0])+'. '+i[1])
        while(1):
            print("\nCurrent Record: \n")
            for i in enumerate(rd):
                print(str(i[0]+1)+'. '+i[1])
            print("-------------------\n")
            s = input("1. create a new record\n2. delete the last record\n3. stop editing\n")
            if(s == '3'):
                break
            elif(s == '1'):
                rc = input("Please input the vaccination record: (vaccination_day_month_year, example: AZ_01_09_2021)\n")
                ck = rc.split('_')
                if(len(ck) != 4):
                    self.inv_info()
                    continue
                ligal = 0
                for i in self.model.rec_vac[1: ]:
                    if(i == ck[0]):
                        ligal = 1
                if(ligal == 0):
                    print("Vaccine is not recognized by Hong Kong government\n")
                    continue
                rd.append(rc)
            elif(s == '2'):
                if(len(rd) > 0):
                    rd.pop()
            else:
                self.inv_info()
        return [num_inj,rd] # number of injections : str, vaccination record : str

    def record(self, ID):
        """
        displays the vaccination record of a specific user.
        Param: id of the user that want ot see his or her vaccination record.
        """
        tmp = self.model.id[ID]
        if(str(tmp[4]) == '-1'):
            print("Vaccination has been completed.")
        else:
            print(str(tmp[4]) + " vaccinations have already been given.")
        print("Vaccination record: ")
        for i in tmp[5]:
            print("------------------------\n"+i)
        print("------------------------")