from tkinter import *
from tkinter import messagebox as ms
from PIL import ImageTk, Image
import tkinter as tk
import random
import wikipedia
import time

import sqlite3


with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEX NOT NULL);')
db.commit()
db.close()

class intro:
    
    def __init__(self,master):
        self.master = master
        self.master.title("INTRO PAGE")
        self.widgets()
        

    def introo(self):
        self.newWindow = Toplevel(self.master)
        self.app = main(self.newWindow)

    def widgets(self):
        
        self.root=root
        img=tk.PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\shop.png")
        self.head = Label(self.master,text = 'WELCOME TO EASY SHOPI',font = ('Helvetica',25,'bold'),pady = 10,bg='orange',fg='white')
        self.head.pack(expand=1,fill=tk.X)
        self.lbl=tk.Label(root,image=img,height=500,width=500,bg='orange').pack()
        self.button1=tk.Button(root, text="    CONTINUE TO SHOP : ) ",font = ('Times',10,'bold'),bd=6,bg ='green',fg='orange',command=self.introo)
        self.button1.place(x=160,y=400)
        
        self.root.mainloop()

        

class main():
    
    def __init__(self,master):
        self.master = master        
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.email = StringVar()
        self.widgets()
        self.master.title("Login Page")
        
      

   
    def login(self): 
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result = c.fetchall()
        if result:
            self.logf.pack_forget()
            ms.showinfo('logged in succesfully',self.username.get() + '\n Logged In')
            self.head['pady'] = 150
            self.newWindow = Toplevel(self.master)
            self.app = eshopi(self.newWindow)
        else:
            ms.showerror('Oops!','Username Not Found.')
            
    def new_user(self):
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user,[(self.username.get())])        
        if c.fetchall():
            ms.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!','Account Created! , Click On CONTINUE TO SHOP! and Login')
            self.log()
            insert = 'INSERT INTO user(username,password) VALUES(?,?)'
            c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
            db.commit()


    def update(self):
        u=self.username.get()
        p=self.password.get()

        if(self.username.get() =="" or self.password.get() == ""):
            ms.askokcancel("Reset Password","please fill all details!!!")
        else:
            conn = sqlite3.connect('quit.db')
            with conn:
                   cursor=conn.cursor
                   conn.execute("UPDATE user SET password=? WHERE username=?",(p,u))
                   ms.askokcancel("Reset Password","Password is updated!!!,Click on Continue To Shop")
                   conn.commit()
        


        
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = 'Login User'
        self.logf.pack()
    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.address.set('')
        self.phone.set('')
        self.email.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def up(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.logf.pack_forget()
        self.head['text'] = 'Forgot Password ?'
        self.upf.pack()
    
        
    def widgets(self):
        self.head = Label(self.master,text = 'LOGIN USER',bg='yellow',font = ('',35),pady = 10)
        self.head.pack(expand=1,fill=tk.X)
        self.logf = Frame(self.master,bg='yellow',padx =10,pady = 10)
        Label(self.logf,text = 'Username: ',font = ('',20),bg='yellow',pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.logf,text = 'Password: ',font = ('',20),bg='yellow',pady=5,padx=5).grid(sticky = W)
        Entry(self.logf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.logf,text = ' Login ',bd = 5 ,font = ('',15),width=16,bg='blue',fg='white',padx=5,pady=5,command=self.login).grid()
        Button(self.logf,text = ' Create Account ',bd = 5 ,font = ('',15),width=16,bg='blue',fg='white',padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        Button(self.logf,text = ' forgot password ? ',bd = 5 ,font = ('',15),width=16,bg='blue',fg='white',padx=5,pady=5,command=self.up).grid(row=2,column=2)
        self.logf.pack(expand=1,fill=tk.X)
        
        self.crf = Frame(self.master,bg='blue',padx =10,pady = 10)
        Label(self.crf,text = 'Username: ',font = ('',20),bg='blue',fg='white',pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.crf,text = 'Password: ',font = ('',20),bg='blue',fg='white',pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.n_password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Label(self.crf,text = 'Address: ',font = ('',20),bg='blue',fg='white',pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.address,bd = 5,font = ('',15)).grid(row=2,column=1)
        Label(self.crf,text = 'Phone no.: ',font = ('',20),bg='blue',fg='white',pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.phone,bd = 5,font = ('',15)).grid(row=3,column=1)
        Label(self.crf,text = 'email: ',font = ('',20),bg='blue',fg='white',pady=5,padx=5).grid(sticky = W)
        Entry(self.crf,textvariable = self.email,bd = 5,font = ('',15)).grid(row=4,column=1)
        Button(self.crf,text = 'Create Account',bd = 5 ,font = ('',15),width=16,bg='yellow',padx=5,pady=5,command=self.new_user).grid()
        Button(self.crf,text = 'Go to Login',bd = 5 ,font = ('',15),width=16,bg='yellow',padx=5,pady=5,command=self.log).grid(row=5,column=1)


        self.upf = Frame(self.master,bg='yellow',padx =10,pady = 10)
        Label(self.upf,text = 'Username: ',font = ('',20),bg='yellow',pady=5,padx=5).grid(sticky = W)
        Entry(self.upf,textvariable = self.username,bd = 5,font = ('',15)).grid(row=0,column=1)
        Label(self.upf,text = 'New Password: ',font = ('',20),bg='yellow',pady=5,padx=5).grid(sticky = W)
        Entry(self.upf,textvariable = self.password,bd = 5,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.upf,text = ' Update Your Password',bd = 5 ,font = ('',15),width=18,bg='blue',fg='white',padx=5,pady=5,command=self.update).grid(row=4,column=1)
        



        
        

class eshopi:
    def __init__(self,master):
        self.master=master
        self.master.title("E-Shopi Main Page")
        self.master.geometry("1000x800")
        self.widgets2()

    def Shoe(self):
        self.newWindow = Toplevel(self.master)
        self.app = shoes(self.newWindow)
        




    def Cloth(self):
        self.newWindow = Toplevel(self.master)
        self.app = clothes(self.newWindow)

    def Access(self):
        self.newWindow = Toplevel(self.master)
        self.app = acessories(self.newWindow)


    def Gadget(self):
        self.newWindow = Toplevel(self.master)
        self.app = gadgets(self.newWindow)

    

        
    def widgets2(self):
        self.newframe = Frame(self.master,height=800,width=9000)
        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=tk.PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\firstmain.png")
        self.lbl=tk.Label(self.c,image=self.img,height=800,width=9000).pack()
        self.b = Button(self.c,text="Shoes",bd = 10 ,width=15,font = ('',15),bg='red',fg='white',padx=5,pady=5,command=self.Shoe)
        self.b.place(x=20,y=150)
        self.b1 = Button(self.c,text="Clothes",bd = 10 ,width=15,font = ('',15),bg='green',fg='white',padx=5,pady=5,command= self.Cloth)
        self.b1.place(x=250,y=150)
        self.b2 = Button(self.c,text="Accessories",bd = 10 ,width=15,font = ('',15),bg='black',fg='white',padx=5,pady=5,command=self.Access)
        self.b2.place(x=520,y=150)
        self.b3 = Button(self.c,text="Gadgets",bd = 10 ,width=15,font = ('',15),bg='blue', fg='white',padx=5,pady=5,command=self.Gadget)
        self.b3.place(x=770,y=150)
        

        
        self.c.pack()

class shoes:
    def __init__(self,master):
        self.master=master
        self.master.title("SHOES")
        self.master.geometry("1375x950")
        self.widgets3()



    def thnku(self):
        self.newWindow = Toplevel(self.master)
        self.app = thank(self.newWindow)

        
    def ref(self):
        self.x = random.randint(10908, 500876)
        self.randomref = str(self.x)
        self.rand.set(self.randomref)

        self.cas1 = int(self.ashoe1.get())
        self.cfs1 = int(self.fshoe1.get())
        self.ces1 = int(self.eshoe1.get())
        self.cas2 = int(self.ashoe2.get())
        self.cfs2 = int(self.fshoe2.get())
        self.ces2 = int(self.eshoe2.get())
        self.cas3 = int(self.ashoe3.get())
        self.cfs3 = int(self.fshoe3.get())
        self.ces3 = int(self.eshoe3.get())
        self.cas4 = int(self.ashoe4.get())
        self.cfs4 = int(self.fshoe4.get())
        self.ces4 = int(self.eshoe4.get())
        self.cas5 = int(self.ashoe5.get())
        self.cfs5 = int(self.fshoe5.get())
        self.ces5 = int(self.eshoe5.get())
        self.cas6 = int(self.ashoe6.get())
        self.cfs6 = int(self.fshoe6.get())
        self.ces6 = int(self.eshoe6.get())

        self.Cas1 = self.cas1 * 300
        self.Cfs1 = self.cfs1 * 400
        self.Ces1 = self.ces1 * 500
        self.Cas2 = self.cas2 * 150
        self.Cfs2 = self.cfs2 * 200
        self.Ces2 = self.ces2 * 250
        self.Cas3 = self.cas3 * 600
        self.Cfs3 = self.cfs3 * 700
        self.Ces3 = self.ces3 * 800
        self.Cas4 = self.cas4 * 200
        self.Cfs4 = self.cfs4 * 300
        self.Ces4 = self.ces4 * 400
        self.Cas5 = self.cas5 * 800
        self.Cfs5 = self.cfs5 * 900
        self.Ces5 = self.ces5 * 1000
        self.Cas6 = self.cas6 * 100
        self.Cfs6 = self.cfs6 * 200
        
        self.Ces6 = self.ces6 * 300

        self.costofproducts = "Rs.",str('%.2f' % (self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6))
        self.Cgst =  ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/10) 
        self.Sgst  = ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/12)
        self.totalcost =(self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)
        self.overallcost = "Rs.",str('%.2f' %(self.Cgst+self.Sgst+self.totalcost))

        self.cgst.set(self.Cgst)
        self.sgst.set(self.Sgst)
        self.total.set(self.totalcost)
        self.mTotal.set(self.overallcost)

        s1=self.total.get()
        s2=self.cgst.get()
        s3=self.sgst.get()
        s4=self.mTotal.get()
        s5=self.rand.get()
        s6=self.localtime
        


        self.txtreciept=Text(self.c,bg="white",width=41,height=17.5)
        self.txtreciept.place(x=1000,y=350)
        self.txtreciept.insert("1.0", '\t******BILL RECIEPT*******\n')
        self.txtreciept.insert("2.0", 'Transaction ID:'+s5+"\n")
        self.txtreciept.insert("3.0", 'Total Cost:'+s4+"\n")
        self.txtreciept.insert("4.0", 'CGST:'+s2+"\n")
        self.txtreciept.insert("5.0", 'SGST:'+s3+"\n")
        self.txtreciept.insert("6.0", 'Order Date And Time is:'+s6+"\n")
        self.txtreciept.insert("7.0", 'Thank You For Ordering And Your Product Will Be Delivered in 3 To 4 Days')
        
        


        


        

       

    def exit(self):
            self.master.destroy()


    def reset(self):
       self.rand.set('')
       self.ashoe1.set('0')
       self.fshoe1.set('0')
       self.eshoe1.set('0')
       self.ashoe2.set('0')
       self.fshoe2.set('0')
       self.eshoe2.set('0')
       self.ashoe3.set('0')
       self.fshoe3.set('0')
       self.eshoe3.set('0')
       self.ashoe4.set('0')
       self.fshoe4.set('0')
       self.eshoe4.set('0')
       self.ashoe5.set('0')
       self.fshoe5.set('0')
       self.eshoe5.set('0')
       self.ashoe6.set('0')
       self.fshoe6.set('0')
       self.eshoe6.set('0')
       self.total.set('')
       self.cgst.set('')
       self.sgst.set('')
       self.mTotal.set('')
       self.txtreciept.destroy()
       

        
    def widgets3(self):
        
        self.rand = StringVar()
        self.ashoe1 = StringVar()
        self.fshoe1 = StringVar()
        self.eshoe1 = StringVar()
        self.ashoe2 = StringVar()
        self.fshoe2 = StringVar()
        self.eshoe2 = StringVar()
        self.ashoe3 = StringVar()
        self.fshoe3 = StringVar()
        self.eshoe3 = StringVar()
        self.ashoe4 = StringVar()
        self.fshoe4 = StringVar()
        self.eshoe4 = StringVar()
        self.ashoe5 = StringVar()
        self.fshoe5 = StringVar()
        self.eshoe5 = StringVar()
        self.ashoe6 = StringVar()
        self.fshoe6 = StringVar()
        self.eshoe6 = StringVar()
        self.total = StringVar()
        self.cgst = StringVar()
        self.sgst = StringVar()
        self.mTotal = StringVar()
        


        self.ashoe1.set('0')
        self.fshoe1.set('0')
        self.eshoe1.set('0')
        self.ashoe2.set('0')
        self.fshoe2.set('0')
        self.eshoe2.set('0')
        self.ashoe3.set('0')
        self.fshoe3.set('0')
        self.eshoe3.set('0')
        self.ashoe4.set('0')
        self.fshoe4.set('0')
        self.eshoe4.set('0')
        self.ashoe5.set('0')
        self.fshoe5.set('0')
        self.eshoe5.set('0')
        self.ashoe6.set('0')
        self.fshoe6.set('0')
        self.eshoe6.set('0')

        self.localtime=time.asctime(time.localtime(time.time()))
        
        

        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\shoe.png")
        self.lbl=Label(self.c,image=self.img,height=700,width=980)
        self.lbl.place(x=0,y=0)


        self.shoe1a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1a.place(x=180,y=330)
        self.shoe1f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1f.place(x=180,y=365)
        self.shoe1e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1e.place(x=180,y=400)
        self.shoe2a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2a.place(x=480,y=330)
        self.shoe2f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2f.place(x=480,y=365)
        self.shoe2e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2e.place(x=480,y=400)
        self.shoe3a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3a.place(x=820,y=330)
        self.shoe3f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3f.place(x=820,y=365)
        self.shoe3e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3e.place(x=820,y=400)
        self.shoe4a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4a.place(x=165,y=570)
        self.shoe4f=Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4f.place(x=165,y=600)
        self.shoe4e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4e.place(x=165,y=630)
        self.shoe5a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5a.place(x=480,y=570)
        self.shoe5f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5f.place(x=480,y=600)
        self.shoe5e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5e.place(x=480,y=630)
        self.shoe6a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6a.place(x=820,y=570)
        self.shoe6f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6f.place(x=820,y=600)
        self.shoe6e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6e.place(x=820,y=630)

        

        self.lblreference = Label(self.c,font=("arial",13,"bold"),text = "Transaction Id",bg="deep sky blue",fg="white")
        self.lblreference.place(x=1020,y=52)
        self.txtreference = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Transaction Id",textvariable=self.rand,insertwidth=4,bg="white",justify='left')
        self.txtreference.place(x=1150,y=50)

        self.lbltotal = Label(self.c,font=("arial",13,"bold"),text = "Total",bg="deep sky blue",fg="white")
        self.lbltotal.place(x=1050,y=91)
        self.txttotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Total",textvariable=self.total,insertwidth=4,bg="white",justify='left')
        self.txttotal.place(x=1150,y=89)

        self.lblcgst = Label(self.c,font=("arial",13,"bold"),text = "Cgst ",bg="deep sky blue",fg="white")
        self.lblcgst.place(x=1050,y=131)
        self.txtcgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Cgst",textvariable=self.cgst,insertwidth=4,bg="white",justify='left')
        self.txtcgst.place(x=1150,y=129)

        self.lblsgst = Label(self.c,font=("arial",13,"bold"),text = "Sgst",bg="deep sky blue",fg="white")
        self.lblsgst.place(x=1050,y=171)
        self.txtsgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Sgst",textvariable=self.sgst,insertwidth=4,bg="white",justify='left')
        self.txtsgst.place(x=1150,y=169)

        self.lblmtotal = Label(self.c,font=("arial",13,"bold"),text = "Main Total",bg="deep sky blue",fg="white")
        self.lblmtotal.place(x=1050,y=211)
        self.txtmtotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Main Total",textvariable=self.mTotal,insertwidth=4,bg="white",justify='left')
        self.txtmtotal.place(x=1150,y=209)

        self.lbltime = Label(self.c,font=("arial",12,"bold"),text =self.localtime,bg="deep sky blue",fg="white")
        self.lbltime.place(x=1050,y=249)

        self.btntotal= Button(self.c, text=" BUY",bd = 6 ,font = ('',13), bg="green",width=16, fg="white",padx=5,pady=5,command=self.ref)
        self.btntotal.place(x=1000,y=289)

        self.btnreset= Button(self.c, text=" RESET",bd = 6 ,font = ('',13),bg="green",width=16, fg="white",padx=5,pady=5,command=self.reset)
        self.btnreset.place(x=1160,y=289)

        self.btnexit= Button(self.c, text=" Continue Shopping",bd = 6 ,font = ('',12),bg="green", fg="white",padx=5,pady=5,command=self.exit)
        self.btnexit.place(x=1000,y=643)

        self.btnexit= Button(self.c, text=" End Shopping",bd = 6 ,font = ('',12),bg="green",width=16, fg="white",padx=5,pady=5,command=self.thnku)
        self.btnexit.place(x=1160,y=643)
        
        self.c.pack()



         
class clothes:
    def __init__(self,master):
        self.master=master
        self.master.title("CLOTHES")
        self.master.geometry("1375x950")
        self.widgets3()

    def thnku(self):
        self.newWindow = Toplevel(self.master)
        self.app = thank(self.newWindow)

        
    def ref(self):
        self.x = random.randint(10908, 500876)
        self.randomref = str(self.x)
        self.rand.set(self.randomref)

        self.cas1 = int(self.acl1.get())
        self.cfs1 = int(self.fcl1.get())
        self.ces1 = int(self.ecl1.get())
        self.cas2 = int(self.acl2.get())
        self.cfs2 = int(self.fcl2.get())
        self.ces2 = int(self.ecl2.get())
        self.cas3 = int(self.acl3.get())
        self.cfs3 = int(self.fcl3.get())
        self.ces3 = int(self.ecl3.get())
        self.cas4 = int(self.acl4.get())
        self.cfs4 = int(self.fcl4.get())
        self.ces4 = int(self.ecl4.get())
        self.cas5 = int(self.acl5.get())
        self.cfs5 = int(self.fcl5.get())
        self.ces5 = int(self.ecl5.get())
        self.cas6 = int(self.acl6.get())
        self.cfs6 = int(self.fcl6.get())
        self.ces6 = int(self.ecl6.get())

        self.Cas1 = self.cas1 * 499
        self.Cfs1 = self.cfs1 * 580
        self.Ces1 = self.ces1 * 599
        self.Cas2 = self.cas2 * 999
        self.Cfs2 = self.cfs2 * 1200
        self.Ces2 = self.ces2 * 800
        self.Cas3 = self.cas3 * 505
        self.Cfs3 = self.cfs3 * 650
        self.Ces3 = self.ces3 * 599
        self.Cas4 = self.cas4 * 1895
        self.Cfs4 = self.cfs4 * 1200
        self.Ces4 = self.ces4 * 1499
        self.Cas5 = self.cas5 * 1500
        self.Cfs5 = self.cfs5 * 1350
        self.Ces5 = self.ces5 * 1299
        self.Cas6 = self.cas6 * 560
        self.Cfs6 = self.cfs6 * 600
        
        self.Ces6 = self.ces6 * 650

        self.costofproducts = "Rs.",str('%.2f' % (self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6))
        self.Cgst =  ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/10) 
        self.Sgst  = ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/12)
        self.totalcost =(self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)
        self.overallcost = "Rs.",str('%.2f' %(self.Cgst+self.Sgst+self.totalcost))

        self.cgst.set(self.Cgst)
        self.sgst.set(self.Sgst)
        self.total.set(self.totalcost)
        self.mTotal.set(self.overallcost)

        s1=self.total.get()
        s2=self.cgst.get()
        s3=self.sgst.get()
        s4=self.mTotal.get()
        s5=self.rand.get()
        s6=self.localtime
        


        self.txtreciept=Text(self.c,bg="white",width=41,height=17.5)
        self.txtreciept.place(x=1000,y=350)
        self.txtreciept.insert("1.0", '\t******BILL RECIEPT*******\n')
        self.txtreciept.insert("2.0", 'Transaction ID:'+s5+"\n")
        self.txtreciept.insert("3.0", 'Total Cost:'+s4+"\n")
        self.txtreciept.insert("4.0", 'CGST:'+s2+"\n")
        self.txtreciept.insert("5.0", 'SGST:'+s3+"\n")
        self.txtreciept.insert("6.0", 'Order Date And Time is:'+s6+"\n")
        self.txtreciept.insert("7.0", 'Thank You For Ordering And Your Product Will Be Delivered in 3 To 4 Days')
        
        


        


        

       

    def exit(self):
            self.master.destroy()


    def reset(self):
       self.rand.set('')
       self.acl1.set('0')
       self.fcl1.set('0')
       self.ecl1.set('0')
       self.acl2.set('0')
       self.fcl2.set('0')
       self.ecl2.set('0')
       self.acl3.set('0')
       self.fcl3.set('0')
       self.ecl3.set('0')
       self.acl4.set('0')
       self.fcl4.set('0')
       self.ecl4.set('0')
       self.acl5.set('0')
       self.fcl5.set('0')
       self.ecl5.set('0')
       self.acl6.set('0')
       self.fcl6.set('0')
       self.ecl6.set('0')
       self.total.set('')
       self.cgst.set('')
       self.sgst.set('')
       self.mTotal.set('')
       self.txtreciept.destroy()
       

        
    def widgets3(self):
        
        self.rand = StringVar()
        self.acl1 = StringVar()
        self.fcl1 = StringVar()
        self.ecl1 = StringVar()
        self.acl2 = StringVar()
        self.fcl2 = StringVar()
        self.ecl2 = StringVar()
        self.acl3 = StringVar()
        self.fcl3 = StringVar()
        self.ecl3 = StringVar()
        self.acl4 = StringVar()
        self.fcl4 = StringVar()
        self.ecl4 = StringVar()
        self.acl5 = StringVar()
        self.fcl5 = StringVar()
        self.ecl5 = StringVar()
        self.acl6 = StringVar()
        self.fcl6 = StringVar()
        self.ecl6 = StringVar()
        self.total = StringVar()
        self.cgst = StringVar()
        self.sgst = StringVar()
        self.mTotal = StringVar()
        


        self.acl1.set('0')
        self.fcl1.set('0')
        self.ecl1.set('0')
        self.acl2.set('0')
        self.fcl2.set('0')
        self.ecl2.set('0')
        self.acl3.set('0')
        self.fcl3.set('0')
        self.ecl3.set('0')
        self.acl4.set('0')
        self.fcl4.set('0')
        self.ecl4.set('0')
        self.acl5.set('0')
        self.fcl5.set('0')
        self.ecl5.set('0')
        self.acl6.set('0')
        self.fcl6.set('0')
        self.ecl6.set('0')

        self.localtime=time.asctime(time.localtime(time.time()))
        
        

        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\clothesf.png")
        self.lbl=Label(self.c,image=self.img,height=700,width=980)
        self.lbl.place(x=0,y=0)


        self.cl1a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl1,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl1a.place(x=180,y=330)
        self.cl1f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl1,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl1f.place(x=180,y=365)
        self.cl1e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl1,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl1e.place(x=180,y=400)
        self.cl2a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl2,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl2a.place(x=480,y=330)
        self.cl2f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl2,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl2f.place(x=480,y=365)
        self.cl2e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl2,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl2e.place(x=480,y=400)
        self.cl3a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl3,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl3a.place(x=820,y=330)
        self.cl3f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl3,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl3f.place(x=820,y=365)
        self.cl3e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl3,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl3e.place(x=820,y=400)
        self.cl4a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl4,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl4a.place(x=165,y=600)
        self.cl4f=Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl4,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl4f.place(x=165,y=635)
        self.cl4e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl4,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl4e.place(x=165,y=670)
        self.cl5a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl5,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl5a.place(x=480,y=600)
        self.cl5f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl5,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl5f.place(x=480,y=635)
        self.cl5e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl5,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl5e.place(x=480,y=670)
        self.cl6a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.acl6,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl6a.place(x=820,y=600)
        self.cl6f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fcl6,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl6f.place(x=820,y=635)
        self.cl6e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ecl6,insertwidth=1,bg="white",fg="black",justify='left')
        self.cl6e.place(x=820,y=670)

        

        self.lblreference = Label(self.c,font=("arial",13,"bold"),text = "Transaction Id",bg="deep sky blue",fg="white")
        self.lblreference.place(x=1020,y=52)
        self.txtreference = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Transaction Id",textvariable=self.rand,insertwidth=4,bg="white",justify='left')
        self.txtreference.place(x=1150,y=50)

        self.lbltotal = Label(self.c,font=("arial",13,"bold"),text = "Total",bg="deep sky blue",fg="white")
        self.lbltotal.place(x=1050,y=91)
        self.txttotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Total",textvariable=self.total,insertwidth=4,bg="white",justify='left')
        self.txttotal.place(x=1150,y=89)

        self.lblcgst = Label(self.c,font=("arial",13,"bold"),text = "Cgst ",bg="deep sky blue",fg="white")
        self.lblcgst.place(x=1050,y=131)
        self.txtcgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Cgst",textvariable=self.cgst,insertwidth=4,bg="white",justify='left')
        self.txtcgst.place(x=1150,y=129)

        self.lblsgst = Label(self.c,font=("arial",13,"bold"),text = "Sgst",bg="deep sky blue",fg="white")
        self.lblsgst.place(x=1050,y=171)
        self.txtsgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Sgst",textvariable=self.sgst,insertwidth=4,bg="white",justify='left')
        self.txtsgst.place(x=1150,y=169)

        self.lblmtotal = Label(self.c,font=("arial",13,"bold"),text = "Main Total",bg="deep sky blue",fg="white")
        self.lblmtotal.place(x=1050,y=211)
        self.txtmtotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Main Total",textvariable=self.mTotal,insertwidth=4,bg="white",justify='left')
        self.txtmtotal.place(x=1150,y=209)

        self.lbltime = Label(self.c,font=("arial",12,"bold"),text =self.localtime,bg="deep sky blue",fg="white")
        self.lbltime.place(x=1050,y=249)

        self.btntotal= Button(self.c, text=" BUY",bd = 6 ,font = ('',13), bg="green",width=16, fg="white",padx=5,pady=5,command=self.ref)
        self.btntotal.place(x=1000,y=289)

        self.btnreset= Button(self.c, text=" RESET",bd = 6 ,font = ('',13),bg="green",width=16, fg="white",padx=5,pady=5,command=self.reset)
        self.btnreset.place(x=1160,y=289)

        self.btnexit= Button(self.c, text=" Continue Shopping",bd = 6 ,font = ('',12),bg="green", fg="white",padx=5,pady=5,command=self.exit)
        self.btnexit.place(x=1000,y=643)

        self.btnexit= Button(self.c, text=" End Shopping",bd = 6 ,font = ('',12),bg="green",width=16, fg="white",padx=5,pady=5,command=self.thnku)
        self.btnexit.place(x=1160,y=643)
        
        self.c.pack()


