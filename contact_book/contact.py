from tkinter import *
import csv
from tkinter import messagebox

contactlist=[]

def ReadCSVFile():
	global header
	with open('contacts.csv') as csvfile:
		read1 = csv.reader(csvfile,delimiter=',')
		header = next(read1)
		for row in read1:
			contactlist.append(row)
	set_select()		
	print(contactlist)

def WriteInCSVFile(phonelist):
	with open('contacts.csv','w',newline='') as csvfile1:
		write1 = csv.writer(csvfile1,delimiter=',')
		write1.writerow(header)
		for row in contactlist:
			write1.writerow(row)

def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])

def AddInfo():
	if firstname.get()!="" and lastname.get()!="" and contact.get()!="":
		contactlist.append([firstname.get()+' '+lastname.get(),contact.get()])
		print(contactlist)
		WriteInCSVFile(contactlist)
		set_select()
		EntryReset()
		messagebox.showinfo("Confermation", "Succesfully Added New Contact")
		
	else:
		messagebox.showerror("Error", "Please fill the information")

def UpdateInfo():
	if firstname.get() and lastname.get() and contact.get():
		contactlist[Selected()] = [ firstname.get()+' '+lastname.get(), contact.get()]
		WriteInCSVFile(contactlist)
		messagebox.showinfo("Confirmation", "Succesfully Update Contact")
		EntryReset()
		set_select()

	elif not(firstname.get()) and not(lastname.get()) and not(contact.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
			messagebox.showerror("Error", message)

def Reset():
	firstname1.set('')
	lastname1.set('')
	contact1.set('')


def Delete():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
		if result==True:
			del contactlist[Selected()]
			WriteInCSVFile(contactlist)
			set_select()
	else:
		messagebox.showerror("Error", 'Please select the Contact')

def Loading():
    name, phone = contactlist[Selected()]
    print(name.split(' '))
    firstname1.set(name.split()[0])
    lastname1.set(name.split()[1])
    contact1.set(phone)


def set_select():
    contactlist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in contactlist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")

win = Tk()
win.title("contact book")

Frame1 = LabelFrame(win,text="Enter the Contact Detail")
Frame1.grid(padx=15,pady=15)

Frame2 = Frame(Frame1)
Frame2.grid(row=0,column=0,padx=15,pady=15)
name1 = Label(Frame2,text="Name")
name1.grid(row=0,column=0,padx=5,pady=5)
firstname1 = StringVar()

firstname = Entry(Frame2,width=30, textvariable=firstname1)
firstname.grid(row=0,column=1,padx=5,pady=5)
lastname2= Label(Frame2,text="LastName")
lastname2.grid(row=1,column=0,padx=5,pady=5)
lastname1= StringVar()
lastname = Entry(Frame2,width=30,textvariable=lastname1)
lastname.grid(row=1,column=1,padx=5,pady=5)
contact2= Label(Frame2,text="Contact")
contact2.grid(row=2,column=0,padx=5,pady=5)
contact1 = StringVar()
contact3 = Entry(Frame2,width=30,textvariable=contact1)
contact3.grid(row=2,column=1,padx=5,pady=5)
Frame3 = Frame(win)
Frame3.grid(row=0,column=1,padx=15,pady=15,sticky=E)

button = Button(Frame3,text="Add Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=AddInfo)
button.grid(row=0,column=0,padx=8,pady=8)

button1 = Button(Frame3,text="Update Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=UpdateInfo)
button1.grid(row=1,column=0,padx=8,pady=8)


button2 = Button(Frame3,text="Reset",width=15,bg="#6B69D6",fg="#FFFFFF",command=Reset)
button2.grid(row=2,column=0,padx=8,pady=8)

Display = Frame(win)
Display.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(Display, orient=VERTICAL)
select = Listbox(Display, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#282923",fg="#E7C855",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)

ActionFrame = Frame(win)
ActionFrame.grid(row=1,column=1,padx=15,pady=15,sticky=E)

button3 = Button(ActionFrame,text="Delete",width=15,bg="#D20000",fg="#FFFFFF",command=Delete)
button3.grid(row=0,column=0,padx=5,pady=5,sticky=S)

button4 = Button(ActionFrame,text="Load",width=15,bg="#6B69D6",fg="#FFFFFF",command=Loading)
button4.grid(row=1,column=0,padx=5,pady=5)

ReadCSVFile()

win.mainloop()