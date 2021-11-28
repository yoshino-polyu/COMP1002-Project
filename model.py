"""
The model 
    includes user information being represented, and will be acted upon latter. 
    determine the system state
"""
from io import TextIOWrapper
from os import TMP_MAX, error
import sys
from collections import defaultdict

class Model:

    NUM_FILES = 7
    
    def __init__(self):
        self.info = []   # [user id, last name, first name, department, number of injection,[injection info],'studentornot']
        self.pass_info = [] # [user id, password]
        self.rec_vac = [] # [the name of recognized vaccines, ... ]

        self.admin_password = '' # password of admin

        self.id = dict()
        self.nme = defaultdict(list)
        self.dpt = defaultdict(list)
        self.isInjected = defaultdict(list)
        self.isStu = defaultdict(list)
        self.userIndex = defaultdict(list)
        self.password = dict()


    def encode(self, p):
        """
        Motivation: When others access password.txt, they do not know what a particular user's password is.
        Encrypts the string (actual password) entered by the user and returns the encrypted string.
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
        self.nme[LAST + FIRST].append(temp)
        self.dpt[DEP].append(temp)
        self.isInjected[INJ_INFO[0]].append(temp)
        self.isStu[WHO].append(temp)
        self.userIndex[ID].append(len(self.info)-1)

        self.pass_info.append([ID, SEC])
        self.password[ID] = SEC
        self.userIndex[ID].append(len(self.pass_info)-1)

    
    def get_vaccines(self):
        
        return 0
    """
    Returns a current list (instance field) of regonized vaccines.
    Note: Only the vaccine recognized by HK gov is the vaccine that can be successfully written into the vaccine record.
    """
    
    def create_new_storage(self):
        print("Create a new storage file")
        FL = open("storage.txt","x")
        FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
        FL.close()
        """
        Transfer data into the system and writes the specified string to a file. 
        The string content is stored in the buffer until the file is closed or the buffer is flushed
        
        Returns:
        None
        """
    
    def update_admin(self, word : str):
        self.admin_password = word
        pass
    """
    updates the password of admin
    Param: word -> the new password of admin
    """

    def update_vacc(self, list_vacc : list):
        self.rec_vac = ['vaccination name'] + list_vacc
        pass
    """
    adds the newly recognised vaccines into existing recognised vaccines
    Param: list_vacc -> the newly recognised vaccines from admin
    """
    def wrong_file_storage(self):
        """ When an error occurs in the read data, a new file is generated. """
        s = input("Unexcepted information in storage file, create a new file? [y/n]")
        if (s == 'y' or s == 'Y'):
            self.info.clear()
            FL = open("storage.txt","w")
            FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
            FL.close()
            self.init()
        else:
            print('Program Exit')
            sys.exit()
        
        
    def load_file(self):
        """
        Open the TXT document and call create_new() if encounter a IOE error
        Try evall the stored personnel information and call wrong_file () if error occurs
        Check if it is a known type list and call wrong_file () if is not list
        When the length of info is not 7, the wrong_file() is invoked if the length is illegal.
        """
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
                    i[j[0]] = j[1].lower()
            self.info.append(i)
    """
    read lines for initialising self.info where all users' information is stored.
    """
    
    def create_new_password(self):
        print("create a new password file")
        FL = open("password.txt","x")
        FL.write("['user','password']\n")
        FL.close()


    def read_password(self):
        try:
            FL = open("password.txt", "r", encoding = "UTF-8")
        except FileNotFoundError:
            self.create_new_password()
            FL = open("password.txt", "r", encoding= 'UTF-8')
        finally:
            for i in FL.readlines():
                self.pass_info.append(eval(i))
            FL.close()
    """
    read lines for initialising self.pass_info where all users' passwords are stored.
    """
    def create_new_admin(self):
        print("create a new admin file")
        FL = open("admin.txt","x")
        FL.write(str(self.encode("admin")))
        FL.close()


    def read_admin(self):
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
        self.password[id] = new
        self.pass_info[self.userIndex[id][1]][1] = new
    
    def append_record(self, ID, record : list):
        x = self.info[self.userIndex[ID][0]]
        self.nme[x[1] + x[2]].remove(x)
        self.dpt[x[3]].remove(x)
        self.isInjected[x[4]].remove(x)
        self.isStu[x[6]].remove(x)
        x[4] = record[0]
        x[5] = record[1]
        self.id[x[0]] = x
        self.nme[x[1] + x[2]].append(x)
        self.dpt[x[3]].append(x)
        self.isInjected[x[4]].append(x)
        self.isStu[x[6]].append(x)
        return 0
    """
    appends the vaccination record to the end of vaccination information list
    """
    
    def create_new_vaccination(self):
        print("create a new vaccination file")
        FL = open("vaccination.txt","x")
        FL.write("'vaccination name'\n")
        FL.close()

    def read_vaccination(self):
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
        self.load_file()
        self.read_password()
        self.read_vaccination()
        self.read_admin()
        for j in enumerate(self.info[1:]):
            i = j[1]
            self.id[i[0]] = i
            self.nme[i[1] + i[2]].append(i)
            self.dpt[i[3]].append(i)
            self.isInjected[i[4]].append(i)
            self.isStu[i[6]].append(i)
            self.userIndex[i[0]].append(j[0]+1)
            #tmp = User()
        for j in enumerate(self.pass_info[1:]):
            i = j[1]
            self.password[i[0]] = i[1]
            self.userIndex[i[0]].append(j[0]+1)
        """
        Initialize the file and write the contents to the list
        """
    
    
    def write_file(self):
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
        """
        Store the read content in the middle of memory, write according to the format
        """