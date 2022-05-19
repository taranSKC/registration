from tkinter import *
import mysql.connector as connector

root = Tk()

root.geometry("644x344")
#Heading
Label(root, text="REGISTRATION FORM", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)



def getvals():
    con = connector.connect(host="localhost",
                            port="3306",
                            user="root",
                            password="1234",
                            database="registration")

    print("created")

    query1 = "insert into data(name,phone,gender,emergency,payment) values('{}','{}','{}','{}','{}');".format(
        namevalue.get(),
        phonevalue.get(),
    gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get())
    cur = con.cursor()
    cur.execute(query1)
    con.commit()
    print("inseerted")

    query2="select * from data;"
    cur=con.cursor()
    cur.execute(query2)
    for row in cur:
        print(row)



#Button & packing it and assigning it a command
Button(text="Submit", command=getvals).grid(row=7, column=3)



root.mainloop()
