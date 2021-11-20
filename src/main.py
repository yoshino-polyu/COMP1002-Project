from os import error
import sys
"""
a list to store the user information, 
user id, last name, first name, department, 
"""
info = []

id = dict()
nme = dict()
dpt = dict()
isInjected = dict()
isStu = dict()

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
        FL = open("storage.txt","r")
    except FileNotFoundError:
        create_New()
        FL = open("storage.txt","r")
    for i in FL.readlines():
        try:
            eval(i)
        except Exception:
            FL.close()
            wrongFile()
            break
        if isinstance(i, list) == 0:
            FL.close()
            wrongFile()
            break
        if(len(i) != 7):
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


def init():
    load_File()
    for i in info[1:]:
        id[i[0]] = i
        nme[i[1]+i[2]] = i
        dpt[i[3]] = i
        isInjected[i[4]] = i
        isStu[i[6]] = i
    """
    Initialize the file and write the contents to the list
    """



def main():
    init()
    while True:
        option = str(input("Choose C for using command line interface, choose G for useing graphic user interface"))
        if option == 'G':
            # GUI
            return 0
        elif option == 'C':
            while True:
                # read all info from txt, and store it into storage.
                who = str(input("Input u to enter the user login page. Input a to enter the administrator login page. Input b to go back to the last menu."))
                if who == 'u':
                    id = str(input("Please input your user id").split())
                    password = str(input("Please input your password").split())
                    
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

# f = open("test.txt", "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))
# f.close()

# q = open("test.txt", "a+")
# for i in range(5):
#     q.write("append line %d\r\n" % (i + 1 + 10))
# q.close()

