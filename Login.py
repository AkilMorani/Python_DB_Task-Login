#!/usr/bin/env python
# coding: utf-8

# In[1]:


import  sqlite3
conn=sqlite3.connect("student.db")
print("Database created successfully")


# In[3]:


conn.execute("""
CREATE TABLE IF NOT EXISTS ADMIN(
ADMIN_ID INTEGER PRIMARY KEY NOT NULL ,
USERNAME TEXT NOT NULL, 
PASSWORD TEXT NOT NULL)
""")
print ("Table ADMIN created successfully")


# In[4]:


conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'admin')");

conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('scott', 'tiger')");

conn.commit()
print ("Records inserted successfully")


# In[14]:


cursor = conn.execute("SELECT * from ADMIN")
print("ID\tUSERNAME\tPASSWORD")
for row in cursor:
   print ("{}\t{}\t\t{}".format(row[0],row[1],row[2]))
conn.close()


# In[16]:


from tkinter import *

def login():
    uname=username.get()
    pwd=password.get()

    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      
      conn = sqlite3.connect('student.db')
      
      cursor = conn.execute('SELECT * from ADMIN where USERNAME="%s" and PASSWORD="%s"'%(uname,pwd))
       
      if cursor.fetchone():
       message.set("Login successful.")
      else:
       message.set("Wrong username or password!!!")

def Loginform():
    global login_screen
    login_screen = Tk()
    
    login_screen.title("Login Window")
    
    login_screen.geometry("350x250")
    login_screen["bg"]="#1C2833"
    
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    
    Label(login_screen,width="300", text="Login Form", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    
    Label(login_screen, text="Username * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    
    Entry(login_screen, textvariable=username,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    
    Label(login_screen, text="Password * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    
    Entry(login_screen, textvariable=password ,show="*",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    
    Label(login_screen, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    
    Button(login_screen, text="Login", width=10, height=1, command=login, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=170)
    login_screen.mainloop()
    
Loginform()


# In[ ]:




