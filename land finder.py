from Tkinter import *
from tkMessageBox import *
#import random

root1=Tk()
root1.title("Land Finder")
root1.attributes('-fullscreen',True)
#======================================================================================================================================================================
#l1=PhotoImage(file="img2.gif")
#l1=Label(root1,image=l1,text='Abhinav Gaurav \n 151207 \n C.S.E. \n B1 \n +919753607277 \n abhinavgaurav001@gmail.com \n Find Land To Buy',font='Jokerman 20  ',compound=CENTE
#Button(l1, text='continue',command=cont).pack(side=BOTTOM,expand='yes')
#l1.pack()

#i1=PhotoImage(file="img2_2048.gif"9)
#i1=Label(root1,image=i1,font="Aerial 20 bold",text="        The Land Finder       " ,compound=CENTER,bd=10,fg='red')
#Button(i1,padx=16,pady=1,bd=4,fg='black',font="Arial 16 bold",width=5,command=enter).pack(anchor=CENTER)

#photo=PhotoImage(file="img2_2048.gif")
#Label(image=photo).pack(fill='both',expand='yes')
#logo = PhotoImage(file="img2_2048.gif")
#w1 = Label(root1, image=logo).pack(side="right")
#explanation = """Abhinav Gaurav \n 151207 \n C.S.E. \n B1 \n +919753607277 \n abhinavgaurav001@gmail.com \n Find Land To Buy """
#w2 = Label(root1, 
           #justify=LEFT,
           #padx = 10, 
           #text=explanation,font='Jokerman 20 ').pack(side="left")
#def enter():
    #root1=Toplevel(root2)
#    #root1.wm_iconbitmap('Entypo_e70c(2).ico')
#root1.attributes('-fullscreen',True)
#=================================================================================================================================================================
Label(root1,text='Abhinav Gaurav \n 151207 \n C.S.E. \n B1 \n +919753607277 \n abhinavgaurav001@gmail.com \n Find Land To Buy',font='Jokerman 20  ',bg='light green').pack(fill="both",expand="yes")
    

