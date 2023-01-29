#A simple registration form using python language
from tkinter import *
root=Tk()
Label(root, text= "User Registration Form",font="arial 17 bold").grid(row=0,column=3)

#this is the function that tells the user what just happened after submiting forms
def getvals():
    print("Your registration has been accepted!!")


#this are the variables 
first_name=Label(root,text="First name:") #this is the variable for First Name 
last_name=Label(root,text="Last name")    #this is the variable for Last Name
gender=Label(root,text="Gender")           #this is the variable for Gender
yourID=Label(root,text="ID number")          #this is the variable for the ID of the person
phone_number=Label(root,text="phone number")  #this is the variable for the Phone Number
payment_mood=Label(root,text="Payment mood")  #this is the variable for Payment Mood

#this is makes it (variables) visible in the grid form and well aligned
first_name.grid(row=1, column=2)
last_name.grid(row=2, column=2)
gender.grid(row=3, column=2)
yourID.grid(row=4, column=2)
phone_number.grid(row=5, column=2)
payment_mood.grid(row=6, column=2)

#datatype for the place Holder
first_namevalue=StringVar
last_namevalue=StringVar
gendervalue=StringVar
yourIDvalue=StringVar
phone_numbervalue=StringVar
payment_moodvalue=StringVar
checkvalue =IntVar

first_nameentry=Entry(root, textvariable=first_namevalue)
last_nameentry=Entry(root, textvariable=last_namevalue)
genderentry=Entry(root, textvariable=gendervalue)
yourIDentry=Entry(root, textvariable=yourIDvalue)
phone_numberentry=Entry(root, textvariable=phone_number)
payment_moodentry=Entry(root, textvariable=payment_moodvalue)

#this will make it visible in the gid container
first_nameentry.grid(row=1, column=3,)
last_nameentry.grid(row=2, column=3,)
genderentry.grid(row=3, column=3,)
yourIDentry.grid(row=4, column=3,)
phone_numberentry.grid(row=5, column=3,)
payment_moodentry.grid(row=6, column=3,)

#creating check button 
checkbtn=Checkbutton(text="Remember me!", variable=checkvalue)
checkbtn.grid(row=7, column=3)

#creating a sumbiting button for the user
Button(text="Sumbit" , command=getvals).grid(row=8, column=3)

root.geometry("500x350")
# You can change the background color if you wish to ... the code is below
#root.config(bg='red')

root.mainloop()