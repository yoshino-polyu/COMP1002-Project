# def main():
#     while True:
#         option = str(input("Choose C for using command line interface, choose G for useing graphic user interface"))
#         if option == 'G':
#             # GUI
#             return 0
#         elif option == 'C':
#             while True:
#                 # read all info from txt, and store it into storage.
#                 storage = dict()
#                 who = str(input("Input u to enter the user login page. Input a to enter the administrator login page. Input b to go back to the last menu."))
#                 if who == 'u':
#                     id = str(input("Please input your user id").split())
#                     password = str(input("Please input your password").split())
#                     # change password
#                     # 
#                 if who == 'a':
                    
                    
#                     break
#                 if who == 'b':
#                     break
#         else:
#             # try catch needed
#             return 0

info = []
def load_File():
    FL = open("storage.txt","r")
    for i in FL.readlines():
        print(i)
        info.append(eval(i))
    FL.close()

def print_File():
    ##FL = open("storage.txt","w")
    print('\n'.info)
    #for i in info:
        #st = ','.join(i)
        #print(st)
        ##FL.write(i)
    ##FL.close()

load_File()
for i in range(10):
    info.append(['POLYU FUCK U !!!!'])
print_File()
# f = open("test.txt", "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))
# f.close()

# q = open("test.txt", "a+")
# for i in range(5):
#     q.write("append line %d\r\n" % (i + 1 + 10))
# q.close()