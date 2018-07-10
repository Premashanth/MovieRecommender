# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 21:53:50 2018

@author: Dinesh
"""
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
import webbrowser
import sqlite3
import importlib
from ScraperGUI import *


def signup(a,b):
    conn = sqlite3.connect('Auth.db')
    #conn.execute('''CREATE TABLE USER_DATA                     
    #            (ID VARCHAR PRIMARY KEY     NOT NULL,
    #            PASS           VARCHAR    NOT NULL);''')
    conn.execute("INSERT INTO USER_DATA VALUES (?,?)",(a,b))
    conn.commit()
    cursor = conn.execute("SELECT ID, PASS from USER_DATA")
    for row in cursor:
       print ("ID = ", row[0])
       print ("PASS = ", row[1])
    conn.close()
    
def login(a,b):
    conn = sqlite3.connect('Auth.db')
    conn.commit()
    cursor = conn.execute("SELECT * FROM USER_DATA WHERE ID = (?)",(a,))
    for row in cursor:
        if row[1]==b:   
            label = ttk.Label(frame1,text= "    Success            ",foreground="green").grid(column=1,row=4,sticky="W")
            win.quit()
            win.destroy()
            func1()
            #importlib.import_module("ScraperGUI") #importing scraper file
        elif row[1]!=b:   
            label = ttk.Label(frame1,text= "Wrong Password",foreground="red").grid(column=1,row=4,sticky="W")
    conn.close()
     

def quitt():
    win.quit()
    win.destroy()
    exit()
    
def help_page():
    url = 'help.html'
    webbrowser.open(url, new=2)    

def about_page():
    url='https://tryguys.github.io'
    webbrowser.open(url, new=2)    
    
win=tk.Tk()
win.title("Movie Recommeder")
win.minsize(width=600,height=400)

# Menu Bar
menu_bar=Menu()
win.config(menu=menu_bar)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Refresh Window")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quitt)
menu_bar.add_cascade(label="File",menu=file_menu)

help_menu=Menu(menu_bar,tearoff=0)
help_menu.add_command(label="Get Help Here",command=help_page)
menu_bar.add_cascade(label="Help",menu=help_menu)

about_menu=Menu(menu_bar,tearoff=0)
about_menu.add_command(label="Read Here",command=about_page)
menu_bar.add_cascade(label="About Us",menu=about_menu)


    
#Tab Interface
tabs=ttk.Notebook(win)

tab0=ttk.Frame(tabs)
tabs.add(tab0,text="Guest")

tab1=ttk.Frame(tabs)
tabs.add(tab1,text="Sign Up")

tab2=ttk.Frame(tabs)
tabs.add(tab2,text="Log In")

tabs.pack(expand=1,fill="both")

#Tab 1, Frame 1 SIGN UP
frame0=ttk.Labelframe(tab1,text="Enter following details:")
frame0.grid(padx=150,pady=100)
ttk.Label(frame0,text="Email ID").grid(column=0,row=0,sticky="W")
ttk.Label(frame0,text="Password").grid(column=0,row=1,sticky="W")
x0=ttk.Entry(frame0)
y0=ttk.Entry(frame0)
x0.grid(column=1,row=0)
y0.grid(column=1,row=1)

def get_val():
    signup(x0.get(),y0.get())

btn1=ttk.Button(frame0,text="Submit",command=get_val).grid(column=3,row=3)

#Tab 2,Frame 1 LOGIN
frame1=ttk.Labelframe(tab2,text="Enter login credentials")
frame1.grid(padx=150,pady=100)
ttk.Label(frame1,text="Email ID").grid(column=0,row=0,sticky="W")
ttk.Label(frame1,text="Password").grid(column=0,row=1,sticky="W")
x=ttk.Entry(frame1)
y=ttk.Entry(frame1)
x.grid(column=1,row=0)
y.grid(column=1,row=1)

def get_val1():
    login(x.get(),y.get())

btn1=ttk.Button(frame1,text="Submit",command=get_val1).grid(column=3,row=2)

#Tab 3,Frame 1 CHOOSING GENRE
genre=tk.StringVar()
frame2=ttk.Labelframe(tab0,text="Details")
frame2.grid(padx=150,pady=100,column=0,row=0)

#Frame 1, Box 1 GENRE 1
tempFrame=ttk.Label(frame2,text="Choose Genre 1").grid(column=0,row=0,sticky="W")
genre_list=ttk.Combobox(frame2,textvariable=genre)
genre_list['values']=('Action','Anime','Kids','Comedies','Documentaries','Dramas','Horror','Romance','Sci-Fi','Thriller')
genre_list.grid(column=1,row=0)
genre_list.current(0)

#Frame 1, Box 2 GENRE 2
genre=tk.StringVar()
tempFrame1=ttk.Label(frame2,text="Choose Genre 2").grid(column=0,row=1,sticky="W")
genre_list=ttk.Combobox(frame2,textvariable=genre)
genre_list['values']=('None','Action','Anime','Kids','Comedies','Documentaries','Dramas','Horror','Romance','Sci-Fi','Thriller')
genre_list.grid(column=1,row=1)
genre_list.current(0)

#Frame 1, Box 3 GENRE 3
genre=tk.StringVar()
tempFrame1=ttk.Label(frame2,text="Choose Genre 3").grid(column=0,row=2,sticky="W")
genre_list=ttk.Combobox(frame2,textvariable=genre)
genre_list['values']=('','None','Action','Anime','Kids','Comedies','Documentaries','Dramas','Horror','Romance','Sci-Fi','Thriller')
genre_list.grid(column=1,row=2)
genre_list.current(0)
#Adding Padding to all 3 Boxes
for lopper in frame2.winfo_children():
    lopper.grid_configure(padx=5,pady=3 )
for lopper in frame0.winfo_children():
    lopper.grid_configure(padx=5,pady=3 )
for lopper in frame1.winfo_children():
    lopper.grid_configure(padx=5,pady=3 )

btn1=ttk.Button(frame2,text="Enter").grid(column=3,row=3)

#Main GUI Call
win.mainloop()