# # Written by Yunfei LIU  Nov 23, 2020"""
# def main():
#     print("Copyright 2020 Mu Yuan LI, Owen CHAN, Yun Fei LIU\nAll rights reserved.\n\n")
#     while True:
#         modeChar = str(input("Enter 'C' for command line mode, 'G' for GUI (Not developed yet), 'E' for exit: "))
#         if modeChar == 'E':
#             return 0
#         if modeChar == 'G':
#             print('Not developed yet!')
#             return 0
#         if modeChar == 'C':
#             while True:
#                 funcChar = str(input("\nEnter 'A' for advanced functions, 'B' for basic functions, 'R' for return to previous menu: "))
#                 if funcChar == 'R':
#                     break
#                 if funcChar == 'A':
#                     print("\n1.UserImpactIndex\n2.PostImpactIndex\n3.FriendshipIndex\n4.QuotationIndex\n5.FindKOL\n")
#                     choiceChar = str(input("Please enter numbers to use functions, other to return: "))
#                     if choiceChar == '1':
#                         userName = str(input("\nEnter the user name: "))
#                         print("The impact index for %s is %s\n" % (userName, UserImpactIndex(userName))) # This function calcuate a user's impact index. It receives a user name and return this user's impact index. For the algorithm, please refer to the report
#                     elif choiceChar == '2':
#                         post = str(input("\nEnter the post title: "))
#                         print("The impact index for %s is %s\n" % (post, PostImpactIndex(post))) # This function calculate the impact index of 
#                     elif choiceChar == '3':
#                         userName1 = str(input("\nEnter user name 1: "))
#                         userName2 = str(input("\nEnter user name 2: "))
#                         print("\nThe friendship index between %s and %s is %s" %(userName1,userName2,FriendshipIndex(userName1,userName2)))
#                     elif choiceChar == '4':
#                         userName1 = str(input("\nEnter user name 1: "))
#                         userName2 = str(input("\nEnter user name 2: "))
#                         print("\nThe quotation index between %s and %s is %s" %(userName1,userName2,QuotationIndex(userName1,userName2)))
#                     elif choiceChar == '5':
#                         miniIndex = float(input("Please enter the minimum index of KOL: "))
#                         percentage = float(input("Please enter the percentage of KOL: "))
#                         print("\nThe KOL list\n")
#                         for i in KOL(miniIndex,percentage):
#                             print("Name:%s\nImpact Index:%s\n" %(i[0],i[1]))

#                 if funcChar == 'B':
#                     print("1.Anchor\n2.DirectReport\n3.GetA\n4.GetU\n5.IsDirectSource\n6.IsSource\n7.IsFriend\n8.NicePrintA\n9.NicePrintU\n10.Report\n")
#                     choiceChar = str(input("Please enter numbers to use functions, other to return: "))
#                     if choiceChar == '1':
#                         continue
#                     elif choiceChar == '2':
#                         post = str(input("\nEnter the post title: "))
#                         reportList = DirectReport(post)
#                         print("Direct report of post '%s'"% post)
#                         for item in reportList:
#                             print(item)
#                     elif choiceChar == '3':
#                         GetA()
#                     elif choiceChar == '4':
#                         GetU()
#                     elif choiceChar == '5':
#                         post1 = str(input("\nEnter source title: "))
#                         post2 = str(input("\nEnter report title: "))
#                         print("%s is the direct source of %s ? "%(post1,post2),end='')
#                         print(IsDirectSource(post1,post2))
#                     elif choiceChar == '6':
#                         post1 = str(input("\nEnter source title: "))
#                         post2 = str(input("\nEnter report title: "))
#                         print("%s is the source of %s ? "%(post1,post2),end='')
#                         print(IsSource(post1,post2))
#                     elif choiceChar == '7':
#                         userName1 = str(input("\nEnter user name 1: "))
#                         userName2 = str(input("\nEnter user name 2: "))
#                         print("%s and %s are friends? "%(userName1,userName2),end = '')
#                         print(IsFriend(userName1,userName2))
#                     elif choiceChar == '8':
#                         post = str(input("\nEnter the post title: "))
#                         NicePrintA(post)
#                     elif choiceChar == '9':
#                         userName = str(input("\nEnter the user name: "))
#                         NicePrintU(userName)
#                     elif choiceChar == '10':
#                         post = str(input("\nEnter the post title: "))
#                         reportList = Report(post)
#                         print("Report of post '%s'"% post)
#                         for item in reportList:
#                             print(item)

# main()

import sys

info = []

id = dict()
nme = dict()
dpt = dict()
isInjected = dict()

def create_New():
    FL = open("storage.txt","x")
    FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
    FL.close()


def load_File():
    try:
        FL = open("storage.txt","r")
    except IOError:
        create_New()
        FL = open("storage.txt","r")
    for i in FL.readlines():
        print(i)
        info.append(eval(i))
    FL.close()

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

def init():
    load_File()
    for i in info:
        if(len(i) != 7):
            s = input("Unexcepted information in storage file, create a new file? [y/n]")
            if(s == 'y' or s == 'Y'):
                FL = open("storage.txt","w")
                FL.write("['ID','LAST NAME','FIRST NAME','DEPARTMENT','Number of Injection',['Injection Information',],'isStudent']\n")
                FL.close()
            else:
                print('Program Exit')
                sys.exit()
        i[0]



def main():
    while True:
        option = str(input("Choose C for using command line interface, choose G for useing graphic user interface"))
        if option == 'G':
            # GUI
            return 0
        elif option == 'C':
            while True:
                # read all info from txt, and store it into storage.
                storage = dict()
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
                
# f = open("test.txt", "w+")
# for i in range(10):
#     f.write("This is line %d\r\n" % (i + 1))
# f.close()

# q = open("test.txt", "a+")
# for i in range(5):
#     q.write("append line %d\r\n" % (i + 1 + 10))
# q.close()

