import mysql.connector as con
from tkinter import Tk
from tkinter import *
import time
import plyer
from plyer import notification
from tkinter import messagebox
from matplotlib import pyplot as plt 





def l1():
    messagebox.showinfo('login info',"logined succesfully")
    login()
    submit()


def signup():
    root1= Tk()
    root1.attributes("-fullscreen",True)
    root1.config(bg="lavender")

    username=Label(root1,text='username',bg='lavender',fg='black',font=('Arial Black',20,'bold'))
    username.place(x=100,y=300)

    user_name=Entry(root1,bg='lavender',font=('Arial Black',20,'bold'))
    user_name.place(x=300,y=300)
    user_name.focus()

    password=Label(root1,text='Password',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    password.place(x=100,y=400)

    password_=Entry(root1,font=('Arial Black',20,'bold'),bg='lavender',bd=0,show="*")
    password_.place(x=300,y=400)

    age=Label(root1,text='Age',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    age.place(x=100,y=500)

    age_=Entry(root1,font=('Arial Black',20,'bold'),bg='lavender')
    age_.place(x=300,y=500)

    sub=Button(root1,text='submit',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    sub.place(x=300,y=600)

    x=con.connect(host='localhost',user='root',password='Mouse@2010',database='dhirubhai',command=submit)
    y=x.cursor()
    u=user_name.get()
    p=password_.get()
    a=age_.get()
    v=[u,p,a]
    y.execute("select * from login")
    data=y.fetchall()
    for i in data:
        if i==v:
            submit()


def login():
    x=con.connect(host='localhost',user='root',password='Mouse@2010',database='dhirubhai')
    y=x.cursor()
    u=user_name.get()
    p=password_.get()
    a=age_.get()
    y.execute("insert into login(username,password,age) values(%s,%s,%s)",(u,p,a))
    x.commit()



def goal():
    B=Tk()
    B.attributes("-fullscreen",True)
    B.config(bg='lavender')
    hg=Label(B,text="Set Health Goal",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    hg.pack()
#weight loss
    wl=Label(B,text="Do you want to do \n(Weight Loss or Muscle Gain)? ",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    wl.place(x=200,y=200)
    wl_en=Entry(B,width=40,font=('Arial Black',20,'bold'),bg='lavender')
    wl_en.place(x=600,y=200)
    d=wl_en.get()
    
    m="Age Range	Gender	Sedentary (Maintenance)	Moderately Active (Maintenance)	Active (Maintenance) \nCaloric Surplus for Muscle Gain\n10-12 years	Male	1,600-1,800 cal/day	1,800-2,200 cal/day	2,000-2,600 cal/day	+200-400 cal/day\nFemale	1,400-1,600 cal/day	1,600-1,800 cal/day	1,800-2,200 cal/day	+200-400 cal/day\n13-18 years	Male	2,000-2,400 cal/day	2,400-2,800 cal/day	2,800-3,200 cal/day	+300-500 cal/day\nFemale	1,800-2,000 cal/day	2,000-2,400 cal/day	2,400-2,800 cal/day	+300-500 cal/day\n19-30 years	Male	2,400-2,600 cal/day	2,600-2,800 cal/day	2,800-3,000 cal/day	+300-500 cal/day\nFemale	1,800-2,000 cal/day	2,000-2,400 cal/day	2,400-2,800 cal/day	+300-500 cal/day\n31-50 years	Male	2,200-2,400 cal/day	2,400-2,600 cal/day	2,600-2,800 cal/day	+200-400 cal/day\nFemale	1,800-2,000 cal/day	2,000-2,200 cal/day	2,200-2,400 cal/day	+200-400 cal/day\n51-70 years	Male	2,000-2,200 cal/day	2,200-2,400 cal/day	2,400-2,600 cal/day	+200-400 cal/day\nFemale	1,600-1,800 cal/day	1,800-2,000 cal/day	2,000-2,200 cal/day	+200-400 cal/day\n71-80 years	Male	1,800-2,000 cal/day	2,000-2,200 cal/day	2,200-2,400 cal/day	+100-300 cal/day\nFemale	1,600-1,800 cal/day	1,800-2,000 cal/day	2,000-2,200 cal/day	+100-300 cal/day"
    v="Reminder","10-12-year-old (sedentary):\nMaintenance: 1,600-2,000 cal/day\nTo lose weight: 1,100-1,500 cal/day\n19-30-year-old (moderately active):\nMaintenance: 2,000-2,600 cal/day\nTo lose weight: 1,500-2,100 cal/day\n51-70-year-old (active):\nMaintenance: 2,000-2,600 cal/day\nTo lose weight: 1,500-2,100 cal/day"
    


def submit():
    a=Tk()
    a.attributes("-fullscreen",True)
    a.config(bg="lavender")
    
  
# Show image using label 
    lm=Label(a,text="Log Meal",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    lm.pack()
#name
    nm_lm=Label(a,text="Meal Name",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    nm_lm.place(x=300,y=200)
    nm=Entry(a,bg='lavender',width=40,font=('Arial Black',18,'bold'))
    nm.place(x=500,y=200)
#calories
    c_lm=Label(a,text="Calories",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    c_lm.place(x=300,y=250)
    cm=Entry(a,bg='lavender',width=40,font=('Arial Black',18,'bold'))
    cm.place(x=500,y=250)
#proteins
    pm_lm=Label(a,text="Proteins",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    pm_lm.place(x=300,y=300)
    pm=Entry(a,width=40,bg='lavender',font=('Arial Black',18,'bold'))
    pm.place(x=500,y=300)
#fats
    fm_lm=Label(a,text="Fats",bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    fm_lm.place(x=300,y=350)
    fm=Entry(a,width=40,bg='lavender',font=('Arial Black',18,'bold'))
    fm.place(x=500,y=350)
    B=Button(a,text="Next",command=goal,bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
    B.place(x=400,y=400)
    
    sizes = [3, 2, 1]
    labels = 'Calories', 'Protiens', 'fats'
    plt.pie(sizes,labels = labels)
    plt.title('Your Analysis')
    plt.axis('equal')
    plt.show()
    
    

    
root=Tk()
root.attributes("-fullscreen",True)
root.config(bg='lavender')

bag = PhotoImage(file = "deit1.png") 
label1 = Label(root,image=bag,bd=0) 
label1.place(x = 600, y = 200)


Label(root,text='NUTRITION AND DIET PLANNER \nWITH HEALTH GOALS',bg='lavender',fg='dark blue',font=('Arial Black',28,'bold')).pack()

username=Label(root,text='username',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
username.place(x=100,y=300)

user_name=Entry(root,bg='lavender',font=('Arial Black',20,'bold'))
user_name.place(x=300,y=300)
user_name.focus()

password=Label(root,text='Password',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
password.place(x=100,y=400)

password_=Entry(root,bg='lavender',font=('Arial Black',20,'bold'),show="*")
password_.place(x=300,y=400)

age=Label(root,text='Age',bg='lavender',fg='dark blue',font=('Arial Black',20,'bold'))
age.place(x=100,y=500)

age_=Entry(root,bg='lavender',font=('Arial Black',20,'bold'))
age_.place(x=300,y=500)


b=Button(root,text="Submit",bg='lavender',fg='dark blue',font=('Arial Black',16,'bold'),bd=0,command=l1)
b.place(x=400,y=600)

s=Button(root,text="Singup",bg='lavender',fg='dark blue',font=('Arial Black',16,'bold'),bd=0,command=signup)
s.place(x=400,y=670)

root.mainloop()