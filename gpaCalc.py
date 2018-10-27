

from tkinter import *
from Unzip_File import

'''
What do you need to get a certain grade in a class
'''

root = Tk()
root.wm_title("GPA Calculator")

def unzip_action():
	usr1 = entry_1.get()
	usr2 = entry_2.get()
	usr3 = entry_3.get()

	Unzip = UnzipFile(str(usr1),str(usr2),usr3.encode('ascii'))
	Unzip.unzip()
def clear_action():
    pass

label_1 = Label(root, text='Current GPA') # create a label with name Filename
label_2 = Label(root, text='Desired GPA')
#label_3 = Label(root, text='File Password')

unzipBtn = Button(root, text='Calculate', command=unzip_action) # button click unzips file
clearBtn = Button(root, text='Clear', command=clear_action())

entry_1 = Entry(root)  # entry fields for input
entry_2 = Entry(root)
entry_3 = Entry(root)

label_1.grid(row=0, sticky=E) # placement assignment
label_2.grid(row=1, sticky=E)
#label_3.grid(row=2, sticky=E)

entry_1.grid(row=0, column=1) # placement assignment
entry_2.grid(row=1, column=1)
#entry_3.grid(row=2, column=1)
unzipBtn.grid(row=3, column=2)
clearBtn.grid(row=199, column=0)

#c = Checkbutton(root, text='Keep me logged in') # creates a checkbutton
#c.grid(columnspan=2) # places the checkbutton

root.geometry("450x200")
root.mainloop()


'''
You would need a 'A' in 'x number of 5 unit classes' to be able to achieve that GPA
Change the names of the variables to reflect the action 

'''