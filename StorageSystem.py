import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import ast
#Notes FOR NOAH Ctrl + K + Z = Zen Mode


"""
READ THE 'readme.txt' FILE
ALWAYS KEEP THE 'creds.json' FILE OUTSIDE OF THE FOLDER

"""

scope = ["https://spreadsheets.google.com/feeds",
'https://www.googleapis.com/auth/spreadsheets',
"https://www.googleapis.com/auth/drive.file",
"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet1 = client.open("Utlaan Av Kamerautstyr").sheet1
datasheet1 = sheet1.get_all_records()
Datalength = len(datasheet1)

col1 = sheet1.col_values(1)
col2 = sheet1.col_values(2)
col3 = sheet1.col_values(3)
col4 = sheet1.col_values(4)
col5 = sheet1.col_values(5)
col6 = sheet1.col_values(6)
col7 = sheet1.col_values(7)
col8 = sheet1.col_values(8)
col9 = sheet1.col_values(9)
col10 = sheet1.col_values(10)

root = tk.Tk()
root.attributes("-fullscreen", True)

def DelUsernameEnt(*args):
    username_ent.delete(0, END)
    

def DelPasswordEnt(*args):
    password_ent.delete(0, END)
    

def DelNewUsernameEnt(*args):
    reg_username_ent.delete(0, END)
    
def DelNewPasswordEnt(*args):
    reg_password_ent.delete(0, END)

def DelNameEnt(*args):
    reg_Name_ent.delete(0,END)

def DelPhoneEnt(*args):
    reg_phoneN_ent.delete(0,END)

def removestr(inStorage):      #THIS FUNCTION REMOVES EMPTY STRINGS FROM A LIST
    while("" in inStorage):
        inStorage.remove("")

    """
    while("" in list):
        list.remove("THE STRING")
    """
#DELETE ENTRYBOX CONTENTS


def RegAcc():
    username_ent.grid_forget()
    password_ent.grid_forget()
    login_Btn.grid_forget()
    lend_item_btn.grid_forget()
    try:
        StorageMenu.grid_forget()
        NotInStorageMenu.grid_forget()

    except:
        pass


    reg_username_ent.bind("<Button-1>", DelNewUsernameEnt)
    reg_password_ent.bind("<Button-1>", DelNewPasswordEnt)
    reg_phoneN_ent.bind("<Button-1>", DelPhoneEnt)
    reg_Name_ent.bind("<Button-1>", DelNameEnt)


    reg_usernameString.set("Nytt Brukernavn")
    reg_passwordString.set("Nytt Passord")
    reg_NameString.set("Fullt Navn")
    reg_pnString.set("Telefonnummer")


    reg_username_ent.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)
    reg_password_ent.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)

    reg_Name_ent.grid(row=2, column=0, ipadx=5, ipady=5, padx=5, pady=5)
    reg_phoneN_ent.grid(row=3, column=0, ipadx=5, ipady=5, padx=5, pady=5)

    reg_btn.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, pady=5)

def RegUser():

    username = reg_username_ent.get()
    password = reg_password_ent.get()

    fname = reg_Name_ent.get()
    phone = reg_phoneN_ent.get()

    for name in range(1,len(col6)):
        if(str(username) == str(col6[name])): 
            #Checking if Username is in the database
            print("Name Already Exists!")
            break
    else:
        sheet1.update_cell(int(name) + 2 ,6,str(username))
        sheet1.update_cell(int(name) + 2 ,7 ,str(password))
        sheet1.update_cell(int(name) + 2, 1, str(fname))
        sheet1.update_cell(int(name) + 2, 2, str(phone))
        UserLogin()



def LoggedIn(username, password):
    
    global StorageMenu
    global NotInStorageMenu
    global lendItem
    global lentItem
    global inStorage
    global notInStorage
    print(username, password)

    root.attributes("-fullscreen", True)
    username_ent.grid_forget()
    password_ent.grid_forget()
    login_Btn.grid_forget()
    """Get the entire column into a list Then Creating a variable set to the first value 
    of that column 'PÅ LAGER' and then creating an optionmenu with that information"""


    inStorage = list(col8) 
    removestr(inStorage)
    lendItem = StringVar(root)
    lendItem.set(inStorage[0])
    StorageMenu = ttk.OptionMenu(root, lendItem, *inStorage)
    StorageMenu.grid(row=0, column=0, ipadx = 10, ipady=10, padx = 5)

    notInStorage = list(col9)
    removestr(notInStorage)
    lentItem = StringVar(root)
    lentItem.set(notInStorage[0])
    NotInStorageMenu = ttk.OptionMenu(root, lentItem, *notInStorage)
    NotInStorageMenu.grid(row=0, column=1, ipadx=10, ipady=10, padx=5)

    lend_item_btn.grid(row=0, column = 3, ipadx=10, ipady=3, padx=10, pady=10)

    
