from typing import Tuple
from model import Model
"""
The View is an observer of the Mddel, and it can observe the state of Model and then display it to user. 
"""

class View:
    def __init__(self, model : Model) -> None:
        self.model = model
    
    def id_validation(self):
        while True:
            ID = input("Please input your user id: ")
            if ID not in self.model.password:
                print("id does not exist, please try again")
                continue
            secret = input("Please input your password: ")
            if secret != self.model.password[ID]:
                print("Incorrect password, please try again")
                continue
            print("login successfully")
            return ID
    
    def admin_id_valid(self):
        while True:
            ID = input("Please input your user id: ")
            
        # do not return anything, only allow at most 3 tries
        
    """
    check whether the user is the admin, and we only have one admin in this system. 
    """
    def read_input(self):
        return str(input())


    def get_name(self):
        pass
        # while True:
        # L = input("Please input your last name and first name separate by comma. (i.e. Chen,Dawen)").split(',')
            
        # return ['last', 'fi']
        
    def get_id(self):
        enums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        res = ""
        while True:
            id = input("pealse input your identity card number formed by 8 bits of number and 1 bit of alphabet ")
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
            return res
    """
    gets a valid id from user
    """
    def get_who(self):
        res = ""
        while True:
            who = input("are you a student or staff?, 1 -> student, 0 -> staff")
            if who == '1':
                res = who
            elif who == '0':
                res = who
            else:
                self.inv_info()
                continue
            return res
    """
    return a str indicating the user type, 1 -> student, 0 -> staff
    """
    def choose_dpt(self):
        print("Witch department are you from?")
        res = ""
        while True:
            c = input("Please input a number\n1. AAE 2. BME 3. COMP 4. EE 5. EIE 6. ISE 7. ME")
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
    """
    returns a string of department name with upper case
    """

    def get_inj_info(self):
        print("Please input the type of vaccine you have received:\nBelow are some of the vaccines recognized by the Hong Kong government:")
        # get a list of recognised vaccines from model, and print it out one by one
        # self.model.vaccines
        # e.g., print("1. AZ 2. BTN 3. MOD")
        return 0
    """
    returns a ??? of injection information
    """
    
    def new_pass(self):
        a = ''
        ifligal = 0
        while(ifligal == 0):
            a = str(input("Please enter the new password formed by 10 ~ 20 bits of numbers and letters"))
            if(len(a) < 10 or len(a) > 20):
                print("Password is too Short or too long, please ensure it only contains 10 ~ 20 bits of numbers or letters")
                continue
            ifligal = 1
            for i in a:
                if (i.lower() > 'z' or i.lower() < 'a') and (i > '9' or i < '0'):
                    print("Password has unexpected characters, please ensure it only contains 10 ~ 20 bits of numbers or letters")
                    ifligal = 0
                    break
        return a

    def entry_page(self):
        print("Please input a number:")
        print("1. using command line interface")
        print("2. using graphic user interface")
        print("3. exit program")

    def command_line(self):
        print("Please input a number:")
        print("1. user login")
        print("2. administrator login")
        print("3. register an account")
        print("4. go back to the last page")
        print("5. exit program")

    def user_page(self):
        print("Please input a number:")
        print("1. change the password")
        print("2. see current vaccination record")
        print("3. update vaccination record")
        print("4. go back to the last page")
        print("5. exit program")
    
    def admin_page(self):
        print("Please input a number:")
        print("1. list all information, sorted by department with alphabetical order and proper indentation")
        print("2. display a vaccination information of a specific student or teaching staff according to his or ")
        print("3. ")
        
        
    def inv_info(self):
        print("invalid input, please try again!")
        
    def valid(self):
        print("action succeed!")
    
    def update_record():
        print("Please input the date of your most recent vaccination in the format of dd/mm/yyyy")
        # format checking -> until user input the correct formate
        print("Please enter the type of vaccine you have taken in upper case")
        # format checking -> until user input the correct formate
        # return the record string
        pass # comment out pass once finishing this function
    """
    returns the string of vaccination record input by user
    """
    def record(self, ID):
        tmp = self.model.id[ID]
        if(str(tmp[4]) == '-1'):
            print("Vaccination has been completed.")
        else:
            print(str(tmp[4]) + " vaccinations have already been given.")
        print("Vaccination record: ")
        for i in tmp[5]:
            print("------------------------\n"+i)
        print("------------------------")
    """
    displays the vaccination record of a specific user.
    """