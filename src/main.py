from os import error
import sys
from collections import defaultdict
"""
a list to store the user information, 
user id, last name, first name, department, 
"""
info = []

id = defaultdict(list)
nme = defaultdict(list)
dpt = defaultdict(list)
isInjected = defaultdict(list)
isStu = defaultdict(list)
password = dict()

def create_New():
    print("Create new file")
    FL = open("storage.txt","x")
    FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
    FL.close()
    """
    Transfer data into the system and writes the specified string to a file. 
    The string content is stored in the buffer until the file is closed or the buffer is flushed
    
    Returns:
    None
    """

def wrongFile():
    s = input("Unexcepted information in storage file, create a new file? [y/n]")
    if(s == 'y' or s == 'Y'):
        info.clear()
        FL = open("storage.txt","w")
        FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
        FL.close()
        init()
    else:
        print('Program Exit')
        sys.exit()
    """
    When an error occurs in the read data, a new file is generated.
    
    Returns:
    None
    """
        

def load_File():
    try:
        FL = open("storage.txt","r", encoding='UTF-8')
    except FileNotFoundError:
        create_New()
        FL = open("storage.txt","r", encoding='UTF-8')
    for i in FL.readlines():
        try:
            eval(i)
        except Exception:
            FL.close()
            wrongFile()
            break
        if isinstance(eval(i), list) == 0:
            FL.close()
            wrongFile()
            break
        if(len(eval(i)) != 7):
            FL.close()
            wrongFile()
            break
        
        info.append(eval(i))
    FL.close()
    """
    Open the TXT document and call create_New() if encounter a IOE error
    Try evall the stored personnel information and call wrongFile () if error occurs
    Check if it is a known type list and call wrongFile () if is not list
    When the length of info is not 7, the wrongFile() is invoked if the length is illegal
    
      
    Returns:
    None
   
    Raises:
    Exception: An error occurred accessing the text.
    
    
    """

def print_File():
    FL = open("storage.txt","w")
    for i in info:
        FL.write('[')
        for j in i:
            if isinstance(j, list):
                FL.write('[')
                for k in j:
                    FL.write("'"+str(k)+"'"+',')
                FL.write('],')
            else:
                FL.write("'"+str(j)+"'"+',')
        FL.write(']\n')
    FL.close()
       
    """
    Store the read content in the middle of memory, write according to the format
    """

def read_password():
    FL = open("password.txt", "r", encoding= "UTF-8")
    for i in FL.readlines():
        tmp = eval(i)
        password[tmp[0]] = tmp[1]
        

def update_password():
    
def init():
    load_File()
    for i in info[1:]:
        id[i[0]].append(i)
        nme[i[1]+i[2]].append(i)
        dpt[i[3]].append(i)
        isInjected[i[4]].append(i)
        isStu[i[6]].append(i)
    """
    Initialize the file and write the contents to the list
    """



def main():
    read_password()
    init() # read all info from txt, and store it into storage.
    while True:
        option = str(input("Choose C for using command line interface, choose G for useing graphic user interface"))
        if option == 'G':
            # GUI
            return 0
        elif option == 'C':
            while True:
                who = str(input("Input u to enter the user login page. Input a to enter the administrator login page. Input b to go back to the last menu."))
                if who == 'u':
                    while True:
                        id = str(input("Please input your user id").split())
                        if id not in password:
                            print("id does not exist, please try again")
                            continue
                        secret = str(input("Please input your password").split())
                        if secret != password[id]:
                            print("Incorrect password, please try again")
                            continue
                        f_list = """
                        Please select a function you want to use:
                        a. change password
                        b. see current vaccination record
                        c. input vaccination information
                        """
                        print(f_list)
                        user_manner = str(input())
                        if user_manner == 'a':
                            print("Please enter the new password")
                            new_secret = str(input())
                            password[id] = new_secret
                            update_password()
                        elif user_manner == 'b':
                            
                        # change password
                        # 
                if who == 'a':
                    
                    
                    break
                if who == 'b':
                    break
        else:
            # try catch needed
            return 0

init()
for i in dpt['COMP']:
    print(i,type(i))

# f = open("test.txt", "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))
# f.close()

# q = open("test.txt", "a+")
# for i in range(5):
#     q.write("append line %d\r\n" % (i + 1 + 10))
# q.close()