class acessories:
    def __init__(self,master):
        self.master=master
        self.master.title("ACCESSORIES")
        self.master.geometry("1375x950")
        self.widgets3()
        
    def thnku(self):
        self.newWindow = Toplevel(self.master)
        self.app = thank(self.newWindow)

        
    def ref(self):
        self.x = random.randint(10908, 500876)
        self.randomref = str(self.x)
        self.rand.set(self.randomref)

        self.cas1 = int(self.ashoe1.get())
        self.cfs1 = int(self.fshoe1.get())
        self.ces1 = int(self.eshoe1.get())
        self.cas2 = int(self.ashoe2.get())
        self.cfs2 = int(self.fshoe2.get())
        self.ces2 = int(self.eshoe2.get())
        self.cas3 = int(self.ashoe3.get())
        self.cfs3 = int(self.fshoe3.get())
        self.ces3 = int(self.eshoe3.get())
        self.cas4 = int(self.ashoe4.get())
        self.cfs4 = int(self.fshoe4.get())
        self.ces4 = int(self.eshoe4.get())
        self.cas5 = int(self.ashoe5.get())
        self.cfs5 = int(self.fshoe5.get())
        self.ces5 = int(self.eshoe5.get())
        self.cas6 = int(self.ashoe6.get())
        self.cfs6 = int(self.fshoe6.get())
        self.ces6 = int(self.eshoe6.get())

        self.Cas1 = self.cas1 * 2000
        self.Cfs1 = self.cfs1 * 2500
        self.Ces1 = self.ces1 * 2300
        self.Cas2 = self.cas2 * 199
        self.Cfs2 = self.cfs2 * 2500
        self.Ces2 = self.ces2 * 190
        self.Cas3 = self.cas3 * 2000
        self.Cfs3 = self.cfs3 * 2508
        self.Ces3 = self.ces3 * 2100
        self.Cas4 = self.cas4 * 450
        self.Cfs4 = self.cfs4 * 259
        self.Ces4 = self.ces4 * 230
        self.Cas5 = self.cas5 * 200
        self.Cfs5 = self.cfs5 * 250
        self.Ces5 = self.ces5 * 230
        self.Cas6 = self.cas6 * 450
        self.Cfs6 = self.cfs6 * 320
        
        self.Ces6 = self.ces6 * 400

        self.costofproducts = "Rs.",str('%.2f' % (self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6))
        self.Cgst =  ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/10) 
        self.Sgst  = ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/12)
        self.totalcost =(self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)
        self.overallcost = "Rs.",str('%.2f' %(self.Cgst+self.Sgst+self.totalcost))

        self.cgst.set(self.Cgst)
        self.sgst.set(self.Sgst)
        self.total.set(self.totalcost)
        self.mTotal.set(self.overallcost)

        s1=self.total.get()
        s2=self.cgst.get()
        s3=self.sgst.get()
        s4=self.mTotal.get()
        s5=self.rand.get()
        s6=self.localtime
        


        self.txtreciept=Text(self.c,bg="white",width=41,height=17.5)
        self.txtreciept.place(x=1000,y=350)
        self.txtreciept.insert("1.0", '\t******BILL RECIEPT*******\n')
        self.txtreciept.insert("2.0", 'Transaction ID:'+s5+"\n")
        self.txtreciept.insert("3.0", 'Total Cost:'+s4+"\n")
        self.txtreciept.insert("4.0", 'CGST:'+s2+"\n")
        self.txtreciept.insert("5.0", 'SGST:'+s3+"\n")
        self.txtreciept.insert("6.0", 'Order Date And Time is:'+s6+"\n")
        self.txtreciept.insert("7.0", 'Thank You For Ordering And Your Product Will Be Delivered in 3 To 4 Days')
        
        


        


        

       

    def exit(self):
            self.master.destroy()


    def reset(self):
       self.rand.set('')
       self.ashoe1.set('0')
       self.fshoe1.set('0')
       self.eshoe1.set('0')
       self.ashoe2.set('0')
       self.fshoe2.set('0')
       self.eshoe2.set('0')
       self.ashoe3.set('0')
       self.fshoe3.set('0')
       self.eshoe3.set('0')
       self.ashoe4.set('0')
       self.fshoe4.set('0')
       self.eshoe4.set('0')
       self.ashoe5.set('0')
       self.fshoe5.set('0')
       self.eshoe5.set('0')
       self.ashoe6.set('0')
       self.fshoe6.set('0')
       self.eshoe6.set('0')
       self.total.set('')
       self.cgst.set('')
       self.sgst.set('')
       self.mTotal.set('')
       self.txtreciept.destroy()
       

        
    def widgets3(self):
        
        self.rand = StringVar()
        self.ashoe1 = StringVar()
        self.fshoe1 = StringVar()
        self.eshoe1 = StringVar()
        self.ashoe2 = StringVar()
        self.fshoe2 = StringVar()
        self.eshoe2 = StringVar()
        self.ashoe3 = StringVar()
        self.fshoe3 = StringVar()
        self.eshoe3 = StringVar()
        self.ashoe4 = StringVar()
        self.fshoe4 = StringVar()
        self.eshoe4 = StringVar()
        self.ashoe5 = StringVar()
        self.fshoe5 = StringVar()
        self.eshoe5 = StringVar()
        self.ashoe6 = StringVar()
        self.fshoe6 = StringVar()
        self.eshoe6 = StringVar()
        self.total = StringVar()
        self.cgst = StringVar()
        self.sgst = StringVar()
        self.mTotal = StringVar()
        


        self.ashoe1.set('0')
        self.fshoe1.set('0')
        self.eshoe1.set('0')
        self.ashoe2.set('0')
        self.fshoe2.set('0')
        self.eshoe2.set('0')
        self.ashoe3.set('0')
        self.fshoe3.set('0')
        self.eshoe3.set('0')
        self.ashoe4.set('0')
        self.fshoe4.set('0')
        self.eshoe4.set('0')
        self.ashoe5.set('0')
        self.fshoe5.set('0')
        self.eshoe5.set('0')
        self.ashoe6.set('0')
        self.fshoe6.set('0')
        self.eshoe6.set('0')

        self.localtime=time.asctime(time.localtime(time.time()))
        
        

        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\accessoriesf.png")
        self.lbl=Label(self.c,image=self.img,height=700,width=980)
        self.lbl.place(x=0,y=0)


        self.shoe1a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1a.place(x=160,y=335)
        self.shoe1f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1f.place(x=160,y=370)
        self.shoe1e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1e.place(x=160,y=405)
        self.shoe2a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2a.place(x=480,y=330)
        self.shoe2f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2f.place(x=480,y=365)
        self.shoe2e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2e.place(x=480,y=400)
        self.shoe3a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3a.place(x=820,y=335)
        self.shoe3f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3f.place(x=820,y=370)
        self.shoe3e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3e.place(x=820,y=405)
        self.shoe4a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4a.place(x=165,y=580)
        self.shoe4f=Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4f.place(x=165,y=615)
        self.shoe4e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4e.place(x=165,y=650)
        self.shoe5a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5a.place(x=480,y=580)
        self.shoe5f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5f.place(x=480,y=615)
        self.shoe5e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5e.place(x=480,y=650)
        self.shoe6a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6a.place(x=820,y=580)
        self.shoe6f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6f.place(x=820,y=615)
        self.shoe6e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6e.place(x=820,y=650)

        

        self.lblreference = Label(self.c,font=("arial",13,"bold"),text = "Transaction Id",bg="deep sky blue",fg="white")
        self.lblreference.place(x=1020,y=52)
        self.txtreference = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Transaction Id",textvariable=self.rand,insertwidth=4,bg="white",justify='left')
        self.txtreference.place(x=1150,y=50)

        self.lbltotal = Label(self.c,font=("arial",13,"bold"),text = "Total",bg="deep sky blue",fg="white")
        self.lbltotal.place(x=1050,y=91)
        self.txttotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Total",textvariable=self.total,insertwidth=4,bg="white",justify='left')
        self.txttotal.place(x=1150,y=89)

        self.lblcgst = Label(self.c,font=("arial",13,"bold"),text = "Cgst ",bg="deep sky blue",fg="white")
        self.lblcgst.place(x=1050,y=131)
        self.txtcgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Cgst",textvariable=self.cgst,insertwidth=4,bg="white",justify='left')
        self.txtcgst.place(x=1150,y=129)

        self.lblsgst = Label(self.c,font=("arial",13,"bold"),text = "Sgst",bg="deep sky blue",fg="white")
        self.lblsgst.place(x=1050,y=171)
        self.txtsgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Sgst",textvariable=self.sgst,insertwidth=4,bg="white",justify='left')
        self.txtsgst.place(x=1150,y=169)

        self.lblmtotal = Label(self.c,font=("arial",13,"bold"),text = "Main Total",bg="deep sky blue",fg="white")
        self.lblmtotal.place(x=1050,y=211)
        self.txtmtotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Main Total",textvariable=self.mTotal,insertwidth=4,bg="white",justify='left')
        self.txtmtotal.place(x=1150,y=209)

        self.lbltime = Label(self.c,font=("arial",12,"bold"),text =self.localtime,bg="deep sky blue",fg="white")
        self.lbltime.place(x=1050,y=249)

        self.btntotal= Button(self.c, text=" BUY",bd = 6 ,font = ('',13), bg="green",width=16, fg="white",padx=5,pady=5,command=self.ref)
        self.btntotal.place(x=1000,y=289)

        self.btnreset= Button(self.c, text=" RESET",bd = 6 ,font = ('',13),bg="green",width=16, fg="white",padx=5,pady=5,command=self.reset)
        self.btnreset.place(x=1160,y=289)

        self.btnexit= Button(self.c, text=" Continue Shopping",bd = 6 ,font = ('',12),bg="green", fg="white",padx=5,pady=5,command=self.exit)
        self.btnexit.place(x=1000,y=643)

        self.btnexit= Button(self.c, text=" End Shopping",bd = 6 ,font = ('',12),bg="green",width=16, fg="white",padx=5,pady=5,command=self.thnku)
        self.btnexit.place(x=1160,y=643)
        
        self.c.pack()
        
        

