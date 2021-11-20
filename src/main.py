# Written by Yunfei LIU  Nov 23, 2020"""
def main():
    print("Copyright 2020 Mu Yuan LI, Owen CHAN, Yun Fei LIU\nAll rights reserved.\n\n")
    while True:
        modeChar = str(input("Enter 'C' for command line mode, 'G' for GUI (Not developed yet), 'E' for exit: "))
        if modeChar == 'E':
            return 0
        if modeChar == 'G':
            print('Not developed yet!')
            return 0
        if modeChar == 'C':
            while True:
                funcChar = str(input("\nEnter 'A' for advanced functions, 'B' for basic functions, 'R' for return to previous menu: "))
                if funcChar == 'R':
                    break
                if funcChar == 'A':
                    print("\n1.UserImpactIndex\n2.PostImpactIndex\n3.FriendshipIndex\n4.QuotationIndex\n5.FindKOL\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        userName = str(input("\nEnter the user name: "))
                        print("The impact index for %s is %s\n" %(userName,UserImpactIndex(userName)))
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        print("The impact index for %s is %s\n" %(post,PostImpactIndex(post)))
                    elif choiceChar == '3':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe friendship index between %s and %s is %s" %(userName1,userName2,FriendshipIndex(userName1,userName2)))
                    elif choiceChar == '4':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("\nThe quotation index between %s and %s is %s" %(userName1,userName2,QuotationIndex(userName1,userName2)))
                    elif choiceChar == '5':
                        miniIndex = float(input("Please enter the minimum index of KOL: "))
                        percentage = float(input("Please enter the percentage of KOL: "))
                        print("\nThe KOL list\n")
                        for i in KOL(miniIndex,percentage):
                            print("Name:%s\nImpact Index:%s\n" %(i[0],i[1]))

                if funcChar == 'B':
                    print("1.Anchor\n2.DirectReport\n3.GetA\n4.GetU\n5.IsDirectSource\n6.IsSource\n7.IsFriend\n8.NicePrintA\n9.NicePrintU\n10.Report\n")
                    choiceChar = str(input("Please enter numbers to use functions, other to return: "))
                    if choiceChar == '1':
                        continue
                    elif choiceChar == '2':
                        post = str(input("\nEnter the post title: "))
                        reportList = DirectReport(post)
                        print("Direct report of post '%s'"% post)
                        for item in reportList:
                            print(item)
                    elif choiceChar == '3':
                        GetA()
                    elif choiceChar == '4':
                        GetU()
                    elif choiceChar == '5':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the direct source of %s ? "%(post1,post2),end='')
                        print(IsDirectSource(post1,post2))
                    elif choiceChar == '6':
                        post1 = str(input("\nEnter source title: "))
                        post2 = str(input("\nEnter report title: "))
                        print("%s is the source of %s ? "%(post1,post2),end='')
                        print(IsSource(post1,post2))
                    elif choiceChar == '7':
                        userName1 = str(input("\nEnter user name 1: "))
                        userName2 = str(input("\nEnter user name 2: "))
                        print("%s and %s are friends? "%(userName1,userName2),end = '')
                        print(IsFriend(userName1,userName2))
                    elif choiceChar == '8':
                        post = str(input("\nEnter the post title: "))
                        NicePrintA(post)
                    elif choiceChar == '9':
                        userName = str(input("\nEnter the user name: "))
                        NicePrintU(userName)
                    elif choiceChar == '10':
                        post = str(input("\nEnter the post title: "))
                        reportList = Report(post)
                        print("Report of post '%s'"% post)
                        for item in reportList:
                            print(item)

main()
