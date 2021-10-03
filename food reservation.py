from tkinter import*
from tkinter import messagebox
import time
import datetime as dt
import mysql.connector
from prettytable import from_db_cursor

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="foodreservation"
)



window=Tk()
window.title("Ordering System")
window.geometry("1700x800")
window.config(bg="lavender")

label1=Label(window,text="WELCOME",bg="purple",fg="white",width=200)
label1.place(x=0,y=10)


#name n number



label2=Label(window,text="Enter customer Name",bg="purple",fg="white",width=25)
label2.place(x=20,y=80)

name=Entry(window,width=30)
name.place(x=220,y=80)

label3=Label(window,text="Enter customer Number",bg="purple",fg="white",width=25)
label3.place(x=450,y=80)

number=Entry(window,width=30)
number.place(x=650,y=80)



#burger



def click1():
    a=int(burger.get())
    b=a+1
    burger.delete(0,"end")
    burger.insert(0,b)


photo1=PhotoImage(file=r"burger11.png",height=60,width=80)
b1=Button(window,image=photo1,command=click1)
b1.place(x=20,y=200)

burger=Entry(window,width=10)
burger.place(x=150,y=225)
burger.insert(0,"0")

def rem1():
    a=int(burger.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        burger.delete(0,"end")
        burger.insert(0,b)

r1=Button(window,text="Remove",bg="red",fg="white",command=rem1)
r1.place(x=250,y=220)


#fries



def click2():
    a=int(fries.get())
    b=a+1
    fries.delete(0,"end")
    fries.insert(0,b)

photo2=PhotoImage(file=r"fries11.png",height=60,width=80)
b2=Button(window,image=photo2,command=click2)
b2.place(x=20,y=300)

fries=Entry(window,width=10)
fries.place(x=150,y=325)
fries.insert(0,"0")

def rem2(): 
    a=int(fries.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        fries.delete(0,"end")
        fries.insert(0,b)

r2=Button(window,text="Remove",bg="red",fg="white",command=rem2)
r2.place(x=250,y=320)


#pizza



def click3():
    a=int(pizza.get())
    b=a+1
    pizza.delete(0,"end")
    pizza.insert(0,b)


photo3=PhotoImage(file=r"pizza11.png",height=60,width=80)
b3=Button(window,image=photo3,command=click3)
b3.place(x=20,y=400)

pizza=Entry(window,width=10)
pizza.place(x=150,y=425)
pizza.insert(0,"0")

def rem3():
    a=int(pizza.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        pizza.delete(0,"end")
        pizza.insert(0,b)
        
r3=Button(window,text="Remove",bg="red",fg="white",command=rem3)
r3.place(x=250,y=420)


#sandwitch



def click4():
    a=int(sandwitch.get())
    b=a+1
    sandwitch.delete(0,"end")
    sandwitch.insert(0,b)

photo4=PhotoImage(file=r"sandwitch11.png",height=60,width=80)
b4=Button(window,image=photo4,command=click4)
b4.place(x=20,y=500)

sandwitch=Entry(window,width=10)
sandwitch.place(x=150,y=525)
sandwitch.insert(0,"0")

def rem4():
    a=int(sandwitch.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        sandwitch.delete(0,"end")
        sandwitch.insert(0,b)

r4=Button(window,text="Remove",bg="red",fg="white",command=rem4)
r4.place(x=250,y=520)



#subway



def click5():
    a=int(sub.get())
    b=a+1
    sub.delete(0,"end")
    sub.insert(0,b)

photo5=PhotoImage(file=r"sub11.png",height=60,width=80)
b5=Button(window,image=photo5,command=click5)
b5.place(x=20,y=600)

sub=Entry(window,width=10)
sub.place(x=150,y=625)
sub.insert(0,"0")

def rem5():
    a=int(sub.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        sub.delete(0,"end")
        sub.insert(0,b)

r5=Button(window,text="Remove",bg="red",fg="white",command=rem5)
r5.place(x=250,y=620)



#water



def click6():
    a=int(water.get())
    b=a+1
    water.delete(0,"end")
    water.insert(0,b)

photo6=PhotoImage(file=r"water11.png",height=60,width=80)
b6=Button(window,image=photo6,command=click6)
b6.place(x=450,y=200)

water=Entry(window,width=10)
water.place(x=580,y=225)
water.insert(0,"0")

def rem6():
    a=int(water.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        water.delete(0,"end")
        water.insert(0,b)
        
r6=Button(window,text="Remove",bg="red",fg="white",command=rem6)
r6.place(x=680,y=220)



#softdrink



def click7():
    a=int(softdrink.get())
    b=a+1
    softdrink.delete(0,"end")
    softdrink.insert(0,b)

photo7=PhotoImage(file=r"softdrink11.png",height=60,width=80)
b6=Button(window,image=photo7,command=click7)
b6.place(x=450,y=300)

softdrink=Entry(window,width=10)
softdrink.place(x=580,y=325)
softdrink.insert(0,"0")

def rem7():
    a=int(softdrink.get())
    if a==0:
        messagebox.showinfo("Error","Please add some items")
    else:
        b=a-1
        softdrink.delete(0,"end")
        softdrink.insert(0,b)

r7=Button(window,text="Remove",bg="red",fg="white",command=rem7)
r7.place(x=680,y=320)




#total                             #b=99,f=55,p=149,s=80,s=185,w=20,d=40



def total():                                                                                             
    a=int(burger.get())
    a1=a*99
    b=int(fries.get())
    b1=b*55
    c=int(pizza.get())
    c1=c*149
    d=int(sandwitch.get())
    d1=d*80
    e=int(sub.get())
    e1=e*185
    f=int(water.get())
    f1=f*20
    g=int(softdrink.get())
    g1=g*40
    
    global total
    total=a1+b1+c1+d1+e1+f1+g1
    totalrs.delete(0,"end")
    totalrs.insert(0,total)


    

total=Button(window,text="TOTAL",bg="yellow",fg="black",width=15,font=("bold",12),command=total)
total.place(x=480,y=400)
global totalrs
totalrs=Entry(window,width=16,font=("bold",12))
totalrs.place(x=480,y=440)



#bill



def create_window():
    n=name.get()
    no=number.get()
    a=int(burger.get())
    a1=a*99
    b=int(fries.get())
    b1=b*55
    c=int(pizza.get())
    c1=c*149
    d=int(sandwitch.get())
    d1=d*80
    e=int(sub.get())
    e1=e*185
    f=int(water.get())
    f1=f*20
    g=int(softdrink.get())
    g1=g*40
    h=totalrs.get()

    n=name.get()
    o=number.get()
    l=len(o)
    if(n==""):
        messagebox.showinfo("Error","Please enter customer name")
        totalrs.delete(0,"end")
    elif (o==""):
        messagebox.showinfo("Error","Please enter customer your number")
        totalrs.delete(0,"end")
    elif not o.isdigit():
        messagebox.showinfo("Number","Please enter numeric values.")
        totalrs.delete(0,"end")
    elif l<10 or l>10:
         messagebox.showinfo("Number","Please Check the Number.")
    elif a==0 and b==0 and c==0 and d==0 and e==0 and f==0 and g==0:
        messagebox.showinfo("Order","Please take the Order")
    elif h=="0" or h=="":
         messagebox.showinfo("Error","Please Calulate the Total first")
        
        
    else:
        global window1
        window1=Toplevel(window)
        window1.geometry("400x300")
        window1.title("Acknowledgement")
        window1.config(bg="lavender")

    xyz = Text(window1, height=9, width=30, bg="lavender", fg="black")
    xyz.place(x=60, y=80)

    


    
    if a>0:
        t2=("Burger X",a,"=",a1)

        xyz.insert(0.0,t2)
        xyz.insert("end","\n")
    else:
        pass
    
        
    if b>0:
        u2=("Fries X",b,"=",b1)
        xyz.insert("end",u2)
        xyz.insert("end","\n")
    else:
        pass
    
    if c>0:
        v=("Pizza X",c,"=",c1)
        xyz.insert("end",v)
        xyz.insert("end","\n")
    else:
        pass

    if d>0:
        w=("Sandwitch X",d,"=",d1)
        xyz.insert("end",w)
        xyz.insert("end","\n")
    else:
        pass
    
    if e>0:
        x=("Subway X",e,"=",e1)
        xyz.insert("end",x)
        xyz.insert("end","\n")
    else:
        pass
    
    if f>0:
        y=("Water X",f,"=",f1)
        xyz.insert("end",y)
        xyz.insert("end","\n")
    else:
        pass
    
    if g>0:
        z=("SoftDrink X",g,"=",g1)
        xyz.insert("end",z)
        xyz.insert("end","\n")
    else:
        pass
    
        
    t=("TOTAL=",total)
    xyz.insert("end","\n")
    xyz.insert("end",t)

    global description
    description=xyz.get(0.0,"end")
    


    ty=Label(window1,text="Thank You Visit Again")
    ty.place(x=120,y=275)
    

    date=dt.datetime.now()
    global format_date
    format_date=f"{date:%a,%b-%d-%y}"
    dateis=Label(window1,text=format_date)
    dateis.place(x=300,y=20)
    
    global abc
    abc=time.strftime("%H:%M:%S")
    timeis=Label(window1,text=abc)
    timeis.place(x=320,y=5)


    
    label=Label(window1,text="RECIEPT",fg="white",bg="purple",width=10,font=("bold",9))
    label.place(x=160,y=10)

    bname=Label(window1,text="Name:",width=5)
    bname.place(x=10,y=50)

    n1=Label(window1,text=n)
    n1.place(x=70,y=50)

    bno=Label(window1,text="Number:",width=7)
    bno.place(x=150,y=50)

    no1=Label(window1,text=no)
    no1.place(x=220,y=50)

    print1=Button(window1,text="PRINT",bg="purple",fg="white",command=db)
    print1.place(x=160,y=240)

    

bill=Button(window,text="---BILL--- ",bg="yellow",fg="black",width=15,font=("bold",12),command=create_window)
bill.place(x=480,y=520)



#print&db


def db():
    mycursor = mydb.cursor()
    n=name.get()
    no=number.get()
    wow= "INSERT INTO orders(Customer_name,Customer_number,Order_details,Total,Date,Time) VALUES (%s,%s,%s,%s,%s,%s)"
    val = [(n,no,description,total,format_date,abc)]
    mycursor.executemany(wow,val)
    messagebox.showinfo("Thank You","Entry Added Succesfully")
    mydb.commit()
    window1.destroy()
    name.delete(0,"end")
    number.delete(0,"end")
    burger.delete(0,"end")
    burger.insert(0,0)
    fries.delete(0,"end")
    fries.insert(0,0)
    pizza.delete(0,"end")
    pizza.insert(0,0)
    sandwitch.delete(0,"end")
    sandwitch.insert(0,0)
    sub.delete(0,"end")
    sub.insert(0,0)
    water.delete(0,"end")
    water.insert(0,0)
    softdrink.delete(0,"end")
    softdrink.insert(0,0)
    totalrs.delete(0,"end")
    totalrs.insert(0,0)



#history

def his():
    window2=Toplevel(window)
    window2.geometry("850x600")
    window2.title("Order History")
    window2.config(bg="lavender")

    orderhistory=Text(window2)
    orderhistory.place(x=0,y=20,width=850,height=600)
    sum1=Entry(window2,width=65)
    sum1.place(x=0,y=0)
    
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM orders")
    x = from_db_cursor(mycursor)
    orderhistory.insert(INSERT,(x))
    mycursor.execute("SELECT SUM(Total) FROM orders")
    y= from_db_cursor(mycursor)
    sum1.insert(INSERT,(y))

def menu():
    window3=Toplevel(window)
    window3.geometry("400x300")
    window3.title("Menu")
    window3.config(bg="lavender")
    l1=Label(window3,text="ITEMS",bg="purple",fg="white",width=20)
    l1.place(x=20,y=30)
    l2=Label(window3,text="COST",bg="purple",fg="white",width=20)
    l2.place(x=200,y=30)

    l3=Label(window3,text="Burger",bg="yellow",fg="black",width=20)
    l3.place(x=20,y=80)
    c1=Label(window3,text="Rs-99",bg="red",fg="white",width=10)
    c1.place(x=240,y=80)
    
    l4=Label(window3,text="Fries",bg="yellow",fg="black",width=20)
    l4.place(x=20,y=110)
    c2=Label(window3,text="Rs-55",bg="red",fg="white",width=10)
    c2.place(x=240,y=110)

    l5=Label(window3,text="Pizza",bg="yellow",fg="black",width=20)
    l5.place(x=20,y=140)
    c3=Label(window3,text="Rs-149",bg="red",fg="white",width=10)
    c3.place(x=240,y=140)

    l6=Label(window3,text="Sandwitch",bg="yellow",fg="black",width=20)
    l6.place(x=20,y=170)
    c4=Label(window3,text="Rs-80",bg="red",fg="white",width=10)
    c4.place(x=240,y=170)
    
    l7=Label(window3,text="Subway",bg="yellow",fg="black",width=20)
    l7.place(x=20,y=200)
    c1=Label(window3,text="Rs-185",bg="red",fg="white",width=10)
    c1.place(x=240,y=200)

    l8=Label(window3,text="Water Bottle",bg="yellow",fg="black",width=20)
    l8.place(x=20,y=230)
    c1=Label(window3,text="Rs-20",bg="red",fg="white",width=10)
    c1.place(x=240,y=230)

    l9=Label(window3,text="Soft Drinks",bg="yellow",fg="black",width=20)
    l9.place(x=20,y=260)
    c1=Label(window3,text="Rs-40",bg="red",fg="white",width=10)
    c1.place(x=240,y=260)
    
    


menu=Button(window,text="View Menu",bg="yellow",fg="black",width=15,font=("bold",12),command=menu)
menu.place(x=1000,y=100)



history=Button(window,text="View Orders History",bg="yellow",fg="black",width=15,font=("bold",12),command=his)
history.place(x=1150,y=100)

    











                                    ####calculator####
expression = "" 


def press(num): 
	
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 

 
def equalpress(): 
 
	try: 
		global expression 
		total = str(eval(expression))
		equation.set(total) 
		expression = "" 
	except: 

		equation.set(" error ") 
		expression = "" 


def clear(): 
	global expression 
	expression = "" 
	equation.set("") 



equation = StringVar() 
expression_field = Entry(window,width=30,textvariable=equation,font=("bold",12))
expression_field.place(x=1000,y=250)

button1 = Button(window, text=' 1 ', fg='black', bg='lightgrey', command=lambda: press(1), height=2, width=7) 
button1.place(x=1000,y=300) 
  
button2 = Button(window, text=' 2 ', fg='black', bg='lightgrey', command=lambda: press(2), height=2, width=7) 
button2.place(x=1070,y=300) 
  
button3 = Button(window, text=' 3 ', fg='black', bg='lightgrey',command=lambda: press(3), height=2, width=7) 
button3.place(x=1140,y=300)
  
button4 = Button(window, text=' 4 ', fg='black', bg='lightgrey',command=lambda: press(4), height=2, width=7) 
button4.place(x=1000,y=350) 
  
button5 = Button(window, text=' 5 ', fg='black', bg='lightgrey',command=lambda: press(5), height=2, width=7) 
button5.place(x=1070,y=350)
  
button6 = Button(window, text=' 6 ', fg='black', bg='lightgrey', command=lambda: press(6), height=2, width=7)
button6.place(x=1140,y=350)
  
button7 = Button(window, text=' 7 ', fg='black', bg='lightgrey', command=lambda: press(7), height=2, width=7)
button7.place(x=1000,y=400)
  
button8 = Button(window, text=' 8 ', fg='black', bg='lightgrey', command=lambda: press(8), height=2, width=7) 
button8.place(x=1070,y=400)
  
button9 = Button(window, text=' 9 ', fg='black', bg='lightgrey', command=lambda: press(9), height=2, width=7) 
button9.place(x=1140,y=400)
  
button0 = Button(window, text=' 0 ', fg='black', bg='lightgrey', command=lambda: press(0), height=2, width=7) 
button0.place(x=1000,y=450) 
  
plus = Button(window, text=' + ', fg='black', bg='lightgrey',font=("bold",9),command=lambda: press("+"), height=2, width=7)
plus.place(x=1210,y=300)
  
minus = Button(window, text=' - ', fg='black', bg='lightgrey', font=("bold",9),command=lambda: press("-"), height=2, width=7) 
minus.place(x=1210,y=350)
  
multiply = Button(window, text=' * ', fg='black', bg='lightgrey',font=("bold",9),command=lambda: press("*"), height=2, width=7) 
multiply.place(x=1210,y=400)
  
divide = Button(window, text=' / ', fg='black', bg='lightgrey',font=("bold",9), command=lambda: press("/"), height=2, width=7) 
divide.place(x=1210,y=450)

clear = Button(window, text='Clear', fg='black', bg='lightgrey',font=("bold",9),command=clear, height=2, width=7) 
clear.place(x=1070,y=450)
  
equal = Button(window, text=' = ', fg='black', bg='lightgrey', font=("bold",9),command=equalpress,height=2, width=7) 
equal.place(x=1140,y=450) 
  

window.mainloop()