class gadgets:
    def __init__(self,master):
        self.master=master
        self.master.title("GADGETS")
        self.master.geometry("1375x950")
        self.widgets3()

    def thnku(self):
        self.newWindow = Toplevel(self.master)
        self.app = thank(self.newWindow)

        
    def ref(self):
        self.x = random.randint(10908, 500876)
        self.randomref = str(self.x)
        self.rand.set(self.randomref)

        self.cas1 = int(self.ashoe1.get())
        self.cfs1 = int(self.fshoe1.get())
        self.ces1 = int(self.eshoe1.get())
        self.cas2 = int(self.ashoe2.get())
        self.cfs2 = int(self.fshoe2.get())
        self.ces2 = int(self.eshoe2.get())
        self.cas3 = int(self.ashoe3.get())
        self.cfs3 = int(self.fshoe3.get())
        self.ces3 = int(self.eshoe3.get())
        self.cas4 = int(self.ashoe4.get())
        self.cfs4 = int(self.fshoe4.get())
        self.ces4 = int(self.eshoe4.get())
        self.cas5 = int(self.ashoe5.get())
        self.cfs5 = int(self.fshoe5.get())
        self.ces5 = int(self.eshoe5.get())
        self.cas6 = int(self.ashoe6.get())
        self.cfs6 = int(self.fshoe6.get())
        self.ces6 = int(self.eshoe6.get())

        self.Cas1 = self.cas1 * 60000
        self.Cfs1 = self.cfs1 * 65000
        self.Ces1 = self.ces1 * 65999
        self.Cas2 = self.cas2 * 199000
        self.Cfs2 = self.cfs2 * 190000
        self.Ces2 = self.ces2 * 100000
        self.Cas3 = self.cas3 * 30090
        self.Cfs3 = self.cfs3 * 35700
        self.Ces3 = self.ces3 * 37800
        self.Cas4 = self.cas4 * 19900
        self.Cfs4 = self.cfs4 * 1999
        self.Ces4 = self.ces4 * 19990
        self.Cas5 = self.cas5 * 20000
        self.Cfs5 = self.cfs5 * 19990
        self.Ces5 = self.ces5 * 21345
        self.Cas6 = self.cas6 * 35000
        self.Cfs6 = self.cfs6 * 25000
        
        self.Ces6 = self.ces6 * 25999

        self.costofproducts = "Rs.",str('%.2f' % (self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6))
        self.Cgst =  ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/10) 
        self.Sgst  = ((self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)/12)
        self.totalcost =(self.Cas1+self.Cfs1+self.Ces1+self.Cas2+self.Cfs2+self.Ces2+self.Cas3+self.Cfs3+self.Ces3+self.Cas4+self.Cfs4+self.Ces4+self.Cas5+self.Cfs5+self.Ces5+self.Cas6+self.Cfs6+self.Ces6)
        self.overallcost = "Rs.",str('%.2f' %(self.Cgst+self.Sgst+self.totalcost))

        self.cgst.set(self.Cgst)
        self.sgst.set(self.Sgst)
        self.total.set(self.totalcost)
        self.mTotal.set(self.overallcost)

        s1=self.total.get()
        s2=self.cgst.get()
        s3=self.sgst.get()
        s4=self.mTotal.get()
        s5=self.rand.get()
        s6=self.localtime
        


        self.txtreciept=Text(self.c,bg="white",width=41,height=17.5)
        self.txtreciept.place(x=1000,y=350)
        self.txtreciept.insert("1.0", '\t******BILL RECIEPT*******\n')
        self.txtreciept.insert("2.0", 'Transaction ID:'+s5+"\n")
        self.txtreciept.insert("3.0", 'Total Cost:'+s4+"\n")
        self.txtreciept.insert("4.0", 'CGST:'+s2+"\n")
        self.txtreciept.insert("5.0", 'SGST:'+s3+"\n")
        self.txtreciept.insert("6.0", 'Order Date And Time is:'+s6+"\n")
        self.txtreciept.insert("7.0", 'Thank You For Ordering And Your Product Will Be Delivered in 3 To 4 Days')
        
        


        


        

       

    def exit(self):
            self.master.destroy()


    def reset(self):
       self.rand.set('')
       self.ashoe1.set('0')
       self.fshoe1.set('0')
       self.eshoe1.set('0')
       self.ashoe2.set('0')
       self.fshoe2.set('0')
       self.eshoe2.set('0')
       self.ashoe3.set('0')
       self.fshoe3.set('0')
       self.eshoe3.set('0')
       self.ashoe4.set('0')
       self.fshoe4.set('0')
       self.eshoe4.set('0')
       self.ashoe5.set('0')
       self.fshoe5.set('0')
       self.eshoe5.set('0')
       self.ashoe6.set('0')
       self.fshoe6.set('0')
       self.eshoe6.set('0')
       self.total.set('')
       self.cgst.set('')
       self.sgst.set('')
       self.mTotal.set('')
       self.txtreciept.destroy()
       

        
    def widgets3(self):
        
        self.rand = StringVar()
        self.ashoe1 = StringVar()
        self.fshoe1 = StringVar()
        self.eshoe1 = StringVar()
        self.ashoe2 = StringVar()
        self.fshoe2 = StringVar()
        self.eshoe2 = StringVar()
        self.ashoe3 = StringVar()
        self.fshoe3 = StringVar()
        self.eshoe3 = StringVar()
        self.ashoe4 = StringVar()
        self.fshoe4 = StringVar()
        self.eshoe4 = StringVar()
        self.ashoe5 = StringVar()
        self.fshoe5 = StringVar()
        self.eshoe5 = StringVar()
        self.ashoe6 = StringVar()
        self.fshoe6 = StringVar()
        self.eshoe6 = StringVar()
        self.total = StringVar()
        self.cgst = StringVar()
        self.sgst = StringVar()
        self.mTotal = StringVar()
        


        self.ashoe1.set('0')
        self.fshoe1.set('0')
        self.eshoe1.set('0')
        self.ashoe2.set('0')
        self.fshoe2.set('0')
        self.eshoe2.set('0')
        self.ashoe3.set('0')
        self.fshoe3.set('0')
        self.eshoe3.set('0')
        self.ashoe4.set('0')
        self.fshoe4.set('0')
        self.eshoe4.set('0')
        self.ashoe5.set('0')
        self.fshoe5.set('0')
        self.eshoe5.set('0')
        self.ashoe6.set('0')
        self.fshoe6.set('0')
        self.eshoe6.set('0')

        self.localtime=time.asctime(time.localtime(time.time()))
        
        

        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\gadgetsf.png")
        self.lbl=Label(self.c,image=self.img,height=700,width=980)
        self.lbl.place(x=0,y=0)


        self.shoe1a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1a.place(x=180,y=335)
        self.shoe1f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1f.place(x=180,y=370)
        self.shoe1e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe1,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe1e.place(x=180,y=405)
        self.shoe2a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2a.place(x=480,y=335)
        self.shoe2f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2f.place(x=480,y=370)
        self.shoe2e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe2,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe2e.place(x=480,y=405)
        self.shoe3a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3a.place(x=820,y=335)
        self.shoe3f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3f.place(x=820,y=370)
        self.shoe3e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe3,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe3e.place(x=820,y=405)
        self.shoe4a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4a.place(x=165,y=599)
        self.shoe4f=Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4f.place(x=165,y=632)
        self.shoe4e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe4,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe4e.place(x=165,y=667)
        self.shoe5a =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5a.place(x=480,y=599)
        self.shoe5f =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5f.place(x=480,y=632)
        self.shoe5e =Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe5,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe5e.place(x=480,y=667)
        self.shoe6a = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.ashoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6a.place(x=820,y=599)
        self.shoe6f = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.fshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6f.place(x=820,y=632)
        self.shoe6e = Spinbox(self.c,values=('0','1','2','3','4','5','6','7','8','9','10'),font=("arial",10,"bold"),width=15,bd=5,textvariable=self.eshoe6,insertwidth=1,bg="white",fg="black",justify='left')
        self.shoe6e.place(x=820,y=667)

        

        self.lblreference = Label(self.c,font=("arial",13,"bold"),text = "Transaction Id",bg="deep sky blue",fg="white")
        self.lblreference.place(x=1020,y=52)
        self.txtreference = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Transaction Id",textvariable=self.rand,insertwidth=4,bg="white",justify='left')
        self.txtreference.place(x=1150,y=50)

        self.lbltotal = Label(self.c,font=("arial",13,"bold"),text = "Total",bg="deep sky blue",fg="white")
        self.lbltotal.place(x=1050,y=91)
        self.txttotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Total",textvariable=self.total,insertwidth=4,bg="white",justify='left')
        self.txttotal.place(x=1150,y=89)

        self.lblcgst = Label(self.c,font=("arial",13,"bold"),text = "Cgst ",bg="deep sky blue",fg="white")
        self.lblcgst.place(x=1050,y=131)
        self.txtcgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Cgst",textvariable=self.cgst,insertwidth=4,bg="white",justify='left')
        self.txtcgst.place(x=1150,y=129)

        self.lblsgst = Label(self.c,font=("arial",13,"bold"),text = "Sgst",bg="deep sky blue",fg="white")
        self.lblsgst.place(x=1050,y=171)
        self.txtsgst = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Sgst",textvariable=self.sgst,insertwidth=4,bg="white",justify='left')
        self.txtsgst.place(x=1150,y=169)

        self.lblmtotal = Label(self.c,font=("arial",13,"bold"),text = "Main Total",bg="deep sky blue",fg="white")
        self.lblmtotal.place(x=1050,y=211)
        self.txtmtotal = Entry(self.c,font=("arial",12,"bold"),bd=5,text = "Main Total",textvariable=self.mTotal,insertwidth=4,bg="white",justify='left')
        self.txtmtotal.place(x=1150,y=209)

        self.lbltime = Label(self.c,font=("arial",12,"bold"),text =self.localtime,bg="deep sky blue",fg="white")
        self.lbltime.place(x=1050,y=249)

        self.btntotal= Button(self.c, text=" BUY",bd = 6 ,font = ('',13), bg="green",width=16, fg="white",padx=5,pady=5,command=self.ref)
        self.btntotal.place(x=1000,y=289)

        self.btnreset= Button(self.c, text=" RESET",bd = 6 ,font = ('',13),bg="green",width=16, fg="white",padx=5,pady=5,command=self.reset)
        self.btnreset.place(x=1160,y=289)

        self.btnexit= Button(self.c, text=" Continue Shopping",bd = 6 ,font = ('',12),bg="green", fg="white",padx=5,pady=5,command=self.exit)
        self.btnexit.place(x=1000,y=643)

        self.btnexit= Button(self.c, text=" End Shopping",bd = 6 ,font = ('',12),bg="green",width=16, fg="white",padx=5,pady=5,command=self.thnku)
        self.btnexit.place(x=1160,y=643)
        
        self.c.pack()


        


class thank:
    def __init__(self,master):
        self.master=master
        self.master.title("CLOTHES")
        self.master.geometry("1375x950")
        self.widgets9()
        

    def exit(self):
        root.destroy()


    def widgets9(self):
        self.c=Canvas(self.master,bg="deep sky blue",height=700,width=1200)
        self.c.pack(expand = YES, fill = BOTH)
        self.img=PhotoImage(file="C:\\Users\\HP\\Desktop\\E-Shopi\\thank.png")
        self.lbl=Label(self.c,image=self.img,height=690,width=1350)
        self.lbl.place(x=0,y=0)
        self.exitbt = Button(self.c,text="ESCAPE/EXIT",bd=10,width=10,font=("Helvetica",10,'bold'), bg="green", fg="white",padx=5,pady=5,command=self.exit).place(x=200,y=20)
        self.c.pack()
        
        
        
    

    




    
         
        
        
root = Tk()
intro(root)
root.mainloop()
