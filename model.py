"""
The Model 
    includes user information being represented, and will be acted upon latter. 
    determine the system state
"""
from io import TextIOWrapper
from os import TMP_MAX, error
import sys
from collections import defaultdict

class WrongFileError(Exception):
    """ Raised when the format of storage.txt is incorrect"""
    pass

class Model:

    NUM_FILES = 7
    
    def __init__(self):
        self.info = []   # [user id, last name, first name, department, number of injection (-1 means fully vaccinated),[injection info],'studentornot']
        self.pass_info = [] # [user id, password]

        # [the name of recognized vaccines, ... ] the admin will update the list of recognized vaccines according to the latest information
        # from Hong Kong government. Only the recognized vaccines can be recorded in the file system. 
        self.rec_vac = [] 

        self.admin_password = '' # password of admin

        self.id = dict()
        self.dpt = defaultdict(list) # a dictionary which's key is department, admin can search the department to get the information of its students and stuffs
        self.isInjected = defaultdict(list) # a dictionary which's key is number of injection, admin can get the information that who have not been inejected
        self.userIndex = defaultdict(list) # a dictionary help to get the one user's index of info[] and pass_info[], which can help update the information quickly
        self.password = dict() # a dictionary help to confirm the user's password


    def encode(self, p):
        """
        Encrypts the string (actual password) entered by the user and returns the encrypted string.
        Motivation: 
        1. When others access password.txt, they do not know what a particular user's password is.
        2. Verifying wther the password entered by the user is correct is to determine whether encode(input) is equal to 
        the encrpted string in password.txt
        """
        h1 = 0
        h2 = 0
        h3 = 0
        for i in p:
            h1 = (h1 * 2333 + ord(i)) % 1000000007
            h2 = (h2 * 9973 + ord(i)) % 998244353
            h3 = (h3 * 3001 + ord(i)) % 10000000019
        return str(h1) + str(h2) + str(h3)

    
    def add_tuple(self, ID : str, LAST : str, FIRST : str, DEP : str, INJ_INFO : list, WHO : str, SEC : str):
        """ Adds all the information about the newly registered user to instance variables. """
        temp = [ID, LAST, FIRST, DEP, INJ_INFO[0], INJ_INFO[1], WHO]
        self.info.append(temp)
        self.id[ID] = temp
        self.dpt[DEP].append(temp)
        self.isInjected[INJ_INFO[0]].append(temp)
        self.userIndex[ID].append(len(self.info)-1)

        self.pass_info.append([ID, SEC])
        self.password[ID] = SEC
        self.userIndex[ID].append(len(self.pass_info)-1)
    
    
    def create_new_storage(self):
        """
        Transfers data into the system and writes the specified string to a file. 
        The string content is stored in the buffer until the file is closed or the buffer is flushed
        """
        print("Create a new storage file")
        FL = open("storage.txt","x")
        FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
        FL.close()

    
    def update_admin(self, word : str):
        """
        updates the password of admin
        Param: word -> the new password of admin
        """
        self.admin_password = word


    def update_vacc(self, list_vacc : list):
        """
        adds the newly recognised vaccines into existing recognised vaccines
        Param: list_vacc -> the newly recognised vaccines from admin
        """
        self.rec_vac = list_vacc
        pass

    def wrong_file_storage(self):
        """
        This function is called to create a new storage.txt file if the storage format of the storage.txt file 
        does not conform to the storage specification we defined when reading each line.
        """
        s = input("Unexcepted information in storage file, create a new file? [y/n]")
        if (s == 'y' or s == 'Y'):
            self.info.clear()
            FL = open("storage.txt","w")
            FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
            FL.close()
            raise WrongFileError # go to self.init()
        else:
            print('Program Exit')
            sys.exit()
        
        
    def load_file(self):
        """ Open the txt file for reading, and create a new one if the txt file cannot be found. """
        try:
            FL = open("storage.txt","r", encoding = 'UTF-8')
            self.read_lines(FL)
        except FileNotFoundError:
            self.create_new_storage()
            FL = open("storage.txt","r", encoding = 'UTF-8')
            self.read_lines(FL)
        finally:
            FL.close()


    def read_lines(self, FL : TextIOWrapper):
        """ 
        read lines for initialising self.info where all users' information is stored.
        Param: FL -> A file that has been opened and is in a readable state.
        """
        for i in FL.readlines():
            try:
                eval(i)
            except SyntaxError:
                FL.close()
                self.wrong_file_storage()
                break
            if isinstance(eval(i), list) == 0:
                FL.close()
                self.wrong_file_storage()
                break
            if (len(eval(i)) != Model.NUM_FILES):
                FL.close()
                self.wrong_file_storage()
                break
            i = eval(i)
            for j in enumerate(i):
                if isinstance(j[1],str) == 1:
                    i[j[0]] = j[1].lower() # convert all characters to lowercase
            self.info.append(i)
            
    def create_new_password(self):
        """
        creates a new password.txt file
        """
        #print("create a new password file")
        FL = open("password.txt","x")
        FL.write("['user','password']\n")
        FL.close()


    def read_password(self):
        """
        read password.txt file and store it into self.pass_info.
        """
        try:
            FL = open("password.txt", "r", encoding = "UTF-8")
        except FileNotFoundError:
            self.create_new_password()
            FL = open("password.txt", "r", encoding= 'UTF-8')
        finally:
            for i in FL.readlines():
                self.pass_info.append(eval(i))
            FL.close()

    def create_new_admin(self):
        """
        create a new admin.txt file for storing the password of admin, and the default password is "admin"
        this method will be invoked when previous admin.txt file is not found. 
        """
        #print("create a new admin file")
        FL = open("admin.txt","x")
        FL.write(str(self.encode("admin")))
        FL.close()


    def read_admin(self):
        """
        read admin.txt, and store it into self.admin_password. 
        """
        try:
            FL = open("admin.txt", "r", encoding = "UTF-8")
        except FileNotFoundError:
            self.create_new_admin()
            FL = open("admin.txt","r", encoding = "UTF-8")
        finally:
            for i in FL.readlines():
                self.admin_password = i.strip('\n')
            FL.close()
    
    def update_password(self, id, new):
        """
        update the password dictionary and the list of password information. 
        Param: id is the user id, new is the new changed password string with encryption.
        """
        self.password[id] = new
        self.pass_info[self.userIndex[id][1]][1] = new
    
    def append_record(self, ID, record : list):
        """
        rewrite the corresponding fields of a specific user according to the latest vaccination record.
        """
        x = self.info[self.userIndex[ID][0]]
        self.dpt[x[3]].remove(x)
        self.isInjected[x[4]].remove(x)
        x[4] = record[0]
        x[5] = record[1]
        self.id[x[0]] = x
        self.dpt[x[3]].append(x)
        self.isInjected[x[4]].append(x)

    
    def create_new_vaccination(self):
        """
        create a new vaccination file vaccination.txt with the first line is "vaccination name".
        """
        #print("create a new vaccination file")
        FL = open("vaccination.txt","x")
        FL.write("'vaccination name'\n")
        FL.close()

    def read_vaccination(self):
        """
        read the list of recognized vaccines from vaccination.txt
        """
        try:
            FL = open("vaccination.txt", "r", encoding = "UTF-8")
        except FileNotFoundError:
            self.create_new_vaccination()
            FL = open("vaccination.txt", "r", encoding = "UTF-8")
        finally:
            for i in FL.readlines():
                self.rec_vac.append(i.strip('\n'))
            FL.close()

    def init(self):
        """
        read data from the storage.txt, password.txt, admin.txt and vaccination.txt to store them into the state of this model object.
        update the corresponding dictionary for subsequent queries.
        """
        try:
            self.load_file()
        except WrongFileError:
            print("the format of storage.txt is wrong, and a new one is created!")
            return '0'
        self.read_password()
        self.read_vaccination()
        self.read_admin()
        for j in enumerate(self.info[1:]):
            i = j[1]
            self.id[i[0]] = i
            self.dpt[i[3]].append(i)
            self.isInjected[i[4]].append(i)
            self.userIndex[i[0]].append(j[0]+1)
        for j in enumerate(self.pass_info[1:]):
            i = j[1]
            self.password[i[0]] = i[1]
            self.userIndex[i[0]].append(j[0]+1)
        return '1'

    def write_file(self):
        """
        write the state of model object (basic information list of users, users' password information, 
        the encrypted password of the administrator, and the list of recognised vaccines) into our file system.
        """
        FL = open("storage.txt", "w")
        for i in self.info:
            FL.write('[')
            for j in i:
                if isinstance(j, list):
                    FL.write('[')
                    for k in j:
                        FL.write("'" + str(k) + "'" + ',')
                    FL.write('],')
                else:
                    FL.write("'" + str(j) + "'" + ',')
            FL.write(']\n')
        FL.close()

        FL = open("password.txt", "w")
        for i in self.pass_info:
            FL.write('[')
            for j in i:
                FL.write("'" + str(j) + "'" + ',')
            FL.write(']\n')
        FL.close()

        FL = open("admin.txt", "w")
        FL.write(self.admin_password)
        FL.close()

        FL = open("vaccination.txt", "w")
        for i in self.rec_vac:
            FL.write(i+'\n')
        FL.close()