def LaanTing():
    print("LendITEM")
    """
    Get data from the database, then strip it of empty strings,
    then convert it into a list and add the next item to the list. 
    Thereafter insert the entire list into the cell, and find a way to unpack this when retreiving
    an item.
    """

    selected = lendItem.get()
    print(selected)

    for i in range(1, len(col6)):
        if(str(username) == str(col6[i])):
            contents = []
            try:
                alreadyLendt = col4[i]
                print(contents)
            except:
                contents = []
                print("contents: " + str(contents))

            finally:
                items = ""
                try:
                    contents.append(alreadyLendt + " " + selected)
                except:
                    contents.append(selected)

                for x in range(0,len(contents)):
                    items += str(contents[x])
                print(items)
                contents = items
                sheet1.update_cell(int(i) + 1, 4, str(contents))
                
                for y in range(1,len(col8)):
                    if(str(col8[y]) == str(selected)):
                        sheet1.update_cell(int(y) + 1, 8, "")
                        sheet1.update_cell(int(y) + 1, 9, selected)

def Retrieve():
    for i in range(1, len(col6)):
        if(str(username) == str(col6[i])):
            pass

def Checkuserinfo():
    #CREATE SOME LOGIC THAT COMPARE THE PASSWORDS AND USERNAMES TO THE DATABASE
    global username
    col6 = sheet1.col_values(6)
    col7 = sheet1.col_values(7)
    username = username_ent.get()

    for name in range(1,len(col6)):
        if(str(username) == str(col6[name])): 
            #Checking if Username is in the database
            username = col6[name]
            password = col7[name]
            
            if(username == username_ent.get() and password == password_ent.get()):
                #Sjekker om Username og passord == til Username og Passord I databasen                
                LoggedIn(username, password) #Runs The function that allows you to lend items
        else:
            pass       



def UserLogin():
    try:
        StorageMenu.grid_forget()
        NotInStorageMenu.grid_forget()
        
    except:
        """ MAKES IT POSSIBLE TO LOGIN WHILST IN THE PROGRAM """
        pass
    reg_username_ent.grid_forget()
    reg_password_ent.grid_forget()
    reg_phoneN_ent.grid_forget()
    reg_Name_ent.grid_forget()
    reg_btn.grid_forget()

    root.attributes("-fullscreen", True)
    login_Btn.grid(row=1, column=1, ipadx= 10, ipady=7, padx=5, pady=5, sticky="S")

    username_ent.grid(row=0, column=0, padx = 5, pady = 5, ipadx = 5, ipady = 5)
    password_ent.grid(row=1, column=0, padx = 5, pady = 5, ipadx = 5, ipady = 5)

    passwordString.set("Passord: ")
    usernameString.set("Brukernavn: ")

    username_ent.bind("<Button-1>", DelUsernameEnt)
    password_ent.bind("<Button-1>", DelPasswordEnt)
    


#DEFS ##############################



##### WIDGET REFERENCE ######

#STRINGVARS#
usernameString = StringVar()
passwordString = StringVar()

reg_usernameString = StringVar()
reg_passwordString = StringVar()
reg_NameString = StringVar()
reg_pnString = StringVar()

#STRINGVARS#

login_Btn = Button(root, text = "Login", command=Checkuserinfo, font=("Arial 32"))
username_ent = ttk.Entry(root, textvariable=usernameString,font=("Arial 32"))
password_ent = ttk.Entry(root, textvariable=passwordString, font=("Arial 32"))

reg_username_ent = ttk.Entry(root, textvariable=reg_usernameString,font=("Arial 32"))
reg_password_ent = ttk.Entry(root, textvariable=reg_passwordString, font=("Arial 32"))
reg_btn = Button(root, text = "Registrer", command=RegUser, font=("Arial 32"))

reg_Name_ent = ttk.Entry(root, textvariable=reg_NameString, font=("Arial 32"))
reg_phoneN_ent = ttk.Entry(root, textvariable=reg_pnString, font=("Arial 32"))

lend_item_btn = Button(root, text="Lån", command=LaanTing, font=("Arial 24"))
##### WIDGET REFERENCE ######

menubar = Menu(root)
root.config(menu=menubar)
root.config(background="grey")

MenuUserlogin = "Bruker Login"

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Registrer", command=RegAcc)
filemenu.add_command(label="Admin Login")
filemenu.add_command(label=str(MenuUserlogin), command=UserLogin)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Login", menu=filemenu)




root.mainloop()
