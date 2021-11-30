from typing import Tuple
from model import Model
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
from matplotlib import pyplot as plt

class GUIv:
    def __init__(self, model : Model) -> None: 
        self.model = model

    def main_page(self):
        global window_main
        window_main=Tk()
        window_main.geometry('500x500')
        button1 = Button(window_main, text = "User", font = ('Arial', 15), command = self.user_login_page)
        button2 = Button(window_main, text = "Administrator", font = ('Arial', 15), command = self.admin_login_page)
        button3 = Button(window_main, text = "Register", font = ('Arial', 15), command = self.register_page)
        button1.place(x = 90, y = 210)
        button2.place(x = 170, y = 210)
        button3.place(x = 320, y = 210)
        window_main.mainloop()

    def user_login_page(self):
        global window_login_user
        window_login_user = Tk()
        window_login_user.geometry('500x500')
        labelID = Label(window_login_user, text='netID  ', font=('Arial', 12), fg='grey', justify=RIGHT)
        labelID.place(x=65, y=120)
        labelPwd = Label(window_login_user, text='password  ', font=('Arial', 12), fg='grey', justify=RIGHT)
        labelPwd.place(x=50, y=160)
        global varID
        varID = StringVar(window_login_user, value='')
        global entryID
        entryID = Entry(window_login_user, textvariable=varID)
        entryID.place(x=120, y=124)
        global varPwd
        varPwd = StringVar(window_login_user, value='')
        global entryPwd
        entryPwd = Entry(window_login_user,show='*', textvariable=varPwd)
        entryPwd.place(x=120, y=164)
        res = 0
        buttonOk = Button(window_login_user, text='LOGIN', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command = lambda:self.log_in(res))
        buttonOk.place(x=65, y=200, width=200, height=30)
        if res == 1:
            self.user_page()
        window_login_user.mainloop()

    def admin_login_page(self):
        global window_login_admin
        window_login_admin= Tk()
        window_login_admin.title('1002')
        window_login_admin.geometry('500x500')
        labelPwd = Label(window_login_admin, text='passport  ', font=('Arial', 12), fg='grey', justify=RIGHT)
        labelPwd.place(x=50, y=160)
        global varPwd
        varPwd = StringVar(window_login_admin, value='')
        global entryPwd
        entryPwd = Entry(window_login_admin,show='*', textvariable=varPwd)
        entryPwd.place(x=120, y=164)
        global judge
        judge = -1
        buttonOk = Button(window_login_admin, text='LOGIN', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=lambda:self.log_in(judge))
        buttonOk.place(x=65, y=200, width=200, height=30)
        if judge == 1:
            self.admin_page()
        window_login_admin.mainloop()


    def register_page(self):
        global window_register
        window_register=Tk()
        window_register('1002')
        window_register.geometry('500x500')
        lambda:self.get_who()
        lambda:self.get_id()
        lambda:self.get_name()
        lambda:self.choose_dpt()
        window_register.mainloop()

    def user_page(self):
        global window_user
        window_user=Tk()
        button1 = Button(window_user, text = "Change Pass", font = ('Arial', 15), command = self.new_pass)
        button2 = Button(window_user, text = "User", font = ('Arial', 15), command = self.see_page)
        button3 = Button(window_user, text = "User", font = ('Arial', 15), command = self.update_page)
        button4 = Button(window_user, text = "User", font = ('Arial', 15), command = window_user.destroy)
        button1.place(x = 180, y = 50)
        button2.place(x = 180, y = 100)
        button3.place(x = 180, y = 150)
        button4.place(x = 180, y = 200)
        window_user.mainloop()

    def new_pass(self):
        global window_user_change
        window_user_change=Tk()
        window_login_user('1002')
        window_login_user.geometry('500x500')
        label =Label(window_user_change, text = "Please enter the password formed by 6 ~ 20 bits of numbers and letters: ")
        varpass = tk.StringVar(window_user_change, value='')
        entrypass = tk.Entry(window_user_change, textvariable=varpass)
        entrypass.place(x=120, y=124)
        a = entrypass.get()
        if(len(a) < 6 or len(a) > 20):
            messagebox.showerror(title='Warning', message="Password is too Short or too long, please ensure it only contains 6 ~ 20 bits of numbers or letters")
        for i in a:
            if (i.lower() > 'z' or i.lower() < 'a') and (i > '9' or i < '0'):
                messagebox.showerror(title='Warning', message="Password has unexpected characters, please ensure it only contains 6 ~ 20 bits of numbers or letters")
        window_user_change.mainloop()
        return a

    def see_page(self):
        global window_see
        window_see=Tk()

        window_see.mainloop()

    def update_page(self):
        global window_update
        window_update=Tk()
        self.update_record
        window_update.mainloop()

    def admin_page(self):
        global window_admin
        window_admin=Tk()
        button1 = Button(window_admin, text = "list out all information", font = ('Arial', 15), command = self.list_all_page)
        button2 = Button(window_admin, text = "list out all people who haven't been vaccinated", font = ('Arial', 15), command = self.list_unv_page)
        button3 = Button(window_admin, text = " displays the percentage", font = ('Arial', 15), command = self.display_page)
        button4 = Button(window_admin, text = "Change password", font = ('Arial', 15), command = self.admin_change_page)
        button5 = Button(window_admin, text = "Add new vaccination", font = ('Arial', 15), command = self.add_page)
        button6 = Button(window_admin, text = "Log out", font = ('Arial', 15), command = window_admin.destroy)
        button1.place(x = 180, y = 20)
        button2.place(x = 180, y = 50)
        button3.place(x = 180, y = 80)
        button4.place(x = 180, y = 110)
        button5.place(x = 180, y = 140)
        button6.place(x = 180, y = 170)
        window_admin.mainloop()

    def list_all_page(self):
        global window_list_all
        window_list_all = Tk()
        self.list_all()
        window_list_all.mainloop()

    def list_unv_page(self):
        global window_list_unv
        window_list_unv = Tk()
        
        window_list_unv.mainloop()

    def display_page(self):
        global window_display
        window_display=Tk()
        plt.figure(figsize=(6,9)) 
        labels = [u'Yes',u'No'] 
        sizes = [46,253] 
        colors = ['red','yellowgreen'] 
        explode = (0,0.05) 
        patches,text1,text2 = plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance = 1.2, autopct = '%3.2f%%', shadow = False, startangle =90, pctdistance = 0.6) 
        plt.axis('equal')
        plt.legend()
        plt.show()
        window_display.mainloop()

    def admin_change_page(self):
        global window_admin_change
        window_admin_change=Tk()

        window_admin_change.mainloop()

    def new_vacc(self):
        global window_add
        window_add=Tk()
        vac = self.model.rec_vac
        label1 = Label(window_add, text="Current recognised vaccines: ")
        for i in enumerate(vac[1:]):
            label2 = Label(window_add, text=str(i[0]+1)+". "+i[1])
        label3 = Label(window_add,text="----------------------")
        choose = {1: 'add a new recognised vaccines\n',2: 'delete one vaccines\n',3: 'quit\n'}
        dic={}
        for i in range(len(choose)):
            dic[i]=BooleanVar()
            Checkbutton(window_register, text=choose[i], variable=dic[i]).grid(row=i+2)
            if dic[i].get() == True:
                s = i
        s = input("1. add a new recognised vaccines\n2. delete one vaccines\n3. quit\n")
        if(s == '1'):
            label4=Label(window_register, text="Add Vaccination: ")
            varvacc = StringVar(window_register, value='')
            entryvacc = Entry(window_register,show='*', textvariable=varvacc)
            vac.append(entryvacc.get()).upper()
        elif (s == '2'):
            try:
                label5=Label(window_register, text="Delete Vaccination: ")
                varvacc = StringVar(window_register, value='')
                entryvacc = Entry(window_register,show='*', textvariable=varvacc)
                vac.remove(entryvacc.get()).upper()
            except Exception:
                messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        elif (s == '3'):
            window_add.destroy()
        else:
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        window_add.mainloop()
        return vac
       
    def creat_page(self):
            label=Label(window_register, text="Please input the vaccination record: (vaccination_day_month_year, example: AZ_01_09_2021)\n")
            varvac = tk.StringVar(window_register, value='')
            entryvac = tk.Entry(window_register,show='*', textvariable=varvac)
            rc = entryvac.get().upper()
            ck = rc.split('_')
            if(len(ck) != 4):
                messagebox.showerror(title='Warning', message='Invalid input, please try again!')
            ligal = 0
            for i in self.model.rec_vac[1: ]:
                if(i == ck[0]):
                    ligal = 1
            if(ligal == 0):
                messagebox.showerror(title='Warning', message='Invalid input, please try again!')
            record.append(rc)

    def log_in(self, x):        
        if x == 0:
            ID = entryID.get()
            pwd = self.model.encode(entryPwd.get())
            if ID in self.model.password and pwd == self.model.password[ID]:
                messagebox.showinfo(title = 'Congratulations', message='Login successfully!')
                x = 1
            else:
                messagebox.showerror(title='Warning', message='Your ID or passport is wrong')
                varID.set('')
                varPwd.set('')
        if x == -1:
            pwd = self.model.encode(entryPwd.get())
            if pwd == self.model.admin_password:
                messagebox.showinfo(title = 'Congratulations', message='Login successfully!')
                x = 1
            else:
                if pwd != self.model.password:
                    messagebox.showerror(title='Warning', message='Your ID or passport is wrong')
                    varID.set('')
                    varPwd.set('')
        return x
    
    def get_who(self):
        res=''
        who = {1: 'Student', 2: 'Stuff'}
        dic={}
        for i in range(len(who)):
            dic[i]=BooleanVar()
            Checkbutton(window_register, text=who[i], variable=dic[i]).grid(row=i+2)
            if dic[i].get() == True:
                res = who[i]
        return res

    def get_id(self):
        """
        gets a valid id from user.
        Note: a id is valid when it consists of 8 bits leading numbers and 1 bit of alphabet.
        """
        enums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        label=Label(window_register, text='pealse input your identity card number formed by 8 bits of number and 1 bit of alphabet.')
        label.pack()
        varid = StringVar(window_register, value='')
        entryid = Entry(window_register, textvariable=varid)
        entryid.place(x=120, y=124)
        id = entryid.get()
        if (len(id) != 9):
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        ok = 1
        for i, item in enumerate(id):
            if (i <= 7):
                if (item not in enums):
                    ok = 0
                    break
            elif (ord(item) < ord('a') or ord(item) > ord('z')):
                ok = 0
        if (ok == 0):
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        if (id in self.model.password):
            messagebox.showerror(title='Warning', message='ID is already exist, please try again.\n')
        return id    

    def get_name(self):
        """ read user name for registration purpose. """
        labelLast_Name = Label(window_register, text='Last Name  ', font=('Arial', 12), fg='grey', justify=tk.RIGHT)
        labelLast_Name.place(x=65, y=120)
        labelFirt_Name = Label(window_register, text='First Name  ', font=('Arial', 12), fg='grey', justify=tk.RIGHT)
        labelFirt_Name.place(x=50, y=160)
        global varlast
        varlast = StringVar(window_register, value='')
        global entrylast
        entrylast = Entry(window_register, textvariable=varlast)
        entrylast.place(x=120, y=124)
        global varfirst
        varfirst = StringVar(window_register, value='')
        global entryfirst
        entryfirst = Entry(window_register,show='*', textvariable=varPwd)
        entryfirst.place(x=120, y=164)
        last_n = entrylast.get()
        first_n = entryfirst.get()
        return [last_n.lower(), first_n.lower()]

    def choose_dpt(self):
        """ returns a string of department name with upper case """
        res = ""
        dpt = {1: 'AAE', 2: 'BME', 3: 'COMP', 4: 'EE', 5:'EIE', 6: 'ISE', 7: 'ME'}
        dic={}
        for i in range(len(dpt)):
            dic[i]=BooleanVar()
            Checkbutton(window_register, text=dpt[i], variable=dic[i]).grid(row=i+2)
            if dic[i].get() == True:
                res = dpt[i]
        return res

    def get_inj_info(self):
        """ returns number of injection and the vaccination information in the format of string. """
        labelinj = Label(window_register, text="Please input how many injections you have received: ")
        global varinj
        varinj = StringVar(window_register, value='')
        global entryinj
        entryinj = Entry(window_register, textvariable=varinj)
        entryinj.place(x=120, y=124)
        num_inj = entryinj.get()
        labelvac = Label(window_register, text="Below are some of the vaccines recognized by the Hong Kong government:")
        for i in enumerate(self.model.rec_vac[1:]):
                print(str(i[0])+'. '+i[1])
        global record
        record = []
        print("\nCurrent Record: \n")
        for i in enumerate(record):
            label1 = Label(window_register, text=str(i[0]+1)+'. '+i[1])
            label2 = Label(window_register, text="-------------------\n")
            dpt = {1: 'create a new record\n', 2: 'delete the last record\n', 3: 'stop editing\n'}
            dic={}
            for i in range(len(dpt)):
                dic[i]=BooleanVar()
                Checkbutton(window_register, text=dpt[i], variable=dic[i]).grid(row=i+2)
                if dic[i].get() == True:
                    res = dpt[i]
        s = input()
        if(res == '3'):
            window_register.destroy()
        elif(res == '1'):
            self.create_page()
        elif(s == '2'):
            if(len(record) > 0):
                record.pop()
        else:
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        return [num_inj,record]

    def list_all(self):
        for i in ['AAE', 'BME', 'COMP','EE', 'EIE', 'ISE', 'ME']:
            self.show_dep(i)

    def show_dep(self, dep):
        print("Department: "+dep.upper())
        cnt = 0
        vcnt = 0
        ncnt = 0
        if(dep.lower() not in self.model.dpt):
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
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
        if(cnt > 0):
            print(str(round(vcnt/cnt * 100,2))+"%"+" students/stuffs have been fully vaccinated")
            print(str(round(ncnt/cnt * 100,2))+"%"+" students/stuffs haven't been vaccinated")
        print("---------------------------------")

    def read_input(self):
        """ read input from user. """
        return str(input())

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



          


    
    