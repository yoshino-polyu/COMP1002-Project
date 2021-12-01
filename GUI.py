from typing import Tuple
from model import Model
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import messagebox
#from matplotlib import pyplot as plt

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
        global ID
        ID=entryID.get()
        global varPwd
        varPwd = StringVar(window_login_user, value='')
        global entryPwd
        entryPwd = Entry(window_login_user,show='*', textvariable=varPwd)
        entryPwd.place(x=120, y=164)
        buttonOk = Button(window_login_user, text='LOGIN', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command = lambda:self.log_in_user())
        buttonOk.place(x=65, y=200, width=200, height=30)
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
        buttonOk = Button(window_login_admin, text='LOGIN', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=lambda:self.log_in_admin())
        buttonOk.place(x=65, y=200, width=200, height=30)
        window_login_admin.mainloop()

    def register_page(self):
        window_register=Tk()
        window_register.title('1002')
        window_register.geometry('500x500')
        button1 = Button(window_register, text = "Who", font = ('Arial', 15), command = lambda:self.get_who())
        button2 = Button(window_register, text = "ID", font = ('Arial', 15), command = lambda:self.get_id())
        button3 = Button(window_register, text = "Name", font = ('Arial', 15), command = lambda:self.get_name())
        button4 = Button(window_register, text = "Department", font = ('Arial', 15), command = lambda:self.choose_dpt())
        button1.place(x = 80, y = 210)
        button2.place(x = 160, y = 210)
        button3.place(x = 220, y = 210)
        button4.place(x = 320, y = 210)
        window_register.mainloop()

    def user_page(self):
        global window_user
        window_user=Tk()
        window_user.title('1002')
        window_user.geometry('500x500')
        button1 = Button(window_user, text = "Change Pass", font = ('Arial', 15), command = self.new_pass)
        button2 = Button(window_user, text = "See Record", font = ('Arial', 15), command = self.see_page)
        button3 = Button(window_user, text = "Update Record", font = ('Arial', 15), command = self.update_page)
        button4 = Button(window_user, text = "Log out", font = ('Arial', 15), command = window_user.destroy)
        button1.place(x = 180, y = 50)
        button2.place(x = 180, y = 100)
        button3.place(x = 180, y = 150)
        button4.place(x = 180, y = 200)
        window_user.mainloop()

    def new_pass(self):
        global window_user_change
        window_user_change=Tk()
        window_user_change.title('1002')
        window_user_change.geometry('500x500')
        label1=Label(window_user_change, text = "Please enter the password formed")
        label2=Label(window_user_change,  text= "by 6 ~ 20 bits of numbers and letters: ")
        label1.pack()
        label2.pack()
        varpass = StringVar(window_user_change, value='')
        entrypass = Entry(window_user_change, textvariable=varpass)
        entrypass.place(x=120, y=124)
        a = entrypass.get()
        if(len(a) < 6 or len(a) > 20):
            messagebox.showerror(title='Warning', message="Password is too Short or too long, please ensure it only contains 6 ~ 20 bits of numbers or letters")
        for i in a:
            if (i.lower() > 'z' or i.lower() < 'a') and (i > '9' or i < '0'):
                messagebox.showerror(title='Warning', message="Password has unexpected characters, please ensure it only contains 6 ~ 20 bits of numbers or letters")
        window_user_change.mainloop()
        self.model.update_password(ID, a)
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
        window_admin.title('1002')
        window_admin.geometry('500x500')
        button1 = Button(window_admin, text = "list out all information", font = ('Arial', 15), command = lambda:self.list_all_page)
        button2 = Button(window_admin, text = "list out all people who haven't been vaccinated", font = ('Arial', 15), command = lambda:self.list_unv_page)
        button3 = Button(window_admin, text = "Displays the percentage", font = ('Arial', 15), command = self.display_page)
        button4 = Button(window_admin, text = "Change password", font = ('Arial', 15), command = lambda:self.admin_change_page)
        button5 = Button(window_admin, text = "Add new vaccination", font = ('Arial', 15), command = self.new_vacc)
        button6 = Button(window_admin, text = "Log out", font = ('Arial', 15), command = window_admin.destroy)
        button1.place(x = 50, y = 20)
        button2.place(x = 50, y = 60)
        button3.place(x = 50, y = 100)
        button4.place(x = 50, y = 140)
        button5.place(x = 50, y = 180)
        button6.place(x = 50, y = 220)
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
        '''
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
        '''

    def admin_change_page(self):
        global window_admin_change
        window_admin_change=Tk()
        window_admin.geometry('500x500')

        window_admin_change.mainloop()

    def new_vacc(self):
        global window_add
        window_add=Tk()
        window_add.geometry('500x500')
        vac = self.model.rec_vac
        label1 = Label(window_add, text="Current recognised vaccines: ")
        label1.pack()
        for i in enumerate(vac[1:]):
            label2 = Label(window_add, text=str(i[0]+1)+". "+i[1])
            label2.pack()
        label3 = Label(window_add,text="----------------------")
        label3.pack()
        self.v4=IntVar()
        rb1 = Radiobutton(window_add, text = 'add a new recognised vaccines\n', bg =  "red", variable = self.v4, value = 1)
        rb2 = Radiobutton(window_add, text = 'delete one vaccines\n', bg =  "red", variable = self.v4, value = 2)
        rb3 = Radiobutton(window_add, text = 'quit\n', bg =  "red", variable = self.v4, value = 3)
        s = self.v4
        if(s == '1'):
            label4=Label(window_add, text="Add Vaccination: ")
            label4.pack()
            varvacc = StringVar(window_add, value='')
            entryvacc = Entry(window_add,show='*', textvariable=varvacc)
            entryvacc.pack()
            vac.append(entryvacc.get().upper())
        elif (s == '2'):
            try:
                label5=Label(window_add, text="Delete Vaccination: ")
                label5.pack()
                varvacc = StringVar(window_add, value='')
                entryvacc = Entry(window_add,show='*', textvariable=varvacc)
                entryvacc.pack()
                vac.remove(entryvacc.get().upper())
            except Exception:
                messagebox.showerror(title='Warning', message='Invalid input, please try again!')
        elif (s == '3'):
            window_add.destroy()
        window_add.mainloop()
        return vac

    def log_in_user(self):        
        ID = entryID.get()
        pwd = self.model.encode(entryPwd.get())
        if ID in self.model.password and pwd == self.model.password[ID]:
            messagebox.showinfo(title = 'Congratulations', message='Login successfully!')
            self.user_page()
        else:
            messagebox.showerror(title='Warning', message='Your ID or passport is wrong')
            varID.set('')
            varPwd.set('')
        
    def log_in_admin(self):
        pwd = self.model.encode(entryPwd.get())
        if pwd == self.model.admin_password:
            messagebox.showinfo(title = 'Congratulations', message='Login successfully!')
            self.admin_page()
        else:
            messagebox.showerror(title='Warning', message='Your ID or passport is wrong')
            varID.set('')
            varPwd.set('')
    
    def get_who(self):
        window_who =Tk()
        window_who.geometry('500x500')
        res=''
        v2 = IntVar()
        rbStudent = Radiobutton(window_who, text = "Student", bg = "red", variable = v2, value = 1)
        rbStuff = Radiobutton(window_who, text = "Stuff", bg = "red", variable = v2, value = 2)
        rbStudent.place(x=120, y=120)
        rbStuff.place(x=120, y=160)
        res = v2
        buttonOk = Button(window_who, text='OK', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=window_who.destroy)
        buttonOk.place(x=120, y = 220, width=200, height=30)
        return res

    def get_id(self):
        window_id =Tk()
        window_id.geometry('500x500')
        global enums
        enums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        label1=Label(window_id, text='please input your identity card number ')
        label2=Label(window_id, text='formed by 8 bits of number and 1 bit of alphabet.')
        label1.pack()
        label2.pack()
        varid = StringVar(window_id, value='')
        entryidr = Entry(window_id, textvariable=varid)
        entryidr.place(x=120, y=190)
        id = entryidr.get()
        buttonOk = Button(window_id, text='OK', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=lambda:self.id_get(id))
        buttonOk.place(x=120, y = 220, width=200, height=30)
        if judgement == 0:
            return id

    
    def id_get(self, x):
        global judgement
        judgement=0
        if (len(x) != 9):
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
            judgement=1
        ok = 1
        for i, item in enumerate(x):
            if (i <= 7):
                if (item not in enums):
                    ok = 0
                    break
            elif (ord(item) < ord('a') or ord(item) > ord('z')):
                ok = 0
        if (ok == 0):
            messagebox.showerror(title='Warning', message='Invalid input, please try again!')
            judgement=1
        if (x in self.model.password):
            messagebox.showerror(title='Warning', message='ID is already exist, please try again.\n')
            judgement=1
        return judgement    

    def get_name(self):
        """ read user name for registration purpose. """
        window_name=Tk()
        window_name.geometry('500x500')
        labelLast_Name = Label(window_name, text='Last Name  ', font=('Arial', 12), fg='grey', justify=tk.RIGHT)
        labelLast_Name.place(x=50, y=120)
        labelFirt_Name = Label(window_name, text='First Name  ', font=('Arial', 12), fg='grey', justify=tk.RIGHT)
        labelFirt_Name.place(x=45, y=160)
        varlast = StringVar(window_name, value='')
        entrylast = Entry(window_name, textvariable=varlast)
        entrylast.place(x=130, y=124)
        varfirst = StringVar(window_name, value='')
        entryfirst = Entry(window_name,show='*', textvariable=varfirst)
        entryfirst.place(x=130, y=164)
        last_n = entrylast.get()
        first_n = entryfirst.get()
        buttonOk = Button(window_name, text='OK', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=window_name.destroy)
        buttonOk.place(x=120, y = 220, width=200, height=30)
        return [last_n.lower(), first_n.lower()]

    def choose_dpt(self):
        """ returns a string of department name with upper case """
        window_dpt=Tk()
        window_dpt.geometry('500x500')
        res = ""
        self.v3 = IntVar()
        rbAAE = Radiobutton(window_dpt, text = "AAE", bg =  "red", variable = self.v3, value = 1)
        rbBME = Radiobutton(window_dpt, text = "BME", bg =  "red", variable = self.v3, value = 2)
        rbCOMP = Radiobutton(window_dpt, text = "COMP", bg =  "red", variable = self.v3, value = 3)
        rbEE = Radiobutton(window_dpt, text = "EE", bg =  "red", variable = self.v3, value = 4)
        rbEIE = Radiobutton(window_dpt, text = "EIE", bg =  "red", variable = self.v3, value = 5)
        rbISE = Radiobutton(window_dpt, text = "ISE", bg =  "red", variable = self.v3, value = 6)
        rbME = Radiobutton(window_dpt, text = "ME", bg =  "red", variable = self.v3, value = 7)
        rbAAE.place(x=120,y=20)
        rbBME.place(x=120,y=60)
        rbCOMP.place(x=120,y=100)
        rbEE.place(x=120,y=140)
        rbEIE.place(x=120,y=180)
        rbISE.place(x=120,y=220)
        rbME.place(x=120,y=260)
        res = self.v3   
        buttonOk = Button(window_dpt, text='OK', bg='#%02x%02x%02x' %(5, 187, 251), fg='white', relief='flat', command=window_dpt.destroy)
        buttonOk.place(x=120, y = 300, width=200, height=30)   
        return res

    def get_inj_info(self):
        """ returns number of injection and the vaccination information in the format of string. """
        window_inj=Tk()
        window_inj.geometry('1000x1000')
        labelinj = Label(window_inj, text="Please input how many injections you have received: ")
        labelinj.pack()
        global varinj
        varinj = StringVar(window_inj, value='')
        global entryinj
        entryinj = Entry(window_inj, textvariable=varinj)
        entryinj.place(x=120, y=124)
        num_inj = entryinj.get()
        labelvac = Label(window_inj, text="Below are some of the vaccines recognized by the Hong Kong government:")
        for i in enumerate(self.model.rec_vac[1:]):
            labelx = Label(window_inj, text=str(i[0]+1)+'. '+i[1])
        record = []
        labely=Lael(window_inj, text="\nCurrent Record: \n")
        for i in enumerate(record):
            label1 = Label(window_inj, text=str(i[0]+1)+'. '+i[1])
        label2 = Label(window_inj, text="-------------------\n")
        self.v5 = IntVar()
        rbinj1 = Radiobutton(window_inj, text = 'create a new record\n', bg =  "yellow", variable = self.v5, value = 1)
        rbinj2 = Radiobutton(window_inj, text = 'delete the last record\n', bg =  "yellow", variable = self.v5, value = 2)
        rbinj3 = Radiobutton(window_inj, text = 'stop editing\n', bg =  "yellow", variable = self.v5, value = 3)
        s = self.v5
        if(s == '3'):
            window_inj.destroy()
        elif(s == '1'):
            self.create_page()
            label3=Label(window_add, text="Please input the vaccination record: (vaccination_day_month_year, example: AZ_01_09_2021)\n")
            varvac = tk.StringVar(window_add, value='')
            entryvac = tk.Entry(window_add,show='*', textvariable=varvac)
            entryvac.pack()
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



          


    
    