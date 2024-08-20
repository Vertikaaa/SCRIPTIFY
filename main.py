from tkinter import *
import tkinter as tk
import string
import random
import pyperclip


def generate() : 
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(length_Box.get())                                                        


    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))

    #password=random.sample(all,password_length)
    #password_Field.insert(0,password)
 
def copy():
    randompassword=passwordField.get()
    pyperclip.copy(randompassword)

root=tk.Tk()    #opens up a new window with the GUI but here it will execute really fast
root.config(bg='rosybrown4')
choice=IntVar()

frame = tk.Frame(root)
frame.grid(row=0, column=0)

Font =('Roboto',15,'bold')
 
passwordLabel = tk.Label(root, text='PASSWORD GENERATOR', font=('times new roman',20,'bold'),bg='white', fg='black') # just created a label hence nothing can be seen on the window
passwordLabel.grid(row=0, column=0, pady=5)

weakradioButton = Radiobutton(root, text='Weak', value=1, variable=choice, font=Font)
weakradioButton.grid(row=1, column=0, pady=5)
mediumradioButton = Radiobutton(root, text='Medium', value=2, variable=choice, font=Font)
mediumradioButton.grid(row=2, column=0, pady=5)

strongradioButton = Radiobutton(root, text='Strong', value=3 ,variable=choice, font=Font)
strongradioButton.grid(row=3, column=0, pady=5)

lengthLabel = Label(root, text='PASSWORD LENGTH', font=Font, bg='white', fg='black')  
lengthLabel.grid(pady=5)

length_Box=Spinbox(root, from_=5, to_=18, width=5, font=Font)
length_Box.grid(pady=5)

generateButton=Button(root, text='GENERATE PASSWORD', font=Font ,command=generate)
generateButton.grid(pady=5)

passwordField=Entry(root, width=25, bd=2, font=Font)
passwordField.grid()

copyButton=Button(root, text='copy', font=Font,command=copy)
copyButton.grid(pady=5)



root.mainloop()  # the screen holds up the window                                                                                                                                                                                                                                                  

