#lets start the project 

    
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import tkinter
import time
import os
import tkinter.filedialog as simpledialog
import datetime
import pymysql



class window1:



    def __init__(self,root):

        self.root=root
        self.root.title("Welcome To Futsal Management System")
        self.root.geometry("1600x900+0+0")
        self.root.config(bg="red")
        self.root.iconbitmap("futsal.ico")
        self.bg_icon2 = ImageTk.PhotoImage(Image.open("football.png"))
        ##########################################   

        
        
        ###frames
        frame1 = Frame(self.root,bg="pink",relief= GROOVE,borderwidth=5)
        frame1.place(x= 420,y = 200,width = 600, height= 500)
        #####################################################################
        logo1= Label(frame1,image=self.bg_icon2)
        logo1.place(x=180,y=20)


        btm_login1=Button(frame1,text="Admin",width=20,command=self.new_window2,font=("times new roman",20,"bold"),bg="orange",fg="black")
        btm_login1.place(x=145,y=300)
        btm_login2=Button(frame1,text="Users",width=20,command=self.new_window3,font=("times new roman",20,"bold"),bg="orange",fg="black")
        btm_login2.place(x=145,y=360)
        btm_login3=Button(frame1,text="National Player",command=self.new_window,width=20,font=("times new roman",20,"bold"),bg="orange",fg="black")
        btm_login3.place(x=145,y=420)
       
        self.ss= "Welcome To Futsal Management System"
        self.count = 0
        self.text = ' '
        self.SliderLabel = Label(self.root,text=self.ss,font=('helvetica',30,'bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
        self.SliderLabel.place(x= 390,y= 0)
        self.tick2()
        

        

        ########################################clock time  


        self.clock = Label(self.root,font=('times',14,'bold'),relief=RIDGE,borderwidth=5,width=20,bg='lawn green')
        self.clock.place(x=0,y= 0)
        self.tick1()

    def tick1(self):
        
    
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        self.clock.config(text="Date :"+ date_string+ "\n"+"Time :"+time_string)

        self.clock.after(1,self.tick1)   

    def tick2(self):

            
        self.count, self.text
        if(self.count>=len(self.ss)):

            self.count= 0
            self.text = ' '
            self.SliderLabel.config(text=self.text)
        else:

            self.text=self.text+self.ss[self.count]  
            self.SliderLabel.config(text=self.text)
            self.count +=  1

        self.SliderLabel.after(200,self.tick2)       


    def new_window2(self):
        self.new_window1 = Toplevel(self.root)
        self.obj = admin_login(self.new_window1)

    def new_window3(self):
        self.new_window3 = Toplevel(self.root)
        self.obj = team_register(self.new_window3)

    def new_window(self):
        self.new_window12= Toplevel(self.root)
        self.obj = national_player(self.new_window12)  


class national_player:
    def __init__(self,root):
        self.root=root
        self.root.title("Information of yours:")
        self.root.geometry("1600x900")
        self.root.config(bg="white")
        self.root.iconbitmap("futsal.ico")
        ########################################## 

        #########################
        self.bg_icon2 = ImageTk.PhotoImage(Image.open("nepal.jpg"))
        logo1 = Label(self.root,image=self.bg_icon2)
        logo1.place(x=450,y=0)
        ##########################
        #adding login frame of national player:
        frame1=Frame(self.root,relief=GROOVE,bg="pink")
        frame1.place(x=450,y=480,height=300,width=640)
        #national player login and editing page:
        title=Label(frame1,text="National Players",font=("times new roman",15,"bold"),bd=4,relief=GROOVE,bg="yellow",fg="blue")
        title.place(x=0,y=0,relwidth=1)
        bt1=Button(frame1,text="Login as National Player",command=self.National_player,font=('Arial',15,'bold'),fg="black",bg="gold2")
        bt1.place(x=150,y=80,width=300)
        bt12=Button(frame1,text="Exit",command=self.Exit,font=('Arial',15,'bold'),fg="black",bg="gold2")
        bt12.place(x=150,y=140,width=300)
    def Exit(self):
        
        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):

            self.root.destroy()    

    def National_player(self):
        
        self.new_window21 = Toplevel(self.root)
        self.obj = national(self.new_window21) 
class national:
    def __init__ (self,root):
        self.root=root
        self.root.title("National Player Register:")
        self.root.geometry("1600x900")
        self.root.config(bg="gold2")
        self.root.iconbitmap("futsal.ico")
        ###########################################
        self.Name = StringVar()
        self.ID = StringVar()
        frame10=Frame(self.root,bg='blue',bd=5,relief=GROOVE)
        frame10.place(x=400,y=50,width=700,height=700)
        label1=Label(frame10,text="Player Name:",font=('times',18,'bold'),bg='yellow',fg='black')
        label1.place(x=60,y=100)
        label2=Label(frame10,text="Player ID:",font=('times',18,'bold'),bg='yellow',fg='black')
        label2.place(x=60,y=200)
        entry1=Entry(frame10,font=("times",18,"bold"),textvariable=self.Name,relief=GROOVE)
        entry1.place(x=300,y=100)
        entry2=Entry(frame10,font=("times",18,"bold"),textvariable=self.ID,relief=GROOVE)
        entry2.place(x=300,y=200)
        btn2=Button(frame10,text="Login",command=self.login,font=('Times',18,'bold'),bg='yellow',fg="black")
        btn2.place(x=100,y=500,width=200)
        btn3=Button(frame10,text="Exit",command=self.Exit,font=('Times',18,'bold'),bg='yellow',fg="black")
        btn3.place(x=350,y=500,width=200)


    def login(self):

        if self.Name.get()=="" or self.ID.get()=="":
    

    
            messagebox.showerror("Error!","Player Name or Password Error!!!!",parent=self.root)


        else:

            try:

                con=pymysql.connect(host="localhost",user="root",password="",database="admin_login3")
                cur=con.cursor()
                cur.execute( "select Name, ID from national_player where Name = %s and ID=%s" ,(self.Name.get(),
                                                                                                self.ID.get()))
                row=cur.fetchone()
                if row==None:

                    messagebox.showerror("Error!!","Invalid Player Name and Id",parent=self.root)
                    self.clear()
                   
                elif row:


                    
                    self.new_window2 = Toplevel(self.root)

                    self.obj = national_player_tools(self.new_window2) 
                    self.clear()



                 
            
            except Exception as es:
                messagebox.showerror("Error!!",f"Error Due to: {str(es)}",parent=self.root)
                self.clear()

    def clear(self):
        (
            self.Name.set(''),
            self.ID.set('')
        )              

    def new_window2(self):

         
        self.new_window2 = Toplevel(self.root)

        self.obj = national_player_tools(self.new_window2)

            

    def Exit(self):
    
        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):

            self.root.destroy()

