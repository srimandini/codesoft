from tkinter import *
import csv
from tkinter import messagebox

contactlist = []
def ReadCSVFile():
	global header
	with open('contacts.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			contactlist.append(row)
	set()		
	print(contactlist)

def WriteInCSVFile(contactlist):
	with open('contacts.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in contactlist:
			writeobj.writerow(row)

def Add():
	if firstname.get()!="" and lastname.get()!="" and contact3.get()!="":
		contactlist.append([firstname.get()+' '+lastname.get(),contact3.get()])
		print(contactlist)
		WriteInCSVFile(contactlist)
		set()
		Reset()
		messagebox.showinfo("Confermation", "New Contact Added Succesfully")
		
	else:
		messagebox.showerror("Error", "Please fill the information")

def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])

def update():
	if firstname.get() and lastname.get() and contact3.get():
		contactlist[Selected()] = [ firstname.get()+' '+lastname.get(), contact3.get()]
		WriteInCSVFile(contactlist)
		messagebox.showinfo("Confirmation", "Contacts Updated Succesfully")
		Reset()
		set()

	elif not(firstname.get()) and not(lastname.get()) and not(contact3.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
			messagebox.showerror("Error", message1)

def Reset():
	firstname1.set('')
	lastname1.set('')
	contact2.set('')


def Delete():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','Are you sure!')
		if result==True:
			del contactlist[Selected()]
			WriteInCSVFile(contactlist)
			set()
	else:
		messagebox.showerror("Error", 'Please select the Contact')

def Load():
    name, phone = contactlist[Selected()]
    print(name.split(' '))
    firstname1.set(name.split()[0])
    lastname1.set(name.split()[1])
    contact2.set(phone)


def set():
    contactlist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in contactlist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")


win = Tk()
win.title("Contact Book")

Frame1 = LabelFrame(win,text="Enter the Contact Detail")
Frame1.grid(padx=15,pady=15)


Frame2 = Frame(Frame1)
Frame2.grid(row=0,column=0,padx=15,pady=15)

lastname3 = Label(Frame2,text="Name")
lastname3.grid(row=0,column=0,padx=5,pady=5)
firstname1 = StringVar()

firstname = Entry(Frame2,width=30, textvariable=firstname1)
firstname.grid(row=0,column=1,padx=5,pady=5)

lastname2= Label(Frame2,text="LastName")
lastname2.grid(row=1,column=0,padx=5,pady=5)
lastname1= StringVar()
lastname = Entry(Frame2,width=30,textvariable=lastname1)
lastname.grid(row=1,column=1,padx=5,pady=5)

contact1= Label(Frame2,text="Contact")
contact1.grid(row=2,column=0,padx=5,pady=5)
contact2 = StringVar()
contact3 = Entry(Frame2,width=30,textvariable=contact2)
contact3.grid(row=2,column=1,padx=5,pady=5)

Frame3 = Frame(win)
Frame3.grid(row=0,column=1,padx=15,pady=15,sticky=E)

button1 = Button(Frame3,text="Add Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=Add)
button1.grid(row=0,column=0,padx=8,pady=8)

button2 = Button(Frame3,text="Update Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=update)
button2.grid(row=1,column=0,padx=8,pady=8)


button3 = Button(Frame3,text="Reset",width=15,bg="#6B69D6",fg="#FFFFFF",command=Reset)
button3.grid(row=2,column=0,padx=8,pady=8)

Display1 = Frame(win)
Display1.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(Display1, orient=VERTICAL)
select = Listbox(Display1, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#282923",fg="#E7C855",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)



Action1 = Frame(win)
Action1.grid(row=1,column=1,padx=15,pady=15,sticky=E)

button4 = Button(Action1,text="Delete",width=15,bg="#D20000",fg="#FFFFFF",command=Delete)
button4.grid(row=0,column=0,padx=5,pady=5,sticky=S)

button5 = Button(Action1,text="Load",width=15,bg="#6B69D6",fg="#FFFFFF",command=Load)
button5.grid(row=1,column=0,padx=5,pady=5)

ReadCSVFile()
win.mainloop()