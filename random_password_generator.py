import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
def low():
    entry.delete(0,END)
    length=var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get()==1:
        for i in range(0,length):
            password+=random.choice(lower)
        return password
    elif var.get()==0:
        for i in range(0,length):
            password+=random.choice(upper)
        return password
    elif var.get()==3:
        for i in range(0,length):
            password+=random.choice(digits)
        return password
    else:
        print("Please choose an options")
        

def generate():
    password1=low()
    entry.insert(10,password)
def copy1():
    random_pass=entry.get()
    pyperclip.copy(random_pass)

    
#GUI
root=Tk()
var=IntVar()
var1=IntVar()

root.title("Random Password Generator")

#Password
Random_password=Label(root,text="Password")
Random_password.grid(row=0)
entry=Entry(root)
entry.grid(row=0, column=1)

#Length
Password_length=Label(root,text="Length")
Password_length.grid(row=1)

#Copy Button
copy_button=Button(root,text="Copy",command=copy1) # copy1 is the function name
copy_button.grid(row=0,column=2)

#Generate Button
generate_button=Button(root,text="Generate",command=generate)
generate_button.grid(row=0,column=3)

#Radio Buttons for selecting the Strength of the password
radio_low=Radiobutton(root,text="Low",variable=var,value=1)
radio_low.grid(row=1,column=2,sticky='E')
radio_medium=Radiobutton(root,text="Medium",variable=var,value=0)
radio_medium.grid(row=1,column=3,sticky='E')
radio_high=Radiobutton(root,text="High",variable=var,value=3)
radio_high.grid(row=1,column=4,sticky='E')

#combo-box
combo = Combobox(root, textvariable=var1)
combo['values']=((8, 9, 10, 11, 12, 13, 14, 15, 16, 
                   17, 18, 19, 20, 21, 22, 23, 24, 25, 
                   26, 27, 28, 29, 30, 31, 32, "Length"))
combo.current(0)
combo.grid(row=1,column=1)
combo.bind('<<ComboboxSelected>>')
                 

root.mainloop()