class national_player_tools:
    def __init__ (self,root):
        self.root=root
        self.root.title("National Player Information window:")
        self.root.geometry("1600x900")
        self.root.config(bg="gold2")
        frame1 = Frame(self.root,bg="green",relief= GROOVE,borderwidth=5)
        frame1.place(x=0,y = 0,width = 500, height= 800)
        frame2 = Frame(self.root,bg="pink",relief= GROOVE,borderwidth=5)
        frame2.place(x=550,y = 0,width = 950, height= 800)
        frame3 = Frame(frame1,bg="green",relief= GROOVE)
        frame3.place(x=0,y = 730,width =500, height= 55)

        
        NameLabel=Label(frame1,text="Player Name:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel.place(x=6,y=30)
        NameLabel2=Label(frame1,text="Player ID:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel2.place(x=6,y=120)
        NameLabel5=Label(frame1,text="Player Email:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel5.place(x=6,y=210)
        NameLabel3=Label(frame1,text="Player Strategy:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel3.place(x=6,y=300)
        NameLabel4=Label(frame1,text="Blood Group:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel4.place(x=6,y=390)
        NameLabel5=Label(frame1,text="Visited Date:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel5.place(x=6,y=480)
        NameLabel6=Label(frame1,text="Rate Futsal:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel6.place(x=6,y=570)
        ################variable
        self.Name = StringVar()
        self.Id = StringVar()
        self.Email = StringVar()
        self.Strategy = StringVar()
        self.Blood_Group = StringVar()
        self.visited_Date = StringVar()
        self.rate = StringVar()


        name1 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Name)
        name1.place(x=250,y=30)
        name2 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Id)
        name2.place(x=250,y=120)
        name5 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Email)
        name5.place(x=250,y=210)
        combo_all1=ttk.Combobox(frame1,width=15,font=("times new roman",15,"bold"),textvariable=self.Strategy,state='readonly')
        combo_all1['values']=(' Attack', 
						' Defense', 
						' Forward', 
						' Winger', 
						' Mid-Player', 
						' Defense', 
						' Mid-Defense', 
						' Goal-Keeper', 
						' Substitute', 
						' Sweeper', 
						' Striker', 
						' Central Midfield')
        combo_all1.place(x=250,y=300,width=215)
        combo_all2=ttk.Combobox(frame1,width=15,font=("times new roman",15,"bold"),textvariable=self.Blood_Group,state='readonly')
        combo_all2['values']=(' A+' ,'A-','B+','B-','O+','O-','AB+','AB-')
        
        combo_all2.place(x=250,y=390,width=215)
        name6 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.visited_Date)
        name6.place(x=250,y=480)
        combo_all3=ttk.Combobox(frame1,width=15,font=("times new roman",15,"bold"),textvariable=self.rate,state='readonly')
        combo_all3['values']=('*****','****','***','**','*','soory')
        combo_all3.place(x=250,y=570,width=215)

        bt1=Button(frame3,text="Submit",font=("arial",16,"bold"),command=self.submit2,width=8,bg="gold2",fg="black",borderwidth=3)
        bt1.place(x=0,y=0)
        bt2=Button(frame3,text="Update",font=("arial",16,"bold"),width=8,bg="gold2",command=self.update,fg="black",borderwidth=3)
        bt2.place(x=120,y=0)
        bt3=Button(frame3,text="Exit",font=("arial",16,"bold"),command=self.Exit,width=8,bg="gold2",fg="black",borderwidth=3)
        bt3.place(x=360,y=0)
        bt2=Button(frame3,text="Clear",command=self.clear,font=("arial",16,"bold"),width=8,bg="gold2",fg="black",borderwidth=3)
        bt2.place(x=240,y=0)
        ######################################
        label_frame=Frame(frame2,bd=4,relief=RIDGE,bg="crimson")
        label_frame.place(x=50,y=100,height=600,width=900)

        scroll_x=Scrollbar(label_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(label_frame,orient=VERTICAL)

        self.staff_table=ttk.Treeview(label_frame,columns=("Player_Name","Player_Id","Email","Strategy","Blood_Group","Visited_Date","Rate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)


        self.staff_table.heading("Player_Name",text="Player_Name")
        self.staff_table.heading("Player_Id",text="Player_Id")
        self.staff_table.heading("Email",text="Email")

        self.staff_table.heading("Strategy",text="Strategy")
        self.staff_table.heading("Blood_Group",text="Blood_Group")
        self.staff_table.heading("Visited_Date",text="Visited_Date")
        self.staff_table.heading("Rate",text="Rate")

        self.staff_table['show']='headings'
        self.staff_table.column("Player_Name",width=200) 
        self.staff_table.column("Email",width=250)
        self.staff_table.pack(fill=BOTH,expand=1)
        self.staff_table.bind("<ButtonRelease->",self.get_cursor)
        self.fetch_data()
        self.clear()


    def submit2(self):


    

        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("insert into national_player_info values(%s,%s,%s,%s,%s,%s,%s)",(self.Name.get(),
                                                                     self.Id.get(),
                                                                     self.Email.get(),
                                                                     self.Strategy.get(),
                                                                     self.Blood_Group.get(),
                                                                     self.visited_Date.get(),
                                                                     self.rate.get()
                                                                     
                                                                     
                                                                   
                                                                
                                                                     
                                                                   
        
                                                                    ))
                                                           

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def update(self):
        
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("update national_player_info set ID=%s,email=%s,strategy=%s,blood_group=%s,visited_date = %s,rate = %s where Name=%s",(
                                                                     self.Id.get(),
                                                                     self.Email.get(),
                                                                     self.Strategy.get(),
                                                                     self.Blood_Group.get(),
                                                                     self.visited_Date.get(),
                                                                     self.rate.get(),
                                                                     self.Name.get()
                                                                         

                                                                            ))   
        
        con.commit()
        self.fetch_data()  
        self.clear()
        con.close()                                                                      

    def fetch_data(self):
        
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from national_player_info")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close() 

    def Exit(self):

            self.root.destroy() 


    def clear(self):

        (self.Name.set(""),
            self.Id.set(""),
            self.Email.set(""),
            self.Strategy.set(""),
            self.Blood_Group.set(""),
            self.visited_Date.set(""),
            self.rate.set("")
        )   
    def get_cursor(self,ev):
        curosor_row=self.staff_table.focus()
        contents=self.staff_table.item(curosor_row)  
        row=contents['values']   
        self.Name.set(row[0]),
        self.Id.set(row[1]),
        self.Email.set(row[2]),
        self.Strategy.set(row[3]),
        self.Blood_Group.set(row[4]),
        self.visited_Date.set(row[5]),
        self.rate.set(row[6])


       


###########################################################################
class admin_login:
    
    def __init__(self,root):

        self.root=root
        self.root.title("Admin Login")
        self.root.geometry("1600x900")
        self.root.config(bg="white")
        self.root.iconbitmap("admin1.ico")



        #for image
        self.bg_icon1 = ImageTk.PhotoImage(Image.open("background.jpg.png"))
       

        #variables::::::
        self.Admin_Name = StringVar()
        self.password=StringVar()

        title=Label(self.root,text="Admin Login",font=("times new roman",40,"bold"),bd=10,relief=GROOVE,bg="yellow",fg="red")
        title.place(x=0,y=0,relwidth=1)
        


        login_frame=Frame(self.root,bg="orange")
        login_frame.place(x=550,y=150)


        logo = Label(login_frame,image=self.bg_icon1).grid(row=0,columnspan=2,pady=20)



        lbluser=Label(login_frame,text="Admin Name",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="red").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(login_frame,bd=5,textvariable=self.Admin_Name, relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=10)


        lbluser=Label(login_frame,text="Password",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="red").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(login_frame,bd=5,textvariable=self.password, relief=GROOVE,show="*",font=("",15)).grid(row=2,column=1,padx=10)



        btm_login=Button(login_frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="red",command=self.login,fg="blue").grid(row=3,column=0,padx=12,pady=10)


        btm_login=Button(login_frame,text="Exit",command=self.Exit,width=15,font=("times new roman",14,"bold"),bg="red",fg="blue").grid(row=3,column=1,padx=16,pady=10)




    
    def login(self):
        


        #get the data and store it into the tuple!
        
        if self.password.get()=="" or self.Admin_Name.get()=="":

            messagebox.showerror("Error!","Admin Name or Password Error!!!!",parent=self.root)


            
        else: 
            try:

                con=pymysql.connect(host="localhost",user="root",password="",database="admin_login3")
                cur=con.cursor()
                cur.execute( "select * from admin3 where Admin_Name= %s and password=%s" ,(self.Admin_Name.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error!!","Invalid Admin Name and Password",parent=self.root)
                    self.clear()
                elif row:


                   self.new_window2 = Toplevel(self.root)

                   self.obj = admin_tools(self.new_window2) 
                   self.clear() 
            
            except Exception as es:
                messagebox.showerror("Error!!",f"Error Due to: {str(es)}",parent=self.root)
                self.clear()


            
      

 


    def Exit(self):

        self.root.destroy()

        
    def clear(self):

        (self.Admin_Name.set(""),
        self.password.set(""),
            
        ) 


    def new_window2(self):
        self.new_window2 = Toplevel(self.root)
        self.obj = admin_tools(self.new_window2)

#for next window 

class admin_tools:
    
    def __init__(self,root):
                                      
                                      
        #here is the code of amdin panel
        self.root=root
        self.root.title("Admin control Place")
        self.root.geometry("1920x1080")
        self.root.config(bg="gold2")
        self.root.iconbitmap("admin1.ico")

        frame2 = Frame(root,bg = "blue",relief=SUNKEN,borderwidth=5)
        frame2.place(x= 170,y = 50,width=1200, height=750)







        #here we will give the data entry 
    

        frontlevel = Label(frame2,text="...........Welcome Admin............",font=("arial",20,"bold",),relief=GROOVE,borderwidth=4,bg="white",fg="red")
        frontlevel.place(x=380,y=10)
        but1=Button(frame2,text="Staff",width=25,font=('times new roman',18,"bold"),command=self.staff,relief=SUNKEN,borderwidth=4,bg="red",)
        but1.place(x=400,y=90)
        but2=Button(frame2,text="Booking History",width=25,font=('times new roman',18,"bold"),command=self.Booking_history,relief=SUNKEN,borderwidth=4,bg="red",)
        but2.place(x=400,y=170)
        but3=Button(frame2,text="Team history",width=25,font=('times new roman',18,"bold"),relief=SUNKEN,command=self.team_history,borderwidth=4,bg="red",)
        but3.place(x=400,y=250)
        but6=Button(frame2,text="Time Shedule",width=25,font=('times new roman',18,"bold"),relief=SUNKEN,borderwidth=4,command=self.time_schedule,bg="red",)
        but6.place(x=400,y=330)
        but6=Button(frame2,text="Add Admin",width=25,command=self.add_admin,font=('times new roman',18,"bold"),relief=SUNKEN,borderwidth=4,bg="red")
        but6.place(x=400,y=410)
        but7=Button(frame2,text="Stopwatch",width=25,font=('times new roman',18,"bold"),command=self.stopwatch,relief=SUNKEN,borderwidth=4,bg="red")
        but7.place(x=400,y=490)
        but8=Button(frame2,text="Add National Player",width=25,font=('times new roman',18,"bold"),command=self.national_player1 ,relief=SUNKEN,borderwidth=4,bg="red")
        but8.place(x=400,y=570)

       
        but9=Button(frame2,text="Exit",width=25,font=('times new roman',18,"bold"),relief=SUNKEN,borderwidth=4,command=self.Exit,bg="red",)
        but9.place(x=400,y=650)
    def national_player1(self):
        self.new_window56 = Toplevel(self.root)
        self.obj = national_player1(self.new_window56)


    def staff(self):
        self.new_window2 = Toplevel(self.root)
        self.obj = staff_records(self.new_window2)


    
    def stopwatch(self):
        self.new_window245 = Toplevel(self.root)
        self.obj = stopwatch(self.new_window245)
        




    def time_schedule(self):
        self.new_window21 = Toplevel(self.root)
        self.obj = time_schedule(self.new_window21)
        

    def Booking_history(self):
        self.new_window21 = Toplevel(self.root)
        self.obj = booking_history(self.new_window21)


    def team_history(self):
        self.new_window76 = Toplevel(self.root)
        self.obj = team_history(self.new_window76)
        




    def add_admin(self):
        self.new_window25 = Toplevel(self.root)
        self.obj = add_admin(self.new_window25)


       
          

    def Exit(self):

        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):

            self.root.destroy()

class national_player1:
    def __init__(self,root):
        self.root=root
        self.root.title("History of the national Football and Futsal Players")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.root.iconbitmap("futsal.ico")
        ########################################## 

        #########################
        self.bg_icon2 = ImageTk.PhotoImage(Image.open("messi.jpg"))
        logo1 = Label(self.root,image=self.bg_icon2)
        logo1.place(x=450,y=100)
        ##########################
        #adding login frame of national player:
        frame1=Frame(self.root,relief=GROOVE,bg="pink",borderwidth=4)
        frame1.place(x=450,y=480,height=300,width=570)
        #national player login and editing page:
        title=Label(frame1,text="National Players",font=("times new roman",15,"bold"),bd=4,relief=GROOVE,bg="yellow",fg="blue")
        title.place(x=0,y=0,relwidth=1)
        bt1=Button(frame1,text="Add National Players",command=self.new_window1,font=('Arial',15,'bold'),fg="black",bg="red")
        bt1.place(x=150,y=80,width=300)
        bt2=Button(frame1,text="Exit",font=('Arial',15,'bold'),command=self.exit,fg="black",bg="red")
        bt2.place(x=150,y=150,width=300)

    def new_window1(self):

        self.new_window2= Toplevel(self.root)
        self.obj = national_player_login(self.new_window2)

    def exit(self):
        self.root.destroy()
       

class national_player_login:
                                  
    def __init__(self,root):

        self.root=root
        self.root.title("National Player")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.root.iconbitmap("admin1.ico")
        frame2=Frame(root,bg="pink")
        frame2.place(x=300,y=60,height=700,width=1000)
        ####here is the login frame of all the data that are required to fill
        ########Add staff labels#################################
        NameLabel=Label(frame2,text="Player Name",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel.place(x=10,y=10)
        NameLabel2=Label(frame2,text="Player ID",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel2.place(x=10,y=80)
        NameLabel5=Label(frame2,text="Gender",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel5.place(x=10,y=150)

        NameLabel3=Label(frame2,text="Player Contact",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel3.place(x=10,y=220)
        NameLabel4=Label(frame2,text="Player Address",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel4.place(x=10,y=290)
        NameLabel6=Label(frame2,text="Player Nationality",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel6.place(x=10,y=360)




        #####variable
        self.Name=StringVar()
        self.ID=StringVar()
        self.gender=StringVar()
        self.Contact=StringVar()
        self.Address=StringVar()
        self.Nationality=StringVar()
    
        

        ##################staff entry box##########
        
        name1 = Entry(frame2,font=('Arial',15,'bold'),bd=5,textvariable=self.Name)
        name1.place(x=250,y=10)
        name2 = Entry(frame2,font=('Arial',15,'bold'),bd=5,textvariable=self.ID)
        name2.place(x=250,y=80)
        combo_all1=ttk.Combobox(frame2,width=15,font=("Arial",15,"bold"),textvariable=self.gender,state='readonly')
        combo_all1['values']=("Male","Female","Others")
        combo_all1.place(x=250,y=150,width=240)
        name3 = Entry(frame2,font=('Arial',15,'bold'),bd=5,textvariable=self.Contact)
        name3.place(x=250,y=220)
        name4 = Entry(frame2,font=('Arial',15,'bold'),bd=5,textvariable=self.Address)
        name4.place(x=250,y=290)
        name4 = Entry(frame2,font=('Arial',15,'bold'),bd=5,textvariable=self.Nationality)
        name4.place(x=250,y=360)

       
        btn5=Button(frame2,text="Submit",command=self.upload,font=("arial",22,"bold"),bg="red",fg="black",relief=GROOVE,borderwidth=2)
        btn5.place(x=40,y=630,width=150)
        btn6=Button(frame2,text="Exit",command=self.Exit,font=("arial",22,"bold"),bg="red",fg="black",relief=GROOVE,borderwidth=2)
        btn6.place(x=300,y=630,width=150)
        


    def Exit(self):

    

        self.root.destroy() 


    def upload(self):
        if self.Name.get()=="" or self.ID.get()=="" or self.gender.get()=="" or self.Contact.get()=="" or self.Address.get()==""or self.Nationality.get()=="":
            
            messagebox.showerror("Error!!!!","Please fill all the form",parent=self.root)
            


    
        else:


            try:


                con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
                cur=con.cursor()
                cur.execute("insert into national_player values(%s,%s,%s,%s,%s,%s)",(self.Name.get(),
                                                                        self.ID.get(),
                                                                        self.gender.get(),
                                                                        self.Contact.get(),
                                                                        self.Address.get(),
                                                                        self.Nationality.get()
                                                                    
                                                                     
                                                        
                                                                     
                                                                     
                                                                   
                                                                
                                                                     
                                                                   
        
                                                                    ))

                messagebox.showinfo("succesfully","Succesfully register as National player",parent=self.root)
               
                con.commit()
                self.clear()
                
                con.close()
                

             
            except Exception as es:
                messagebox.showerror("Error!!","Error due to Name and Id ",parent=self.root)
                self.clear()

                                                           

                
          


           
    def clear(self):
        (
            self.Name.set(""),
        self.ID.set(""),
        self.gender.set(""),
        self.Contact.set(""),
        self.Address.set(""),
        self.Nationality.set("")
            
            
            


        )


















class stopwatch:
    def __init__(self, master):

        self.master = master
        self.master.attributes("-topmost", 0)
        self.master.title("Futsal Stopwatch")
        self._job = None

        self.runningTime = StringVar()

        self.toggleString = StringVar()
        self.toggleString1 = StringVar()

        self.runningTime.set("00-00-00")
        self.toggleString.set("Start")
        self.toggleString1.set("Exit")
        self.isPaused = True
        self.secondsPast = 0

        self.master.geometry("1600x900")
        self.master.config(bg="gold2")
        self.master.resizable(True, True)
        master.protocol("WM_DELETE_WINDOW", self.onclosing)
        master.update()

        self.timeLabel = Label(
            master, textvariable=self.runningTime, font=("Times New Roman", 40)
        )
        self.timeLabel.grid(row=0, column=1)
        self.timeLabel.place(x=630,y=50,width=300,height=200)

        self.toggleButton = Button(
            master, textvariable=self.toggleString, command=self.toggle, relief="raised",font=("times",30,"bold"),bg="red",fg="Black"
        )
        self.toggleButton.place(x=700,y=300,width=150)

        self.toggleButton1 = Button(
            master, textvariable=self.toggleString1, command=self.toggle1, relief="raised",font=("times",30,"bold"),bg="red",fg="Black"
        )
        self.toggleButton1.place(x=700,y=500,width=150)


        self.menubar = Menu(master)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open History", command=self.viewhistory)
        self.filemenu.add_command(label="Change Title", command=self.changetitle)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.master.config(menu=self.menubar)

    def toggle(self):
        with open("history.txt", "a") as historyTXT:
            if self.toggleString.get() == "Start":
                historyTXT.write(time.strftime("%Y:%m:%d\t%H:%M:%S") + "\tStarted\n")
                self.start()
            elif self.toggleString.get() == "Pause":
                historyTXT.write(
                    time.strftime("%Y:%m:%d\t%H:%M:%S")
                    + "\tPaused at: "
                    + self.runningTime.get()
                    + "\n"
                )
                self.pause()
            elif self.toggleString.get() == "Unpause":
                historyTXT.write(
                    time.strftime("%Y:%m:%d\t%H:%M:%S")
                    + "\tUnpaused at: "
                    + self.runningTime.get()
                    + "\n"
                )
                self.unpause()

    def toggle1(self):
        self.master.destroy()            

    def increment(self):
        if self.isPaused == False:
            self.secondsPast += 1
            self.runningTime.set(
                time.strftime("%H:%M:%S", time.gmtime(self.secondsPast))
            )
        self._job = self.master.after(1000, self.increment)

    def start(self):
        self.toggleString.set("Pause")
        self.toggleButton.configure(relief="raised")
        self.isPaused = False
        self.increment()

    def pause(self):
        self.toggleString.set("Unpause")
        self.toggleButton.configure(relief="sunken")
        self.isPaused = True

    def unpause(self):
        self.toggleString.set("Pause")
        self.toggleButton.configure(relief="raised")
        self.isPaused = False

    def viewhistory(self):
        self.historyWin = Toplevel()
        self.historyScroll = Scrollbar(self.historyWin)
        self.historyText = Text(self.historyWin, height=50, width=100)

        self.historyScroll.pack(side=LEFT, fill=Y)
        self.historyText.pack(side=RIGHT, fill=Y)

        self.historyScroll.config(command=self.historyText.yview)
        self.historyText.config(yscrollcommand=self.historyScroll.set)

        with open("history.txt", "r") as historyTXT:
            self.historyText.insert(END, historyTXT.read())

    def changetitle(self):
        if self._job is not None:
            self.master.after_cancel(self._job)
            self._job = None
            with open("history.txt", "a") as historyTXT:
                historyTXT.write("\tSTOPPED\t\n")
        self.answer = simpledialog.askstring("Input", "Set Window Title")
        with open("history.txt", "a") as historyTXT:
            if self.answer is not None:
                self.master.title(self.answer)
                historyTXT.write(
                    "\t"
                    + self.answer
                    + "\t"
                    + time.strftime("%Y:%m:%d\t%H:%M:%S")
                    + "\t\n"
                )
            else:
                self.master.title("Simple Stopwatch")
                historyTXT.write("\t" + time.strftime("%Y:%m:%d\t%H:%M:%S") + "\t\n")

        self.runningTime.set("00-00-00")
        self.toggleString.set("Start")
        self.isPaused = True
        self.secondsPast = 0

    def onclosing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?",parent=self.master):
            with open("history.txt", "a") as historyTXT:
                historyTXT.write("\tSTOPPED\t\n")
            self.master.destroy()            

class booking_history:
    

    def __init__ (self,root):
        

        self.root=root
        self.root.title("Booking History")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        label_frame=Frame(root,bd=4,relief=RIDGE,bg="white")
        label_frame.place(x=300,y=50,height=600,width=900)
    

        scroll_x=Scrollbar(label_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(label_frame,orient=VERTICAL)
        
   


        self.staff_table=ttk.Treeview(label_frame,columns=("Team_Name","Team_Id","court_no","Date","Day","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)


        self.staff_table.heading("Team_Name",text="Team_Name")
        self.staff_table.heading("Team_Id",text="Team_Id")
        self.staff_table.heading("court_no",text="Court_no")
        self.staff_table.heading("Date",text="Date")
        self.staff_table.heading("Day",text="Day")
       

      


        self.staff_table.heading("Time",text="Time")
       
        self.staff_table.pack(fill=BOTH,expand=1)

        self.staff_table['show']='headings'
    
        self.fetch_data()
        
    def fetch_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from booking2")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close()

 





class team_history:
    def __init__(self,root):

    
        self.root=root
        self.root.title("Team History")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.search_by = StringVar()
        self.search_txt = StringVar()

        label_frame=Frame(root,bd=4,relief=RIDGE,bg="white")
        label_frame.place(x=300,y=50,height=600,width=900)
        frame1=Frame(root,bg="gold2",relief=GROOVE)
        frame1.place(x=300,y=650,height=100,width=900)

        scroll_x=Scrollbar(label_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(label_frame,orient=VERTICAL)
        
        label12=Label(frame1,text="Search By",bg="crimson",fg="white",font=("times new romans",15,"bold"))
        label12.place(x=25,y=40)

        combo_all=ttk.Combobox(frame1,width=15,font=("times new roman",15,"bold"),textvariable=self.search_by,state='readonly')
        combo_all['values']=("Id")
        combo_all.place(x=130,y=40)

        name11 = Entry(frame1,font=('times new roman',15,'bold'),textvariable=self.search_txt,bd=5,relief=GROOVE)
        name11.place(x=350,y=40)

        btn11=Button(frame1,text="Search",width=8,font=("times new roman",15,"bold"),bg="white",fg="black",command=self.search_data)
        btn11.place(x=640,y=40)

        btn11=Button(frame1,text="Show All",width=8,font=("times new roman",15,"bold"),bg="white",fg="black",command=self.fetch_data)
        btn11.place(x=800,y=40)

        self.staff_table=ttk.Treeview(label_frame,columns=("Team_Name","Team_Id","Player_Name","Captain_contact","Captain_Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)


        self.staff_table.heading("Team_Name",text="Team_Name")
        self.staff_table.heading("Team_Id",text="Team_Id")
        self.staff_table.heading("Player_Name",text="Players_Name")
       

      


        self.staff_table.heading("Captain_contact",text="Captain_Contact")
        self.staff_table.heading("Captain_Address",text="Captain_Address")
        self.staff_table.pack(fill=BOTH,expand=1)

        self.staff_table['show']='headings'
    
        self.fetch_data()
        
    def fetch_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from users_form")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close()

    def search_data(self):

        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        my_cursor=con.cursor()

        selected = self.search_by.get()
        


        if selected =="Id":#"Staff_ID","Staff_contact"
            sql = "select * from users_form where Id=%s"  

        
        searched = self.search_txt.get()
        result=my_cursor.execute(sql,searched)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close()     









class add_admin:


    def __init__(self,root):

        self.root=root
        self.root.title("Add Admin")
        self.root.geometry("1600x900")
        self.root.config(bg="pink")
        self.root.iconbitmap("users.ico")

        self.Admin_Name=StringVar()
        self.password=StringVar()

        frame1=Frame(root,relief=GROOVE,borderwidth=3,bg="blue")
        frame1.place(x=400,y=50,height=700,width=700)
        lbl1=Label(root,text="Add Multiple Admin",bg="red",font=("Arial",16,"bold"),fg="black",relief=SUNKEN)
        lbl1.place(x=400,y=20)
        lbl2=Label(frame1,text="New Admin Name:",bg="Gold2",fg="black",font=("Arial",18,"bold"))
        lbl2.place(x=60,y=230)
        lbl3=Label(frame1,text="New Admin Password:",bg="Gold2",fg="black",font=("Arial",18,"bold"))
        lbl3.place(x=60,y=330)
        ent1=Entry(frame1,relief=GROOVE,textvariable=self.Admin_Name,font=("Times",18,"bold"))
        ent1.place(x=350,y=230)
        ent2=Entry(frame1,relief=GROOVE,textvariable=self.password,font=("Times",18,"bold"))
        ent2.place(x=350,y=330)
        btn1=Button(frame1,text="Add Admin",bg="red",fg="black",command=self.add_admin,font=("Times",18,"bold"))
        btn1.place(x=100,y=620)
        btn2=Button(frame1,text="Cancel",bg="red",command=self.cancel,fg="black",font=("Times",18,"bold"))

        btn2.place(x=400,y=620)

    def add_admin(self):


        if self.Admin_Name.get()=="" or self.password.get()=="":



    
            messagebox.showerror("Error!","Admin Name or Password Error!!!!",parent=self.root)


            
        else:

            try:


                con=pymysql.connect(host="localhost",user="root",password="",database="admin_login3")
                cur=con.cursor()
                log=cur.execute("insert into admin3 values(%s,%s)",(self.Admin_Name.get(),
                                                                            self.password.get()))
                messagebox.showinfo("Successfully","New Admin is Added",parent=self.root) 
                self.clear()                                                           



                con.commit()   
                con.close()
            except Exception as es:
                messagebox.showerror("Error!!","Admin Name and password already taken",parent=self.root)
                self.clear()  

    def clear(self):
        self.Admin_Name.set('')
        self.password.set('')             

    def cancel(self):


        self.root.destroy() 


                                                                                     

            

                
        




class time_schedule:

    def __init__(self,root):
        
        self.root=root
        self.root.title("Time Schedule For Match")
        self.root.geometry("1600x900")
        self.root.config(bg="pink")
        frame1 = Frame(self.root,bg="blue",relief= GROOVE,borderwidth=5)
        frame1.place(x=0,y = 0,width = 500, height= 800)
        frame2 = Frame(self.root,bg="yellow",relief= GROOVE,borderwidth=5)
        frame2.place(x=550,y = 0,width = 950, height= 800)
        frame3 = Frame(frame1,bg="white",relief= GROOVE)
        frame3.place(x=0,y = 735,width =500, height= 55)

        ##########variables:
        self.teamname=StringVar()
        self.contact=StringVar()
        self.time= StringVar()
        self.field = StringVar()
        self.Staff_ID = StringVar()
        NameLabel=Label(frame1,text="Team Name:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel.place(x=10,y=50)
        NameLabel2=Label(frame1,text="Captain Contact:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel2.place(x=10,y=140)
        NameLabel5=Label(frame1,text="Time Duration:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel5.place(x=10,y=230)
        NameLabel3=Label(frame1,text="Field No:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel3.place(x=10,y=320)
        NameLabel4=Label(frame1,text="Staff ID:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel4.place(x=10,y=410)
        NameLabel6=Label(frame1,text="Available Time:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel6.place(x=10,y=500)
        


        name1 = Entry(frame1,font=('roman',15,'bold'),textvariable=self.teamname,bd=5)
        name1.place(x=250,y=50)
        name2 = Entry(frame1,font=('roman',15,'bold'),textvariable=self.contact,bd=5)
        name2.place(x=250,y=140)
        name5 = Entry(frame1,font=('roman',15,'bold'),textvariable=self.time,bd=5)
        name5.place(x=250,y=230)
        name3 = Entry(frame1,font=('roman',15,'bold'),textvariable=self.field,bd=5)
        name3.place(x=250,y=320)
        name4 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Staff_ID)
        name4.place(x=250,y=410)
        self.txt_time=Text(frame1,bd=5,width=20,height=4,relief=GROOVE,font=("",15))
        self.txt_time.place(x=250,y=500)
        bt1=Button(frame3,text="Submit",font=("arial",16,"bold"),width=8,command=self.submit2,bg="gold2",fg="black",borderwidth=3)
        bt1.place(x=0,y=0)
        bt2=Button(frame3,text="Update",font=("arial",16,"bold"),command=self.update,width=8,bg="gold2",fg="black",borderwidth=3)
        bt2.place(x=120,y=0)
        bt3=Button(frame3,text="Exit",font=("arial",16,"bold"),command=self.Exit,width=8,bg="gold2",fg="black",borderwidth=3)
        bt3.place(x=360,y=0)
        bt2=Button(frame3,text="Clear",font=("arial",16,"bold"),command=self.clear,width=8,bg="gold2",fg="black",borderwidth=3)
        bt2.place(x=240,y=0)
        label_frame1=Frame(frame2,bd=4,relief=RIDGE,bg="crimson")
        label_frame1.place(x=50,y=100,height=600,width=900)

        scroll_x=Scrollbar(label_frame1,orient=HORIZONTAL)
        scroll_y=Scrollbar(label_frame1,orient=VERTICAL)

        self.admin_table=ttk.Treeview(label_frame1,columns=("Team Name","Captain Contact","Time Duration","court_no.","Staff_ID","Time Available"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.admin_table.xview)
        scroll_y.config(command=self.admin_table.yview)


        self.admin_table.heading("Team Name",text="Team Name")
        self.admin_table.heading("Captain Contact",text="Captain Contact")
        self.admin_table.heading("Time Duration",text="Time Duration")
        self.admin_table.heading("court_no.",text="court_no.")

       

      


        self.admin_table.heading("Staff_ID",text="Staff_ID")
        self.admin_table.heading("Time Available",text="Time Available")
        self.admin_table['show']='headings'
        self.admin_table.pack(fill=BOTH,expand=1)
        self.admin_table.column("Time Available",width=200)
        self.admin_table.bind("<ButtonRelease->",self.get_cursor)
        self.fetch_data()




    def Exit(self):
        
        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):

            self.root.destroy() 


    def submit2(self):





    

        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("insert into time_schedule values(%s,%s,%s,%s,%s,%s)",(self.teamname.get(),

                                                                            self.contact.get(),
                                                                            self.time.get(),
                                                                            self.field.get(),
                                                                            self.Staff_ID.get(),
                                                                            self.txt_time.get('1.0',END)

                                                                     
                                                                   
                                                                
                                                                     
                                                                   
        
                                                                    ))
                                                           

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()        


    def fetch_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from time_schedule")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.admin_table.delete(*self.admin_table.get_children())
            for row in rows:
                self.admin_table.insert('',END,values=row)
            con.commit()
        con.close() 


    def get_cursor(self,ev):
        curosor_row=self.admin_table.focus()
        contents=self.admin_table.item(curosor_row)  
        row=contents['values']   
        self.teamname.set(row[0]),
        self.contact.set(row[1])
        self.time.set(row[2]),
        self.field.set(row[3]),
        self.Staff_ID.set(row[4]),
        self.txt_time.delete("1.0",END)
        self.txt_time.insert(END,row[5])
    def clear(self):
    
        (self.teamname.set(""),
            self.contact.set(""),
            self.time.set(""),
            self.field.set(""),
            self.Staff_ID.set(""),
            self.txt_time.delete("1.0",END)
        )
    def update(self):
        
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("update time_schedule set captain_contact=%s,Time_duration=%s,field_no=%s,Staff_ID=%s,time_available = %s where team_name=%s",(
                                                                            self.contact.get(),
                                                                            self.time.get(),
                                                                            self.field.get(),
                                                                            self.Staff_ID.get(),
                                                                            self.txt_time.get('1.0',END),
                                                                            self.teamname.get()

                                                                            ))

        con.commit()
        self.fetch_data()  
        self.clear()
        con.close()                                                                      
    
        
   



class staff_records:
    def __init__(self,root):   
        self.root=root
        self.root.title("Staff Records")
        self.root.geometry("1600x900")
        self.root.config(bg="gold2")
        self.root.iconbitmap("staff.ico")
      
        ##########################################   

        
        
        ###frames
        frame1 = Frame(self.root,bg="blue",relief= GROOVE,borderwidth=5)
        frame1.place(x=0,y = 0,width = 500, height= 800)
        frame2 = Frame(self.root,bg="crimson",relief= GROOVE,borderwidth=5)
        frame2.place(x=550,y = 0,width = 950, height= 800)
        frame3 = Frame(frame1,bg="blue",relief= GROOVE)
        frame3.place(x=0,y = 730,width =500, height= 55)

        NameLabel=Label(frame1,text="Staff Name:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel.place(x=10,y=50)
        NameLabel2=Label(frame1,text="Staff ID:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel2.place(x=10,y=140)
        NameLabel5=Label(frame1,text="Staff E-mail:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel5.place(x=10,y=230)
        NameLabel3=Label(frame1,text="Staff Contact:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel3.place(x=10,y=320)
        NameLabel4=Label(frame1,text="Staff Address:",bg="gold",font=("times",20,"bold"),relief=GROOVE,borderwidth=5,anchor='w')
        NameLabel4.place(x=10,y=410)


        #entry frame
        self.Name=StringVar()
        self.ID=StringVar()
        self.Email=StringVar()
        self.Contact=StringVar()
        self.Address=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()
        

        ##################staff entry box##########
        
        name1 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Name)
        name1.place(x=250,y=50)
        name2 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.ID)
        name2.place(x=250,y=140)
        name5 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Email)
        name5.place(x=250,y=230)
        name3 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Contact)
        name3.place(x=250,y=320)
        name4 = Entry(frame1,font=('roman',15,'bold'),bd=5,textvariable=self.Address)
        name4.place(x=250,y=410)


        #inserting into the frame 3
        bt1=Button(frame3,text="Submit",font=("arial",16,"bold"),command=self.submit2,width=8,bg="red",fg="black",borderwidth=3)
        bt1.place(x=0,y=0)
        bt2=Button(frame3,text="Delete",font=("arial",16,"bold"),command=self.delete_data,width=8,bg="red",fg="black",borderwidth=3)
        bt2.place(x=120,y=0)
        bt3=Button(frame3,text="Exit",font=("arial",16,"bold"),command=self.Exit,width=8,bg="red",fg="black",borderwidth=3)
        bt3.place(x=360,y=0)
        bt2=Button(frame3,text="Clear",font=("arial",16,"bold"),width=8,command=self.clear,bg="red",fg="black",borderwidth=3)
        bt2.place(x=240,y=0)
        #####for showing frame or data frame


        label12=Label(frame2,text="Search By",bg="crimson",fg="white",font=("times new romans",15,"bold"))
        label12.place(x=25,y=40)

        combo_all=ttk.Combobox(frame2,width=15,font=("times new roman",15,"bold"),textvariable=self.search_by,state='readonly')
        combo_all['values']=("Staff_Name","Staff_ID","Staff_contact")
        combo_all.place(x=130,y=40)

        name11 = Entry(frame2,font=('times new roman',15,'bold'),textvariable=self.search_txt,bd=5,relief=GROOVE)
        name11.place(x=350,y=40)

        btn11=Button(frame2,text="Search",width=8,font=("times new roman",15,"bold"),bg="white",fg="black",command=self.search_data)
        btn11.place(x=640,y=40)

        btn11=Button(frame2,text="Show All",width=8,font=("times new roman",15,"bold"),bg="white",fg="black",command=self.fetch_data)
        btn11.place(x=800,y=40)

        ####adding another frame
        label_frame=Frame(frame2,bd=4,relief=RIDGE,bg="crimson")
        label_frame.place(x=50,y=100,height=600,width=900)

        scroll_x=Scrollbar(label_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(label_frame,orient=VERTICAL)

        self.staff_table=ttk.Treeview(label_frame,columns=("Staff Name","Staff Id","email","Staff Contact","Staff Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)


        self.staff_table.heading("Staff Name",text="Staff Name")
        self.staff_table.heading("Staff Id",text="Staff ID")
        self.staff_table.heading("email",text="Staff E-mail")

        self.staff_table.heading("Staff Contact",text="Staff contact")
        self.staff_table.heading("Staff Address",text="Staff Address")

        self.staff_table['show']='headings'
        self.staff_table.column("Staff Name",width=200) 
        self.staff_table.column("Staff Id",width=100)
        self.staff_table.column("Staff Contact",width=200)
        self.staff_table.column("Staff Address",width=200)
        self.staff_table.column("email",width=250)
        self.staff_table.pack(fill=BOTH,expand=1)
        self.staff_table.bind("<ButtonRelease->",self.get_cursor)
        self.fetch_data()
        self.clear()

    def submit2(self):


        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("insert into staff_records1 values(%s,%s,%s,%s,%s)",(self.Name.get(),
                                                                     self.ID.get(),
                                                                     self.Email.get(),
                                                                     self.Contact.get(),
                                                                     self.Address.get()
                                                                     
                                                                     
                                                                   
                                                                
                                                                     
                                                                   
        
                                                                    ))
                                                           

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from staff_records1")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close() 

    def Exit(self):

            self.root.destroy() 


    def clear(self):

        (self.Name.set(""),
            self.ID.set(""),
            self.Email.set(""),
            self.Contact.set(""),
            self.Address.set("") 
        )   
    def get_cursor(self,ev):
        curosor_row=self.staff_table.focus()
        contents=self.staff_table.item(curosor_row)  
        row=contents['values']   
        self.Name.set(row[0]),
        self.ID.set(row[1]),
        self.Email.set(row[2]),
        self.Contact.set(row[3]),
        self.Address.set(row[4])


     #def update(self):
        
        ##con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        #cur=con.cursor()
        #cur.execute("update staff_records1 Name=%s,ID=%s,Email=%s,Contact=%s,Address=%s",(
                                                                     #self.Name.get(),
                                                                     #self.ID.get(),
                                                                     #self.Email.get(),
                                                                     #self.Contact.get(),
                                                                     #self.Address.get()
                                                                     
                                                 #                            )
           #  )#

                                                                     
                                                                     
                                                                   
                                                                
                                                                     
                                                                   
        
                                                                
                                                           

       # con.commit()
       # self.fetch_data()
        #self.clear()
        #con.close()
    def delete_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        sql = "delete from staff_records1 where Staff_ID =%s"
        ids=(self.ID.get(),)
        cur.execute(sql,ids)
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        my_cursor=con.cursor()

        selected = self.search_by.get()
        
        if selected =="Staff_Name":#"Staff_ID","Staff_contact"
            sql = "select * from staff_records1 where staff_name=%s"

        if selected =="Staff_ID":#"Staff_ID","Staff_contact"
            sql = "select * from staff_records1 where Staff_ID=%s"  


        if selected =="Staff_contact":#"Staff_ID","Staff_contact"
            sql = "select * from staff_records1 where staff_contact=%s"      



        
        

        searched = self.search_txt.get()
        result=my_cursor.execute(sql,searched)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for row in rows:
                self.staff_table.insert('',END,values=row)
            con.commit()
        con.close() 
        self.clear()
##########################################################################




class team_register:
    def __init__(self,root):



        #here we will code about the users attributes for our project:


        self.root=root
        self.root.title("Team Register Form")
        self.root.geometry("1600x900")
        self.root.config(bg="pink")
        self.root.iconbitmap("users.ico")

        self.teamname=StringVar()
        self.teamcode=StringVar()
        self.search_data=StringVar()
        self.search_by=StringVar()


        frame1=Frame(self.root,bg="yellow")
        frame1.place(x=300,y=50,width=900,height=700)
        frame3=Frame(frame1,bg="white")
        frame3.place(x=750,y=400,height=100,width=100)


        lbluser1=Label(frame1,text="Team Name:",compound=LEFT,font=("times new roman", 30,"bold"),bg="yellow",fg="black")
        lbluser1.place(x=100,y=200)
        txtuser=Entry(frame1,bd=5,textvariable=self.teamname, relief=GROOVE,font=("",20))
        txtuser.place(x=400,y=200)


        lbluser2=Label(frame1,text="Team Code:",compound=LEFT,font=("times new roman", 30,"bold"),bg="yellow",fg="black")
        lbluser2.place(x=100,y=300)
        txtpass=Entry(frame1,bd=5,textvariable=self.teamcode, relief=GROOVE,show="*",font=("",20))
        txtpass.place(x=400,y=300)
        ###########
        scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame3,orient=VERTICAL)
        scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame3,orient=VERTICAL)

        self.staff_table1=ttk.Treeview(frame3,columns=("team_name","team_id"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_table1.xview)
        scroll_y.config(command=self.staff_table1.yview)

        self.staff_table1.heading("team_name",text="team_name")
        self.staff_table1.heading("team_id",text="team_id")
        self.staff_table1.column("team_name",width=100) 
        self.staff_table1.column("team_id",width=70)
        self.staff_table1['show']='headings'
        self.staff_table1.pack(fill=BOTH,expand=1)
        self.fetch_data()



        btm_login1=Button(frame1,text="Login",width=15,font=("times new roman",20,"bold"),bg="red",command=self.login,fg="blue")
        btm_login1.place(x=180,y=500)
        label23=Label(frame1,text="Search Your Team-Code",bg="red",fg="black",font=("times new romans",16,"bold"))
        label23.place(x=60,y=400)
        entry123=Entry(frame1,relief=GROOVE,textvariable=self.search_data,font=("Arial",16,"bold"))
        entry123.place(x=500,y=400,width=200)
        self.pic29 = ImageTk.PhotoImage(file = "search1.png")
        btn51=Button(frame1,image = self.pic29,command=self.search)
        btn51.place(x=710,y=400)
        combo_all=ttk.Combobox(frame1,width=15,font=("times new roman",15,"bold"),textvariable=self.search_by,state='readonly')
        combo_all['values']=("team_name")
        combo_all.place(x=320,y=400)   





        btm_login=Button(frame1,text="Exit",command=self.Exit,width=15,font=("times new roman",20,"bold"),bg="red",fg="blue")
        btm_login.place(x=450,y=500)
        self.pic12 = ImageTk.PhotoImage(file = "click1.png")
        btn5=Button(frame1,image = self.pic12,command=self.new_team)
        btn5.place(x=600,y=640)
        lbl2=Label(frame1,text="Click here for new team-------------->",font=("arial",20,"bold"),bg="white",fg="black")
        lbl2.place(x=100,y=645)

    def search(self):
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        my_cursor=con.cursor()

        selected = self.search_by.get()
        
        if selected =="team_name":
            sql = "select * from team_register where team_name=%s"
        if selected =="team_id":
            sql = "select * from team_register where team_id=%s"
   



        
        

        searched = self.search_data.get()
        result=my_cursor.execute(sql,searched)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
                                          
            self.staff_table1.delete(*self.staff_table1.get_children())
            for row in rows:
                self.staff_table1.insert('',END,values=row)
            con.commit()
        con.close()
        self.clear()
    def new_team(self):
        self.new_window22= Toplevel(self.root)
        self.obj = new_player(self.new_window22)
 
   
                                      

                            
    def fetch_data(self):
                                          
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from team_register")
        rows=cur.fetchall()
        con.commit()
        con.close()       
                                        
    def clear(self):
                              
        (self.teamname.set(""),
        self.teamcode.set(""),
            
        )    

    def Exit(self):                
        self.addroot.destroy()

    def Exit1(self):                
        self.root.destroy()                                                                       
        

    def login(self):

                                      
                                      


                                      
                                          
            #get the data and store it into the tuple!
        
        if self.teamname.get()=="" or self.teamcode.get()=="":
                                              

            messagebox.showerror("Error!","Team Name and team code Error!!!!",parent=self.root)


            
        else: 
                try:


                    con=pymysql.connect(host="localhost",user="root",password="",database="admin_login3")
                    cur=con.cursor()
                    cur.execute( "select * from team_register where team_name= %s and team_id=%s" ,(self.teamname.get(),self.teamcode.get()))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error!!","Invalid Team Name and Team code",parent=self.root)
                        self.clear()
                
                    elif row:
                                                      


                        self.new_window2 = Toplevel(self.root)

                        self.obj = users_login(self.new_window2) 
                        self.clear()
                    
            
                except Exception as es:
                    messagebox.showerror("Error!!",f"Error Due to: {str(es)}",parent=self.root)
                    

    def Exit(self):                
        self.root.destroy()


class new_player:
    def __init__ (self,root):
        
        self.root=root
        self.root.title("New Player Login")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.root.iconbitmap("users.ico")
        self.teamname = StringVar()
        self.teamcode = StringVar()
        frame1=Frame(self.root,bg="white",bd=5,relief=GROOVE)
        frame1.place(x=300,y=50,width=800,height=650)
        label23=Label(frame1,text="Team Name:",bg="gold2",fg="black",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,anchor='w')
        label23.place(x=160,y=110)
        txtpass1=Entry(frame1,bd=5,textvariable=self.teamname, relief=GROOVE,font=("",20))
        txtpass1.place(x=350,y=110)
        label24=Label(frame1,text="Team Code:",bg="gold2",fg="black",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,anchor='w')
        label24.place(x=160,y=220)
        txtpass=Entry(frame1,bd=5,textvariable=self.teamcode, relief=GROOVE,font=("",20))
        txtpass.place(x=350,y=220)
        btn1=Button(frame1,text="Register",command=self.register1,bg="red",fg="black",font=('times',20,"bold"))
        btn1.place(x=190,y=450,width=150)
        btn2=Button(frame1,text="Exit",command=self.cancel2,bg="red",fg="black",font=('times',20,"bold"))
        btn2.place(x=400,y=450,width=150)
    def cancel2(self):
    
        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):


            self.root.destroy() 



    def register1(self):
                                      
            if self.teamname.get()=="" or self.teamcode.get()=="":
                              
                messagebox.showerror("Error!","Team Name and Team code must be Provided",parent=self.root)


            
            else:
                try:   

                                              

                    con=pymysql.connect(host="localhost",user="root",password="",database="admin_login3")
                    cur=con.cursor()
                    log=cur.execute("insert into team_register values(%s,%s)",(self.teamname.get(),
                                                                            self.teamcode.get()))
                    messagebox.showinfo("Successfully Registred!","Registered",parent=self.root)
                    self.clear1()
                                                                        
                                                                          
                

                    con.commit()   
                    con.close()    

                except Exception as es:


                    messagebox.showerror("Error!!",f"Error Due to: {str(es)}",parent=self.root)
                      

    def clear1(self):
        (self.teamname.set(''),
        self.teamcode.set('')    
        )               





        
class users_login:
    def __init__(self,root):



        #here we will code about the users attributes for our project:


        self.root=root
        self.root.title("Only for Users")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.root.iconbitmap("users.ico")


        #here is the code for entire users login page
        



        frame4 = Frame(root,bg="yellow",relief=SUNKEN,borderwidth=1)
        frame4.place(x=460,y=10,width=600,height=60)


        label4 = Label(frame4,text = "Welcome Users",font=("Arial",25,"bold"),fg="blue",bg="yellow")
        label4.place(x=220,y=7)

        frame5 = Frame(root, bg= "red",relief=GROOVE,borderwidth=3)
        frame5.place(x=340,y=100,height=700,width=900)

        frame6=Frame(frame5,bg="white",relief=GROOVE,borderwidth=2)
        frame6.place(x=0,y=650,height=45,width=900)

        #here the code for label and text written address

        label5 = Label(frame5,text="Fill the form correctly ✔",font=("arial",16,"bold"),fg="Blue",bg="pink")
        label5.place(x=340,y=1)
        
        #variables of 
        self.teamname=StringVar()
        self.id=StringVar()
        self.contact=StringVar()
        self.address=StringVar()
        
       
        

        lbluser1=Label(frame5,text="Team Name:",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="black").grid(row=1,column=0,padx=140,pady=35)
        txtuser1=Entry(frame5,textvariable=self.teamname,bd=5, relief=GROOVE,borderwidth=5,font=("",15)).grid(row=1,column=1,padx=10)
        lbluser11=Label(frame5,text="Team ID:",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="black").grid(row=2,column=0,padx=140,pady=35)
        txtuser11=Entry(frame5,textvariable=self.id,bd=5, relief=GROOVE,borderwidth=5,font=("",15)).grid(row=2,column=1,padx=10)

        lbluser2=Label(frame5,text="Players Name",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="black").grid(row=3,column=0,padx=140,pady=35)
        self.txt_player=Text(frame5,bd=5,width=20,height=4,relief=GROOVE,font=("",15))
        
        self.txt_player.grid(row=3,column=1,padx=10)


        lbluser3=Label(frame5,text="Captain Contact:",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="black").grid(row=5,column=0,padx=140,pady=35)
        txtuser3=Entry(frame5,bd=5,textvariable=self.contact,relief=GROOVE,font=("",15)).grid(row=5,column=1,padx=10)


        

        lbluser4=Label(frame5,text="Address Of Captain:",compound=LEFT,font=("times new roman", 20,"bold"),bg="yellow",fg="black").grid(row=6,column=0,padx=140,pady=35)
        txtpass4=Entry(frame5,bd=5,textvariable=self.address,relief=GROOVE,font=("",15)).grid(row=6,column=1,padx=10)


        


        
    
        btn2=Button(frame6,text="Submit",font=("times new romans",16,"bold"),relief=GROOVE,bg="red",fg="black",command=self.login2)
        btn2.place(x=0,y=0,width=250)

        btn3=Button(frame6,text="Cancel",font=("times new romans",16,"bold"),command=self.Exit1,relief=GROOVE,bg="red",fg="black")
        btn3.place(x=650,y=0,width=250)

        btn4=Button(frame6,text="Clear",font=("times new romans",16,"bold"),command=self.clear,relief=GROOVE,bg="red",fg="black")
        btn4.place(x=335,y=0,width=250)
        

    def login2(self):

        if self.teamname.get()=="" or self.id.get()=="" or self.txt_player.get('1.0',END)=="" or self.contact.get()=="" or self.address.get()=="": 


    
            messagebox.showerror("Error!","Please fill all the required form",parent=self.root)

        else:

            try:


                con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
                cur=con.cursor()
                cur.execute("insert into users_form values(%s,%s,%s,%s,%s)",(self.teamname.get(),
                                                                        self.id.get(),

                                                                        self.txt_player.get('1.0',END),
                                                                        self.contact.get(),
                                                                        self.address.get()
                                                                        ))
                con.commit()
                self.clear()  
                con.close()
                self.new_window4= Toplevel(self.root)
                self.obj = submit(self.new_window4)                                                          
            except Exception as es:


                messagebox.showerror("Error!!",f"Error Due to Team code",parent=self.root)
                self.clear()                                                    



    def Exit1(self):

        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):


            self.root.destroy() 


            
    def clear(self):


    
        (
        self.teamname.set(""),
        self.id.set(""),
        self.txt_player.delete('1.0',END),
        self.contact.set(""),
        self.address.set("") 
         )   


            


    def new_window4(self):
        self.new_window4= Toplevel(self.root)
        self.obj = submit(self.new_window4)









    #   here is the program of submitting the form:
  


class submit:

    def __init__(self,root):
    


        self.root=root
        self.root.title("Booking and Payment")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")

        

        frame11 = Frame(root,bg="blue")
        frame11.place(x=420,y=0,width=700,height=800)
        frame12 = Frame(frame11,relief=SUNKEN,borderwidth=2,bg="gold2")
        frame12.place(x=100,y=0,width=400,height=800)
        frame13 = Frame(frame12,bg="gold2")
        frame13.place(x=0,y=50,width=400,height=600)

        ###
        label1= Label(frame12,text="Book And Pay",font=("Arial",30,"bold"),fg="red",bg="white")
        label1.place(x=60,y=10)
        btn1=Button(frame13,text="Available Time",command=self.time,font=("times new romans",18,"bold"),bg="pink",fg="red")
        btn1.place(x=0,y=120,width=399)
        btn2=Button(frame13,text="Check Your History",command=self.history,font=("times new romans",18,"bold"),bg="pink",fg="red")
        btn2.place(x=0,y=240,width=399)
        btn3=Button(frame13,text="Book - Pay",command=self.book,font=("times new romans",18,"bold"),bg="pink",fg="red")
        btn3.place(x=0,y=360,width=399)

        btn4=Button(frame13,text="Cancel",command=self.cancel,font=("times new romans",18,"bold"),bg="red",fg="black")
        btn4.place(x=100,y=550,width=200)




        ##
    def time(self):
        self.new_window13 = Toplevel (self.root)
        self.obj= time_available(self.new_window13)

    def history(self):
        self.new_window12= Toplevel(self.root)
        self.obj = history(self.new_window12)
       
    def book(self):
        self.new_window14 = Toplevel(self.root)
        self.obj=book_pay(self.new_window14)


    def cancel(self):

    
        res = messagebox.askyesnocancel('Notification','Do you want to exit?',parent=self.root)
        if(res==True):

            self.root.destroy() 
class book_pay:
    def __init__(self,root):
        self.root=root
        self.root.title("Book And Pay Bill")
        self.root.geometry("1600x900")
        self.root.config(bg="blue")
        self.Name = StringVar()
        self.ID = StringVar()
        self.date = StringVar()
        self.court_no = StringVar()
        self.date.set(time.strftime("%Y / %m /%d"))

        self.Day = StringVar()
        self.time = StringVar()
    
        
        frame32=Frame(self.root,bg="red",relief=GROOVE,bd=2)
        frame32.place(x=400,y=100,width=700,height=700)
        label32=Label(root,text="Book by your Team Name And Team Code",font=('times',28,'bold'),bg="white",fg="black")
        label32.place(x=420,y=20)
        label33=Label(frame32,text="Team Name:",font=('times',22,'bold'),bg="white",fg="black")
        label33.place(x=40,y=50)
        label34=Label(frame32,text="Team Code:",font=('times',22,'bold'),bg="white",fg="black")
        label34.place(x=40,y=150)
        label90=Label(frame32,text="Court n0.",font=("times",22,"bold"),bg="white",fg="black")
        label90.place(x=40,y=250)
        label91=Label(frame32,text="Date",font=("times",22,"bold"),bg="white",fg="black")
        label91.place(x=40,y=350)

        
        label35=Label(frame32,text="Day:",font=('times',22,'bold'),bg="white",fg="black")
        label35.place(x=40,y=450)
        label36=Label(frame32,text="Time",font=('times',22,'bold'),bg="white",fg="black")
        label36.place(x=40,y=550)
        entry32=Entry(frame32,font=("arial",22,"bold"),textvariable=self.Name)
        entry32.place(x=250,y=50)
        entry33=Entry(frame32,font=("arial",22,"bold"),show='*',textvariable=self.ID)
        entry33.place(x=250,y=150)
        combo_all11=ttk.Combobox(frame32,width=15,font=("times new roman",22,"bold"),textvariable=self.court_no,state='readonly')
        combo_all11['values']=("1","2","3","4","5","6","7")
        combo_all11.place(x=250,y=250)
        entry331=Entry(frame32,font=("arial",22,"bold"),textvariable=self.date)
        entry331.place(x=250,y=350)

        
        combo_all1=ttk.Combobox(frame32,width=15,font=("times new roman",22,"bold"),textvariable=self.Day,state='readonly')
        combo_all1['values']=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
        combo_all1.place(x=250,y=450)
        
        combo_all2=ttk.Combobox(frame32,width=15,font=("times new roman",22,"bold"),textvariable=self.time,state='readonly')
        combo_all2['values']=("6:00am-7:00am","7:00am-8:00am","8:00am-9:00am","9:00am-10:00am","10:00am-11:00am","11:00am-12pm","12:00pm-1:00pm","1:00pm-2:00pm","2:00pm-3:00pm","3:00pm-4:00pm","4:00pm-5:00pm","5:00pm-6:00pm","6:00pm-7:00pm","7.00pm-8:00pm","8:00pm-9:00pm")
        combo_all2.place(x=250,y=550)

        btn1=Button(frame32,text="Book",command=self.book,font=('times',16,'bold'),bg="gold2")
        btn1.place(x=1,y=650,width=120)
        

        btn2=Button(frame32,text="Clear",command=self.clear,font=('times',16,'bold'),bg="gold2")
        btn2.place(x=150,y=650,width=120)
        btn3=Button(frame32,text="Payment",command=self.payment,font=('times',16,'bold'),bg="gold2")
        btn3.place(x=290,y=650,width=120)
        
        btn4=Button(frame32,text="Checkout",command=self.check_out,font=('times',16,'bold'),bg="gold2")
        btn4.place(x=430,y=650,width=120)
        btn5=Button(frame32,text="Cancel",command=self.cancel,font=('times',16,'bold'),bg="gold2")
        btn5.place(x=570,y=650,width=120)
        

        #######################
    def check_out(self):
    
        self.new_window49 = Toplevel(self.root)
        self.obj=New_Toplevel(self.new_window49)    
          

    def cancel(self):


        messagebox.askyesno("Exit","Do You Really Want to Exit",parent=self.root)
        self.root.destroy()


    def payment(self):

        self.new_window45 = Toplevel(self.root)
        self.obj=payment(self.new_window45)


    def book(self):





        if self.Name=="" or self.ID.get()=="" or self.Day.get()=="" or self.time.get()=="": 

            messagebox.showerror("Error!","Please fill all the required form",parent=self.root)


        else:


            try:
                




                con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
                cur=con.cursor()
                cur.execute("insert into booking2 values(%s,%s,%s,%s,%s,%s)",(self.Name.get(),

                                                                        self.ID.get(),
                                                                        self.court_no.get(),
                                                                        self.date.get(),
                                                                        self.Day.get(),
                                                                        self.time.get()
                                                                        ))
                messagebox.showinfo("Successfully","Your booking is approved",parent=self.root)                                                        
                                                                        
                con.commit()
                self.clear()
                con.close()

            except Exception as es:

                messagebox.showerror("Error!!","Team Id doesnot match with team-name",parent=self.root)
                      
    def clear(self):
    
        (self.Name.set(""),

        self.ID.set(""),
        self.court_no.set(""),
        self.date.set(""),
        self.Day.set(""),
        self.time.set("")
        )


class New_Toplevel:

    def __init__(self,root):
        
        self.root = root
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 23 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 24 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        self.root.geometry("1600x900")
        self.root.title("Check In and Check Out")
        self.root.configure(background="#ffffff")
        self.root.configure(highlightbackground="#ffffff")
        self.root.configure(highlightcolor="black")



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.14, rely=0.12, height=46, width=442)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#bfbfbf")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffffff")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''ENTER THE COURT NO.   :''')

        self.Entry1 = Entry(self.Frame1)
        self.data=StringVar()
        self.Entry1.place(relx=0.67, rely=0.12,height=44, relwidth=0.07)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#bfbfbf")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffffff")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#e6e6e6")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=self.data)







        self.Text1 = Text(self.Frame1)
        self.Text1.place(relx=0.05, rely=0.54, relheight=0.4, relwidth=0.89)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#ffffff")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#e6e6e6")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=824)
        self.Text1.configure(wrap=WORD)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.34, rely=0.28, height=93, width=286)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#bfbfbf")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#ffffff")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''CHECK OUT ''')
        self.Button1.configure(command=self.check_room)
    def check_room(self):
            self.rom = str(self.data.get())
            print(self.rom)
            print("\n")
            if self.rom.isdigit() == True and len(self.rom) != 0:
                self.Text1.insert(INSERT, " CHECKED OUT ""\n") 
                    
     

        
class payment:
    def __init__(self,root):




                              
        self.root=root
        self.root.title("Booking and Payment")
        self.root.geometry("1600x900")
        self.root.config(bg="pink")



        frame9=Frame(root,bg="white",relief=GROOVE,borderwidth=5)
        frame9.place(x=60,y=100,height=700,width=700)
        frame10=Frame(frame9,bg="pink",relief=GROOVE,borderwidth=5)
        frame10.place(x=100,y=20,height=50,width=500)
        label9=Label(frame10,text="Pay Through E-Sewa",font=("Arial",16,"bold"),fg="blue",bg="pink")
        label9.place(x=90,y=4)
        label10=Label(self.root,text="Scan QR-code",font=("Arial",16,"bold"),fg="blue",bg="gold2")
        label10.place(x=300,y=260)
        frame11=Frame(root,bg="white",relief=GROOVE,borderwidth=5)
        frame11.place(x=780,y=100,height=700,width=700)
        label11=Label(frame11,text="Futsal And Canteen Payment",font=("Arial",21,"bold"),fg="blue",bg="gold2")
        label11.place(x=140,y=30)
        #self.pic32 = ImageTk.PhotoImage(file="clickme.png")
        btn23=Button(frame11,text="Open Billing",font=("Arial",18,"bold"),relief=GROOVE,bg="Gold2",fg="black",command=self.bill)
        btn23.place(x=250,y=400)
        #label11=Label(self.root,text="Pay with Cash ",font=("Arial",16,"bold"),fg="blue",bg="gold2")
        #label11.place(x=500,y=400)
        

        self.bg_icon2 = ImageTk.PhotoImage(Image.open("myQG.png"))
        logo1 = Label(self.root,image=self.bg_icon2)
        logo1.place(x=210,y=300)


    def bill(self):
        self.new_window29 = Toplevel(self.root)
        self.obj = Bill_App(self.new_window29)  





class Bill_App:
	def __init__(self,root):
    
		self.root=root
		self.root.geometry("1600x900+0+0")
		self.root.title(" Futsal Billing System")
		bg_color='#675634'
		title=Label(self.root,text="FUTSAL BILL PAYMENT  ",bd=15,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
		#================Variables==========================
		#================Cosemetics==========================

		self.soap=IntVar()
		self.face_cream=IntVar()
		self.face_wash=IntVar()
		self.spray=IntVar()
		self.gell=IntVar()
		self.loshan=IntVar()

		#================Grocery==========================
		
		self.rice=IntVar()
		self.food_oil=IntVar()
		self.daal=IntVar()
		self.wheat=IntVar()
		self.sugar=IntVar()
		self.tea=IntVar()

		#================Cold Drinks==========================

		self.maza=IntVar()
		self.cock=IntVar()
		self.frooti=IntVar()
		self.thumbsup=IntVar()
		self.limca=IntVar()
		self.sprite=IntVar()

		#================Total Product Price & Tax variables==========================

		self.cosemtic_price=StringVar()
		self.grocery_price=StringVar()
		self.cold_drink_price=StringVar()

		self.cosemetic_tax=StringVar()
		self.grocery_tax=StringVar()
		self.cold_drink_tax=StringVar()

		#================Cutomers==================================

		self.c_name=StringVar()
		self.c_phon=StringVar()

		self.bill_no=StringVar()
		x=random.randint(000,999)
		
		self.bill_no.set(str(x))

		self.search_bill=StringVar()




		#=============Customer Details Frame
		F1=LabelFrame(self.root,bd=8,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F1.place(x=0,y=80,relwidth=1)

		cname_lbl=Label(F1,text="Team Name",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
		cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

		cphn_lbl=Label(F1,text="Captain Contact",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
		cphn_txt=Entry(F1,width=15,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

		c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="White",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
		c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

		bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12").grid(row=0,column=6,padx=6,pady=10)


		#===================Cosemetics Frame==========
		
		F2=LabelFrame(self.root,bd=8,text="Chest guard",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F2.place(x=5,y=180,width=325,height=380)

		bath_lbl=Label(F2,text="Futsal Match",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		bath_txt=Entry(F2,width=10,textvariable=self.soap ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		Face_cream_lbl=Label(F2,text="Jersey",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		Face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		Fcae_w_lbl=Label(F2,text="Football",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		Face_w_txt=Entry(F2,width=10,textvariable=self.face_wash, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		Hair_s_lbl=Label(F2,text="Futsal Shoe",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		Hair_s_txt=Entry(F2,width=10,textvariable=self.spray, font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		Hair_g_lbl=Label(F2,text="Football Shocks",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		Hair_g_txt=Entry(F2,width=10,textvariable=self.gell ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
		Body_lbl=Label(F2,text="Moov",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		Body_txt=Entry(F2,width=10,textvariable=self.loshan ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		
		
		#===================Grocery Frame==========
		
		F3=LabelFrame(self.root,bd=8,text="Services",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F3.place(x=340,y=180,width=325,height=380)

		g1_lbl=Label(F3,text="Water",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		g1_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		g2_lbl=Label(F3,text="Refree",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		g2_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		g3_lbl=Label(F3,text="Foods",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		g3_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		g4_lbl=Label(F3,text="Penalty",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		g4_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		g5_lbl=Label(F3,text="Grass",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		g5_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
		g6_lbl=Label(F3,text="Gloves",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		

		#===================Cold Drink Frame==========
		
		F4=LabelFrame(self.root,bd=8,text="Cold Drinks",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F4.place(x=675,y=180,width=325,height=380)

		c1_lbl=Label(F4,text="7UP",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
		c1_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

		c2_lbl=Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
		c2_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

		c3_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
		c3_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

		c4_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
		c4_txt=Entry(F4,width=10,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

		c5_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
		c5_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
		
		c6_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
		c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
		
		#===============Bill Area=============
		F5=Frame(self.root,bd=8,relief=GROOVE)
		F5.place(x=1010,y=180,width=340,height=380)

		bill_title=Label(F5,text="BILL AREA",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)		
		scrol_y=Scrollbar(F5,orient=VERTICAL)
		self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
		scrol_y.pack(side=RIGHT,fill=Y)
		scrol_y.config(command=self.txtarea.yview)
		self.txtarea.pack(fill=BOTH,expand=1)
		

		#==============Button Frame=============

		F6=LabelFrame(self.root,bd=8,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
		F6.place(x=0,y=560,relwidth=1,height=140)
		m1_lbl=Label(F6,text="Payment Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
		m1_txt=Entry(F6,width=18,textvariable=self.cosemtic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

		m2_lbl=Label(F6,text="Total Services Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
		m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

		m3_lbl=Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
		m3_txt=Entry(F6,width=18,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


		c1_lbl=Label(F6,text="PaymentTax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
		c1_txt=Entry(F6,width=18,textvariable=self.cosemetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

		c2_lbl=Label(F6,text="Services Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
		c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

		c3_lbl=Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
		c3_txt=Entry(F6,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


		btn_F=Frame(F6,bd=7,relief=GROOVE)
		btn_F.place(x=740,width=590,height=102)

		total_btn=Button(btn_F,text="Total",command=self.total,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=0,padx=5,pady=5)
		GBill_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=1,padx=5,pady=5)
		Clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=2,padx=5,pady=5)
		Exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=15,bd=4,width=10,font="arial 14 bold").grid(row=0,column=3,padx=4,pady=5)
		
		self.welcome_bill()
#=============functions for working=============================
	def total(self):
		self.c_s_p=self.soap.get()*1200
		self.c_fc_p=self.face_cream.get()*1000
		self.c_fw_p=self.face_wash.get()*1500
		self.c_hs_p=self.spray.get()*1800
		self.c_hg_p=self.gell.get()*120
		self.c_bl_p=self.loshan.get()*90
		self.total_cosemetic_price=float(
										self.c_s_p+
										self.c_fc_p+
										self.c_fw_p+
										self.c_hs_p+
										self.c_hg_p+
										self.c_bl_p
										)
		self.cosemtic_price.set("Rs. "+str(self.total_cosemetic_price))
		self.c_tax=round((self.total_cosemetic_price*0.05),2)
		self.cosemetic_tax.set("Rs. "+str(self.c_tax))

		self.g_r_p=self.rice.get()*25
		self.g_f_p=self.food_oil.get()*100
		self.g_d_p=self.daal.get()*100
		self.g_w_p=self.wheat.get()*20
		self.g_s_p=self.sugar.get()*15
		self.g_t_p=self.tea.get()*10

		self.total_grocery_price=float(
										self.g_r_p+
										self.g_f_p+
										self.g_d_p+
										self.g_w_p+
										self.g_s_p+
										self.g_t_p
										)
		self.grocery_price.set("Rs. "+str(self.total_grocery_price))
		self.g_tax=round((self.total_grocery_price*0.1),2)
		self.grocery_tax.set("Rs. "+str(self.g_tax))

		self.d_m_p=self.maza.get()*50
		self.d_c_p=self.cock.get()*50
		self.d_f_p=self.frooti.get()*30
		self.d_t_p=self.thumbsup.get()*35
		self.d_l_p=self.limca.get()*50
		self.d_s_p=self.sprite.get()*50
		self.total_drinks_price=float(
										self.d_m_p+
										self.d_c_p+
										self.d_f_p+
										self.d_t_p+
										self.d_l_p+
										self.d_s_p
										)
		self.cold_drink_price.set("Rs. "+str(self.total_drinks_price))
		self.d_tax=round((self.total_drinks_price*0.05),2)
		self.cold_drink_tax.set("Rs. "+str(self.d_tax))


		self.Total_bill=float(
								self.total_cosemetic_price+
								self.total_grocery_price+
								self.total_drinks_price+
								self.c_tax+
								self.g_tax+
								self.d_tax
							)	

	def welcome_bill(self):
		self.txtarea.delete('1.0',END)
		self.txtarea.insert(END,"\t Welcome to Futsal Club\n")
		self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
		self.txtarea.insert(END,f"\n Team Name : {self.c_name.get()}")
		self.txtarea.insert(END,f"\n Captain Contact : {self.c_phon.get()}")
		self.txtarea.insert(END,f"\n ====================================")
		self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
		self.txtarea.insert(END,f"\n ====================================")


	def bill_area(self):
		if self.c_name.get()=="" or self.c_phon.get()=="":
			messagebox.showerror("Error","Customer Details are must",parent=self.root)
		elif self.cosemtic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0" :
		 	messagebox.showerror("Error","No Product Purchased",parent=self.root)
		else:	
			self.welcome_bill()
			#========Cosemetics==========
			if self.soap.get()!=0:
				self.txtarea.insert(END,f"\n Futsal charge\t\t{self.soap.get()}\t\t{self.c_s_p}")

			if self.face_cream.get()!=0:
				self.txtarea.insert(END,f"\n Jersey price \t\t{self.face_cream.get()}\t\t{self.c_fc_p}")

			if self.face_wash.get()!=0:
				self.txtarea.insert(END,f"\n Football\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
			
			if self.spray.get()!=0:
				self.txtarea.insert(END,f"\n Futsal Shoe\t\t{self.spray.get()}\t\t{self.c_hs_p}")

			if self.gell.get()!=0:
				self.txtarea.insert(END,f"\n shocks\t\t{self.gell.get()}\t\t{self.c_hg_p}")
			
			if self.loshan.get()!=0:
				self.txtarea.insert(END,f"\n Moov\t\t{self.loshan.get()}\t\t{self.c_bl_p}")
		
			#========Grocery==========
			if self.rice.get()!=0:
				self.txtarea.insert(END,f"\n Mineral Water\t\t{self.rice.get()}\t\t{self.g_r_p}")

			if self.food_oil.get()!=0:
				self.txtarea.insert(END,f"\n Refree charge\t\t{self.food_oil.get()}\t\t{self.g_f_p}")

			if self.daal.get()!=0:
				self.txtarea.insert(END,f"\n Foods\t\t{self.daal.get()}\t\t{self.g_d_p}")
			
			if self.wheat.get()!=0:
				self.txtarea.insert(END,f"\n Penalty\t\t{self.wheat.get()}\t\t{self.g_w_p}")

			if self.sugar.get()!=0:
				self.txtarea.insert(END,f"\n Grass\t\t{self.sugar.get()}\t\t{self.g_s_p}")
			
			if self.tea.get()!=0:
				self.txtarea.insert(END,f"\n Gloves\t\t{self.tea.get()}\t\t{self.g_t_p}")
		
			#========Cold Drinks==========
			if self.maza.get()!=0:
				self.txtarea.insert(END,f"\n 7UP\t\t{self.maza.get()}\t\t{self.d_m_p}")

			if self.cock.get()!=0:
				self.txtarea.insert(END,f"\n Coca Cola\t\t{self.cock.get()}\t\t{self.d_c_p}")

			if self.frooti.get()!=0:
				self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
			
			if self.thumbsup.get()!=0:
				self.txtarea.insert(END,f"\n Thumbs Up\t\t{self.thumbsup.get()}\t\t{self.d_t_p}")

			if self.limca.get()!=0:
				self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
			
			if self.sprite.get()!=0:
				self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
			
			self.txtarea.insert(END,f"\n ------------------------------------")
			if self.cosemetic_tax.get()!="Rs. 0.0":
					self.txtarea.insert(END,f"\n Cosemetic Tax\t\t{self.cosemetic_tax.get()}")
			if self.grocery_tax.get()!="Rs. 0.0":
					self.txtarea.insert(END,f"\n Grocery Tax\t\t{self.grocery_tax.get()}")
			if self.cold_drink_tax.get()!="Rs. 0.0":
					self.txtarea.insert(END,f"\n Cold Drink Tax\t\t{self.cold_drink_tax.get()}")
			
			self.txtarea.insert(END,f"\n Total Bill : \t\t Rs. {self.Total_bill}")
			self.txtarea.insert(END,f"\n ------------------------------------")
			self.save_bill()

	def save_bill(self):
		op=messagebox.askyesno("Saving Bill.....","Do You Want Save your Bill",parent=self.root)

		if op>0:
			self.bill_data=self.txtarea.get('1.0',END)
			f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
			f1.write(self.bill_data)
			f1.close()
			messagebox.showinfo("Saving.....",f"{self.c_name.get()} Your Bill No : {self.bill_no.get()}  Successfully Saved please see the Bills folder on bill directory to see your Bills",parent=self.root)
		else:
			return	

	def find_bill(self):
		present="no"
		for i in os.listdir("Bills/"):
			if i.split('.')[0]==self.search_bill.get():
				f1=open(f"Bills/{i}","r")
				self.txtarea.delete('1.0',END)
				for d in f1:
					self.txtarea.insert(END,d)
				f1.close()
				present="yes"
		if present=="no":
			messagebox.showerror("Error","Invalid Bill Number ..Please Enter Valid Bill Number",parent=self.root)
	
	def clear_data(self):

        #================Cosemetics==========================

		self.soap.set(0)
		self.face_cream.set(0)
		self.face_wash.set(0)
		self.spray.set(0)
		self.gell.set(0)
		self.loshan.set(0)

			#================Grocery==========================
			
		self.rice.set(0)
		self.food_oil.set(0)
		self.daal.set(0)
		self.wheat.set(0)
		self.sugar.set(0)
		self.tea.set(0)

			#================Cold Drinks==========================

		self.maza.set(0)
		self.cock.set(0)
		self.frooti.set(0)
		self.thumbsup.set(0)
		self.limca.set(0)
		self.sprite.set(0)

			#================Total Product Price & Tax variables==========================

		self.cosemtic_price.set("")
		self.grocery_price.set("")
		self.cold_drink_price.set("")

		self.cosemetic_tax.set("")
		self.grocery_tax.set("")
		self.cold_drink_tax.set("")

			#================Cutomers==================================

		self.c_name.set("")
		self.c_phon.set("")

		self.bill_no.set("")
		x=random.randint(1000,9999)
			
		self.bill_no.set(str(x))

		self.search_bill.set("")
		self.welcome_bill()


	def Exit_app(self):

		self.root.destroy()



        








class time_available:

    def __init__(self,root):
        self.root=root

        self.root.title("Time Availabe")
        self.root.geometry("1600x900")
        self.root.config(bg="crimson")
        frame12=Frame(self.root,bg="white",borderwidth=5)
        frame12.place(x=300,y=30,width=800,height=700)
        scroll_x=Scrollbar(frame12,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame12,orient=VERTICAL)

        self.playing_table=ttk.Treeview(frame12,columns=("Current playing Team Name","Time Duration","Field no.","Time Available"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.playing_table.xview)
        scroll_y.config(command=self.playing_table.yview)


        self.playing_table.heading("Current playing Team Name",text="Playing Team Name")
        self.playing_table.heading("Time Duration",text="Time Duration")
        self.playing_table.heading("Field no.",text="Field no.")
        self.playing_table.heading("Time Available",text="Time Available")

       

      


        self.playing_table['show']='headings'
        self.playing_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    
    def fetch_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select team_Name,Time_duration,field_no,time_available from time_schedule")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.playing_table.delete(*self.playing_table.get_children())
            for row in rows:
                self.playing_table.insert('',END,values=row)
            con.commit()
        con.close() 


        





class history :
    def __init__ (self,root):
        self.root=root

        self.root.title("History")
        self.root.geometry("1600x900")
        self.root.config(bg="gold2")
        ##############variable
        self.search_by = StringVar()
        self.search_txt = StringVar()

        frame1= Frame(root,bg="crimson")
        frame1.place(x=250,y=25,height=800,width=1000)
        frame2 = Frame(frame1,bg="white",relief=GROOVE,borderwidth=5)
        frame2.place(x=200,y=650,height=120,width=700)
        frame3=Frame(frame1,bg="white",relief=GROOVE,borderwidth=5)
        frame3.place(x=200,y=30,height=500,width=700)
        label1=Label(frame2,text="Search By:",font=("Arial",18,"bold"),fg="red")
        label1.place(x=3,y=30)
        combo_all=ttk.Combobox(frame2,width=15,font=("times new roman",18,"bold"),textvariable=self.search_by,state='readonly')
        combo_all['values']=("Team_Name","Id",)
        combo_all.place(x=140,y=30)
        name11 = Entry(frame2,font=('times new roman',18,'bold'),textvariable=self.search_txt,bd=5,relief=GROOVE)
        name11.place(x=370,y=30,width=200)
        self.pic1 = ImageTk.PhotoImage(file = "back1.png")
        btn5=Button(root,image = self.pic1,command=self.back)
        btn5.place(x=0,y=0)
        #####################
        scroll_x=Scrollbar(frame3,orient=HORIZONTAL)
        scroll_y=Scrollbar(frame3,orient=VERTICAL)

        self.player_table=ttk.Treeview(frame3,columns=("Team_Name","Id","court_no","Date","Day","Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.player_table.xview)
        scroll_y.config(command=self.player_table.yview)
        #providing heading
        self.player_table.heading("Team_Name",text="Team Name")
        self.player_table.heading("Id",text="Id")
        self.player_table.heading("court_no",text="Court_no")
        self.player_table.heading("Date",text="Date")
        self.player_table.heading("Day",text="Day ")
        self.player_table.heading("Time",text="Time")
        
        self.player_table['show']='headings'
        self.player_table.pack(fill=BOTH,expand=1)
        self.fetch_data()


        self.pic = ImageTk.PhotoImage(file = "search1.png")
        btn4=Button(frame2,image = self.pic,command=self.search_data)
        btn4.place(x=590,y=33)
        btn8=Button(frame2,text="Show All",command=self.fetch_data,relief=GROOVE,bg="white",fg="red",font=("times new romans",14,"bold"))
        btn8.place(x=300,y=70)


    
    def fetch_data(self):
        
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        cur=con.cursor()
        cur.execute("select * from booking2")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.player_table.delete(*self.player_table.get_children())
            for row in rows:
                self.player_table.insert('',END,values=row)
            con.commit()
        con.close()     
    def search_data(self):
            
        con=pymysql.connect(host='localhost',user="root",password="",database="admin_login3")
        my_cursor=con.cursor()
        selected1 = self.search_by.get()
        
        if selected1 == "Team_Name":#"Staff_ID","Staff_contact"
            sql1 = "select * from booking2 where Team_Name=%s"

        if selected1 == "Id":#"Staff_ID","Staff_contact"
            sql1 = "select * from booking2 where Id=%s"  


       



        
        

        searched1 = self.search_txt.get()
        result=my_cursor.execute(sql1,searched1)


        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.player_table.delete(*self.player_table.get_children())
            for row in rows:
                self.player_table.insert('',END,values=row)
            con.commit()
        con.close()   

    def back(self):
        self.root.destroy()    


        
 
      

    
root = Tk()
obj = window1(root)
root.mainloop()