#=========================================================================================================    
def cont():
    #root=Toplevel(root1)
    root1.destroy()
    root=Tk()
    
    #root.geometry("400x250")
    #root.attributes('-fullscreen',True)
    root.wm_iconbitmap('Entypo_e70c(2).ico')
    global photo
    photo=PhotoImage(file="img2.gif")
    Label(root,image=photo).grid(row=0,column=0,rowspan=40,columnspan=4)
    import sqlite3
    con=sqlite3.Connection("kk")
    cur=con.cursor()
    con.text_factory=str
    cur.execute("create table if not exists land(lno varchar(10),Area varchar(30),Locality varchar(30),city varchar(20),oname varchar(30),Mno number)")
    root.title("BUY LAND OF YOURS CHOICE")
    Label(root,text="SELECT YOUR CITY:",font="Aerial 20 bold italic",bg='Red').grid(row=1,column=0,sticky='w')
    m=[('Land no 26','hk colony','Monikonda','Patna','Aditya',9998885552),('Land no 10','hh colony','Lohanipur','Patna','Ramesh',9459835552),('Land no 46','vc colony','Lohanipur','Patna','Ramesh',9459835552),('Land no 6','cx colony','Miyapur','Patna','Ansari',75289552879),('Land no 46','ck colony','Abias','Patna','Arjun Sarawat',8794458562)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",m)
    b=[('Land no 25','ds colony','Raysan','Ahmedabad','Jethalal',9454446552),('Land no 34','fa colony','Sargasan','Ahmedabad','Jignesh',7797446552),('Land no 16','af colony','Sector 17','Ahmedabad','Rupesh',7458796552),('Land no 11','mk colony','Chandkheda','Ahmedabad','Jethalal',94544465456)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",b)
    c=[('Land no 1','vm colony','Sector 21','Chandigarh','Gaurav Gaba',789446552),('Land no 50','mks colony','Sector 5','Chandigarh','Ramesh jhamb',789446589),('Land no 45','vms colony','Sector 17','Chandigarh','Varun Grewal ',889446552),('Land no 31','cf colony','Sector 19','Chandigarh','Ramesh Oberoi ',789245552)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",c)
    d=[('Land no 5','vks colony','Naseem Bagh','Jammu','A.K.Sharma',8558213552),('Land no 16','mvksdk','Badami Bagh','Jammu','Shyam lal',7158213552)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",d)
    e=[('Land no 2','v colony','Indra Nagar','Banglore','R.Kumar',7153246572),('Land no 16','kv colony','Devanahalli','Banglore','Apporv',7668246572),('Land no 2','sv colony','Indra Nagar','Banglore','R.Kumar',7153246572),('Land no 25','mvsm','Besavangudi','Banglore','Parth',7153246123),('Land no 21','mvss','Hennur Rode','Banglore','R.Kumar',7553786572)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",e)
    f=[('Land no 2','smv colony','Arera Colony','Gwalior','Kailash',8532146552),('Land no 8','kvm colony','Nayapura','Gwalior','Usman',8238946552),('Land no 16','sd colony','Ashoka Garden','Gwalior','Saif',7832146552),('Land no 32','ccd colony','Vijay Nagar','Gwalior','Pramendra',8556946552)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",f)
    g=[('Land no 105','gbhcolony','G.K.1','Delhi','Kabir Mehra',8256976342),('Land no 206','vvvcolony','Rohini Sector 13','Delhi','Angad Sachdeva',8656196342),('Land no 15','nbcolony','G.K.2','Delhi','Ashish Oberoi',8123976342),('Land no 6','nl colony','Malviya Nagar','Delhi','Amman Ali',9356976342),('Land no 505','ccv colony','Dwarka East','Delhi','Firoz Agarwal',9556976342)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",g)
    h=[('Land no 25','bbbcolony','Malad','Mumbai','Bilal Syed',7632496782),('Land no 602','mnj','Andheri East','Mumbai','Rishi Kumar',7532246782),('Land no 703','nngh','Bandra west','Mumbai','Ramesh Sippe',9832346782),('Land no 265','vgv colony','Andheri East','Mumbai','Eternal Exotica',8932496782)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",h)
    i=[('Land no 16','bjbcolony','Malviya Nagar','Ajmer','Vikrat Khirwar',8759366552),('Land no 19','ggcolony','Jagatpura','Ajmer','Ajay Mehra',8759389562),('Land no 28','bjb colony','Vaishali Nagar','Ajmer','Ajeet Kumar',7159389562)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",i)
    j=[('Land no 25','vh colony','Anna Nagar','Chennai','Dhanush',8154366342),('Land no 65','bhcolony','Mennambakkam','Chennai','Avik Robinson',8554324342),('Land no 25','jncolony','Anna Nagar','Chennai','M.G.Ramachandranan',8359766342)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",j)
    k=[('Land no 32','nj colony','Gomti Nagar','Kanpur','Anuj Mohan',8356846552),('Land no 52','bbj colony','Hazratganj','Kanpur','Aditya Jhaa',8356847892),('Land no 12','bjcolony','Mahanagar','Kanpur','Prakash Kumar',7556846552),('Land no 45','bh colony','Indra Nagar','Kanpur','Shashwat Singh',9556218552)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",k)
    l=[('Land no 15','mjn colony','New market','Kolkata','Byomkesh',8352786552),(' Land no 1','njj colony','New Kolkata','Kolkata','Momita Chatterjee',8352786127)]
    cur.executemany("insert into land values(?,?,?,?,?,?)",l)
    a=IntVar()
    Radiobutton(root,text='PATNA',variable=a,value=1).grid(row=2,column=0,sticky=W+N)
    Radiobutton(root,text='AHMEDABAD',variable=a,value=2).grid(row=3,column=0,sticky=W+N)
    Radiobutton(root,text='CHANDIGARH',variable=a,value=3).grid(row=4,column=0,sticky=W+N)
    Radiobutton(root,text='JAMMU',variable=a,value=4).grid(row=5,column=0,sticky=W+N)
    Radiobutton(root,text='BANGLORE',variable=a,value=5).grid(row=6,column=0,sticky=W+N)
    Radiobutton(root,text='GWALIOR',variable=a,value=6).grid(row=7,column=0,sticky=W+N)
    Radiobutton(root,text='DELHI',variable=a,value=7).grid(row=2,column=1,sticky=W+N)
    Radiobutton(root,text='MUMBAI',variable=a,value=8).grid(row=3,column=1,sticky=W+N)
    Radiobutton(root,text='AJMER',variable=a,value=9).grid(row=4,column=1,sticky=W+N)
    Radiobutton(root,text='CHENNAI',variable=a,value=10).grid(row=5,column=1,sticky=W+N)
    Radiobutton(root,text='KANPUR',variable=a,value=11).grid(row=6,column=1,sticky=W+N)
    Radiobutton(root,text='KOLKATA',variable=a,value=12).grid(row=7,column=1,sticky=W+N)


   
    def city():
        if a.get()==1:
            cur.execute("select * from land where city='Patna'")
            #z=cur.fetchall()
            #showinfo("CITY=PATNA",z)
            #print z
            ab=cur.fetchall()
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('400x400')
            cname=ab[0][0]
            cdate=ab[0][1]
            ctime=ab[0][2]
            creason=ab[0][3]
            cnumber=ab[0][4]
            croom=ab[0][5]
           # cdays=[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=ab[1][0]
                cdate=ab[1][1]
                ctime=ab[1][2]
                creason=ab[1][3]
                cnumber=ab[1][4]
                croom=ab[1][5]
               # cdays=ab[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=ab[2][0]
                cdate=ab[2][1]
                ctime=ab[2][2]
                creason=ab[2][3]
                cnumber=ab[2][4]
                croom=ab[2][5]
               # cdays=[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=ab[3][0]
                cdate=ab[3][1]
                ctime=ab[3][2]
                creason=ab[3][3]
                cnumber=ab[3][4]
                croom=ab[3][5]
              #  cdays=[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=n4).grid(row=14,column=1,sticky=E+W+N+S)

            def n4():
                master5=Tk()
               # master4.destroy()
                master5.title("Find Your Land")
                master5.wm_iconbitmap('Entypo_e70c(2).ico')
                master5.geometry('400x400')
                cname=ab[4][0]
                cdate=ab[4][1]
                ctime=ab[4][2]
                creason=ab[4][3]
                cnumber=ab[4][4]
                croom=ab[4][5]
               # cdays=[4][6]                                                                  
                Label(master5,text='Land No. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master5,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master5,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master5,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                      
                Button(master5,text='next',command=master5.destroy).grid(row=14,column=1,sticky=E+W+N+S)
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)

            #==========================================================##############################====================================================================
        elif a.get()==2:
            cur.execute("select * from land where city='Ahmedabad'")
            z=cur.fetchall()
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=z[0][0]
            cdate=z[0][1]
            ctime=z[0][2]
            creason=z[0][3]
            cnumber=z[0][4]
            croom=z[0][5]
           # cdays=[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=z[1][0]
                cdate=z[1][1]
                ctime=z[1][2]
                creason=z[1][3]
                cnumber=z[1][4]
                croom=z[1][5]
               # cdays=z[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=z[2][0]
                cdate=z[2][1]
                ctime=z[2][2]
                creason=z[2][3]
                cnumber=z[2][4]
                croom=z[2][5]
               # cdays=z[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=z[3][0]
                cdate=z[3][1]
                ctime=z[3][2]
                creason=z[3][3]
                cnumber=z[3][4]
                croom=z[3][5]
              #  cdays=z[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=master4.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #================================================#######################=====================================================================================
            #showinfo("CITY=AHMEDABAD",z)
            #print z
        elif a.get()==3:
            cur.execute("select * from  land where city='Chandigarh'")
            x=cur.fetchall()
            #showinfo("CHANDIGARH",z)
            #print x
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=x[0][0]
            cdate=x[0][1]
            ctime=x[0][2]
            creason=x[0][3]
            cnumber=x[0][4]
            croom=x[0][5]
           # cdays=x[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=x[1][0]
                cdate=x[1][1]
                ctime=x[1][2]
                creason=x[1][3]
                cnumber=x[1][4]
                croom=x[1][5]
               # cdays=x[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=x[2][0]
                cdate=x[2][1]
                ctime=x[2][2]
                creason=x[2][3]
                cnumber=x[2][4]
                croom=x[2][5]
               # cdays=x[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=x[3][0]
                cdate=x[3][1]
                ctime=x[3][2]
                creason=x[3][3]
                cnumber=x[3][4]
                croom=x[3][5]
              #  cdays=x[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=master4.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #====================================================================###################==============================================================================
            
        elif a.get()==4:
            cur.execute("select * from  land where city='Jammu'")
            c=cur.fetchall()
            #showinfo("CITY=JAMMU",z)
            #print c
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=c[0][0]
            cdate=c[0][1]
            ctime=c[0][2]
            creason=c[0][3]
            cnumber=c[0][4]
            croom=c[0][5]
           # cdays=c[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=c[1][0]
                cdate=c[1][1]
                ctime=c[1][2]
                creason=c[1][3]
                cnumber=c[1][4]
                croom=c[1][5]
               # cdays=c[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=master2.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #=====================================================####################===========================================================================
        elif a.get()==5:
            cur.execute("select * from  land where city='Banglore'")
            v=cur.fetchall()
            #showinfo("CITY=BANGLORE",z)
           # print z
    
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=v[0][0]
            cdate=v[0][1]
            ctime=v[0][2]
            creason=v[0][3]
            cnumber=v[0][4]
            croom=v[0][5]
           # cdays=[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=v[1][0]
                cdate=v[1][1]
                ctime=v[1][2]
                creason=v[1][3]
                cnumber=v[1][4]
                croom=v[1][5]
               # cdays=v[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=v[2][0]
                cdate=v[2][1]
                ctime=v[2][2]
                creason=v[2][3]
                cnumber=v[2][4]
                croom=v[2][5]
               # cdays=v[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=v[3][0]
                cdate=v[3][1]
                ctime=v[3][2]
                creason=v[3][3]
                cnumber=v[3][4]
                croom=v[3][5]
              #  cdays=v[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=n4).grid(row=14,column=1,sticky=E+W+N+S)

            def n4():
                master5=Tk()
               # master4.destroy()
                master5.title("Find Your Land")
                master5.wm_iconbitmap('Entypo_e70c(2).ico')
                master5.geometry('400x400')
                cname=v[4][0]
                cdate=v[4][1]
                ctime=v[4][2]
                creason=v[4][3]
                cnumber=v[4][4]
                croom=v[4][5]
               # cdays=v[4][6]                                                                  
                Label(master5,text='Land No. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master5,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master5,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master5,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                      
                Button(master5,text='next',command=master5.destroy).grid(row=14,column=1,sticky=E+W+N+S)
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #================================================================================================================================================
        elif a.get()==6:
            cur.execute("select * from  land where city='Gwalior'")
            q=cur.fetchall()
            #showinfo("CITY=GWALIOR",z)
            #print q
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=q[0][0]
            cdate=q[0][1]
            ctime=q[0][2]
            creason=q[0][3]
            cnumber=q[0][4]
            croom=q[0][5]
           # cdays=q[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=q[1][0]
                cdate=q[1][1]
                ctime=q[1][2]
                creason=q[1][3]
                cnumber=q[1][4]
                croom=q[1][5]
               # cdays=q[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=q[2][0]
                cdate=q[2][1]
                ctime=q[2][2]
                creason=q[2][3]
                cnumber=q[2][4]
                croom=q[2][5]
               # cdays=q[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=q[3][0]
                cdate=q[3][1]
                ctime=q[3][2]
                creason=q[3][3]
                cnumber=q[3][4]
                croom=q[3][5]
              #  cdays=[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=master4.destroy).grid(row=14,column=1,sticky=E+W+N+S)

           
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #=======================================================================================================================================================
            
        elif a.get()==7:
            cur.execute("select * from  land where city='Delhi'")
            s=cur.fetchall()
            #showinfo("CITY=DELHI",s)
            #print s
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.geometry('300x300')
            cname=s[0][0]
            cdate=s[0][1]
            ctime=s[0][2]
            creason=s[0][3]
            cnumber=s[0][4]
            croom=s[0][5]
           # cdays=s[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=s[1][0]
                cdate=s[1][1]
                ctime=s[1][2]
                creason=s[1][3]
                cnumber=s[1][4]
                croom=s[1][5]
               # cdays=s[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=s[2][0]
                cdate=s[2][1]
                ctime=s[2][2]
                creason=s[2][3]
                cnumber=s[2][4]
                croom=s[2][5]
               # cdays=s[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=s[3][0]
                cdate=s[3][1]
                ctime=s[3][2]
                creason=s[3][3]
                cnumber=s[3][4]
                croom=s[3][5]
              #  cdays=s[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=n4).grid(row=14,column=1,sticky=E+W+N+S)

            def n4():
                master5=Tk()
               # master4.destroy()
                master5.title("Find Your Land")
                master5.wm_iconbitmap('Entypo_e70c(2).ico')
                master5.geometry('400x400')
                cname=s[4][0]
                cdate=s[4][1]
                ctime=s[4][2]
                creason=s[4][3]
                cnumber=s[4][4]
                croom=s[4][5]
               # cdays=s[4][6]                                                                  
                Label(master5,text='Land No. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master5,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master5,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master5,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                      
                Button(master5,text='next',command=master5.destroy).grid(row=14,column=1,sticky=E+W+N+S)
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #======================================================================================================================================
        elif a.get()==8:
            cur.execute("select * from  land where city='Mumbai'")
            d=cur.fetchall()
            #showinfo("CITY=MUMBAI",z)
            #print z
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=d[0][0]
            cdate=d[0][1]
            ctime=d[0][2]
            creason=d[0][3]
            cnumber=d[0][4]
            croom=d[0][5]
           # cdays=d[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=d[1][0]
                cdate=d[1][1]
                ctime=d[1][2]
                creason=d[1][3]
                cnumber=d[1][4]
                croom=d[1][5]
               # cdays=d[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=d[2][0]
                cdate=d[2][1]
                ctime=d[2][2]
                creason=d[2][3]
                cnumber=d[2][4]
                croom=d[2][5]
               # cdays=d[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=d[3][0]
                cdate=d[3][1]
                ctime=d[3][2]
                creason=d[3][3]
                cnumber=d[3][4]
                croom=d[3][5]
              #  cdays=d[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=master4.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #===================================================================================================================================================
        elif a.get()==9:
            cur.execute("select * from  land where city='Ajmer'")
            m=cur.fetchall()
            #showinfo("CITY=AJMER",z)
            #print z
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=m[0][0]
            cdate=m[0][1]
            ctime=m[0][2]
            creason=m[0][3]
            cnumber=m[0][4]
            croom=m[0][5]
           # cdays=m[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=m[1][0]
                cdate=m[1][1]
                ctime=m[1][2]
                creason=m[1][3]
                cnumber=m[1][4]
                croom=m[1][5]
               # cdays=m[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=m[2][0]
                cdate=m[2][1]
                ctime=m[2][2]
                creason=m[2][3]
                cnumber=m[2][4]
                croom=m[2][5]
               # cdays=m[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=master3.destroy).grid(row=14,column=1,sticky=E+W+N+S)
            #def n3():
               # master4=Tk()
                #master3.destroy()
                #master4.title("Billing Service")
                #master4.geometry('400x400')
                #cname=m[3][0]
                #cdate=m[3][1]
                #ctime=m[3][2]
                #creason=m[3][3]
                #cnumber=m[3][4]
                #croom=m[3][5]
              #  cdays=m[3][6]                                                                  
                #Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                #Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                #Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                #Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                #Button(master4,text='next',command=n4).grid(row=14,column=1,sticky=E+W+N+S)

            #def n4():
                #master5=Tk()
               # master4.destroy()
                #master5.title("Billing Service")
                #master5.geometry('400x400')
                #cname=m[4][0]
                #cdate=m[4][1]
                #ctime=m[4][2]
                #creason=m[4][3]
                #cnumber=m[4][4]
                #croom=m[4][5]
               # cdays=m[4][6]                                                                  
                #Label(master5,text='Land No. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                #Label(master5,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                #Label(master5,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                #Label(master5,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                      
                #Button(master5,text='next',command=master5.destroy).grid(row=14,column=1,sticky=E+W+N+S)
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #=========================================================================================================================================
        elif a.get()==10:
            cur.execute("select * from  land where city='Chennai'")
            w=cur.fetchall()
            #showinfo("CITY=CHENNAI",z)
            #print z
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=w[0][0]
            cdate=w[0][1]
            ctime=w[0][2]
            creason=w[0][3]
            cnumber=w[0][4]
            croom=w[0][5]
           # cdays=w[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=w[1][0]
                cdate=w[1][1]
                ctime=w[1][2]
                creason=w[1][3]
                cnumber=w[1][4]
                croom=w[1][5]
               # cdays=w[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land ")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=w[2][0]
                cdate=w[2][1]
                ctime=w[2][2]
                creason=w[2][3]
                cnumber=w[2][4]
                croom=w[2][5]
               # cdays=w[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=master3.destroy).grid(row=14,column=1,sticky=E+W+N+S)
            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #===========================================================================================================================
        elif a.get()==11:
            cur.execute("select * from  land where city='Kanpur'")
            n=cur.fetchall()
            #showinfo("CITY=KANPUR",z)
            #print z
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=n[0][0]
            cdate=n[0][1]
            ctime=n[0][2]
            creason=n[0][3]
            cnumber=n[0][4]
            croom=n[0][5]
           # cdays=n[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=n[1][0]
                cdate=n[1][1]
                ctime=n[1][2]
                creason=n[1][3]
                cnumber=n[1][4]
                croom=n[1][5]
               # cdays=n[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=n2).grid(row=14,column=1,sticky=E+W+N+S)

            def n2():
                master3=Tk()
                #master2.destroy()
                master3.title("Find Your Land")
                master3.wm_iconbitmap('Entypo_e70c(2).ico')
                master3.geometry('400x400')
                cname=n[2][0]
                cdate=n[2][1]
                ctime=n[2][2]
                creason=n[2][3]
                cnumber=n[2][4]
                croom=n[2][5]
               # cdays=n[2][6]
                Label(master3,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master3,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master3,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master3,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                     
                Button(master3,text='next',command=n3).grid(row=14,column=1,sticky=E+W+N+S)
            def n3():
                master4=Tk()
                #master3.destroy()
                master4.title("Find Your Land")
                master4.wm_iconbitmap('Entypo_e70c(2).ico')
                master4.geometry('400x400')
                cname=n[3][0]
                cdate=n[3][1]
                ctime=n[3][2]
                creason=n[3][3]
                cnumber=n[3][4]
                croom=n[3][5]
              #  cdays=n[3][6]                                                                  
                Label(master4,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master4,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master4,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master4,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                                                                                       
                Button(master4,text='next',command=master4.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #===============================================================================================================================================
        elif a.get()==12:
            cur.execute("select * from  land where city='Kolkata'")
            g=cur.fetchall()
            #showinfo("CITY=KOLKATA",z)
            #print z
            
            master1=Tk()
            master1.title("Find Your Land")
            master1.wm_iconbitmap('Entypo_e70c(2).ico')
            master1.geometry('300x300')
            cname=g[0][0]
            cdate=g[0][1]
            ctime=g[0][2]
            creason=g[0][3]
            cnumber=g[0][4]
            croom=g[0][5]
           # cdays=g[0][6]
            def n1():
                master2=Tk()
                master1.destroy()
                master2.title("Find Your Land")
                master2.wm_iconbitmap('Entypo_e70c(2).ico')
                master2.geometry('400x400')
                cname=g[1][0]
                cdate=g[1][1]
                ctime=g[1][2]
                creason=g[1][3]
                cnumber=g[1][4]
                croom=g[1][5]
               # cdays=g[1][6]
                Label(master2,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
                Label(master2,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
                Label(master2,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
                Label(master2,text='Owner Name:'+cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
                Button(master2,text='next',command=master2.destroy).grid(row=14,column=1,sticky=E+W+N+S)

            
                    
            Label(master1,text='Land no. :'+ cname,font='Helvetica 9 bold').grid(pady=5,row=3,column=1,stick=W)
            Label(master1,text='Locality : '+cdate,font='Helvetica 9 bold').grid(padx=2,pady=5,row=4,column=1,stick=W)
            Label(master1,text='City: '+ctime,font='Helvetica 10 bold').grid(pady=5,row=5,column=1,stick=W)
            Label(master1,text='Owner Name:' +cnumber,font='Helvetica 10 bold').grid(pady=5,row=6,column=1,stick=W,columnspan=5)
            
            Button(master1,text='next',command=n1).grid(row=14,column=1,sticky=E+W+N+S)
            #======================================================================================================================================================    
   # Button(root1, text='continue',command=cont).pack(side=BOTTOM,expand='yes')    
    Button(root,text='OK',command=city).grid(row=14,column=2,sticky='ewns')
    def quit():
        quit=askyesnocancel("Quit System","Do you want to quit?")
        if quit>0:
            root.destroy()
            return
    Button(root,text='Exit',command=quit,bg='green').grid(row=16,column=2,sticky='ewns')
def quixt():
        quixt=askyesnocancel("Quit System","Do you want to quit?")
        if quixt>0:
            root1.destroy()
            return
Button(root1,text='Exit',command=quixt).pack(side=BOTTOM,expand='yes')
Button(root1, text='continue',command=cont).pack(side=BOTTOM,expand='yes')
#l1.pack()
root1.mainloop()

