#!/usr/bin/env python
# coding: utf-8

# In[34]:


import sqlite3
conn=sqlite3.connect("contacts.db")
print("Database created successfully")


# In[35]:


conn.execute("""
CREATE TABLE IF NOT EXISTS CONTACTS(
ID INTEGER PRIMARY KEY NOT NULL ,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
GENDER TEXT,
ADDR TEXT NOT NULL,
C_NO TEXT NOT NULL)
""")
print ("Table CONTACTS created successfully")


# In[36]:


conn.execute("INSERT INTO CONTACTS(FIRSTNAME,LASTNAME,GENDER,ADDR,C_NO) VALUES ('XYZ', 'ABC', 'FEMALE', '01 ABC DR.', 0123456789)");

conn.execute("INSERT INTO CONTACTS(FIRSTNAME,LASTNAME,ADDR,C_NO) VALUES ('PQR', 'UVW', '01 XYZ DR.', 0123456789)");

conn.commit()
print ("Records inserted successfully")


# In[41]:


cursor = conn.execute("SELECT * from CONTACTS")
print("ID\tFIRSTNAME\tLASTNAME\tGENDER\tADDR\t\tC_NO")
for row in cursor:
    print ("{}\t{}\t\t{}\t\t{}\t{}\t{}".format(row[0],row[1],row[2],row[3],row[4],row[5]))
conn.close()


# In[38]:


from tkinter import *

def Insert():
    Fname=firstname.get()
    Lname=lastname.get()
    Gender=gender.get()
    Addr=addr.get()
    C_no=c_no.get()

    if Fname=='' or Lname=='' or Gender=='' or Addr=='' or C_no=='':
        message.set("fill the empty field!!!")
    else:
      
        conn = sqlite3.connect('contacts.db')
      
        conn.execute('INSERT INTO CONTACTS(FIRSTNAME,LASTNAME,GENDER,ADDR,C_NO) VALUES ("%s","%s","%s", "%s","%s")'%(Fname,Lname,Gender,Addr,C_no))
      
        conn.commit() 
        
        message.set("Data insertion is successful.")
    
        if cursor.rowcount:
           message.set("Data insertion is successful.")
        else:
           message.set("Error in Insertion.")
    
    conn.close()

def form():
    global Insert_screen
    Insert_screen = Tk()
    
    Insert_screen.title("Contacts Window")
    
    Insert_screen.geometry("450x350")
    Insert_screen["bg"]="#1C2833"
    
    global  message;
    global firstname, lastname, gender, addr, c_no
    
    firstname = StringVar()
    lastname = StringVar()
    gender = StringVar()
    addr = StringVar()
    c_no = StringVar()
    message=StringVar()
    
    Label(Insert_screen,width="400", text="Data Insert Form", bg="#0E6655",fg="white",font=("Arial",12,"bold")).pack()
    
    Label(Insert_screen, text="First_name * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=40)
    
    Entry(Insert_screen, textvariable=firstname,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=42)
    
    Label(Insert_screen, text="Last_name * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=80)
    
    Entry(Insert_screen, textvariable=lastname,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=82)
    
    Label(Insert_screen, text="gender * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=120)
    
    Entry(Insert_screen, textvariable=gender,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=122)
    
    Label(Insert_screen, text="Address * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=160)
    
    Entry(Insert_screen, textvariable=addr,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=162)
    
    Label(Insert_screen, text="Contact No. * ",bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=20,y=200)
    
    Entry(Insert_screen, textvariable=c_no,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=120,y=202)
    
    Button(Insert_screen, text="Add", width=10, height=1, command=Insert, bg="#0E6655",fg="white",font=("Arial",12,"bold")).place(x=125,y=250)
    Insert_screen.mainloop()
    
form()


# In[ ]:





# In[ ]:




