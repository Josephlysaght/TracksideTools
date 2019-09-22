from tkinter import *
from functs import *
import functs

root = Tk()
root.title("Event Folder Tool")
master = Frame(root)
master.grid(column=0,row=0, sticky=(N,W,E,S) )
master.columnconfigure(0, weight = 1)
master.rowconfigure(0, weight = 1)
master.pack(pady = 50, padx = 50)

stat = StringVar(root)


def getvalues():
    try:
        functs.year = yearw.get()
        functs.week = weekw.get()
        functs.eventtype = typew.get()
        functs.loc = locationentry.get()
        return True
    except Exception as ex:
        return False


def createfolders():
    if not getvalues():
        stat.set('Error getting values for files')
    elif not action1():
        stat.set('Error pulling from GIT')
    elif not action2():
        stat.set('Error with new folders, check the event code does exist already')
    elif not action3():
        stat.set('Error Pushing to Git')
    else:
        stat.set('All done, Please close window.')

# Create a Tkinter variable
yearw = StringVar(root)
weekw = StringVar(root)
typew = StringVar(root)
locw = StringVar(root)

# Dictionary with options
years = {'2018', '2019', '2020', '2021', '2022'}
weeks = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
         '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34',
         '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51',
         '52'}
types = {'Race', 'Test', 'Show', 'Demo'}
yearw.set('2019')  # set the default option
weekw.set('01')  # set the default option
typew.set('Test')  # set the default option
locw.set("")
stat.set('Please Enter details')

yearpopupMenu = OptionMenu(master, yearw, *years)
Label(master, text="Year:").grid(row=1, column=1)
yearpopupMenu.grid(row=2, column=1)

weekpopupMenu = OptionMenu(master, weekw, *weeks)
Label(master, text="Week:").grid(row=1, column=2)
weekpopupMenu.grid(row=2, column=2)

typepopupMenu = OptionMenu(master, typew, *types)
Label(master, text="Event Type:").grid(row=1, column=3)
typepopupMenu.grid(row=2, column=3)

locationentry = Entry(master, textvariable=locw)
Label(master, text="Location:").grid(row=1, column=4)
locationentry.grid(row=2, column=4)

spacer2 = Label(master)
spacer2.grid(row=3, column=2)


enter_button = Button(master, text="Enter", command=createfolders)
enter_button.grid(row=4, column=1)

close_button = Button(master, text="Cancel", command=root.destroy)
close_button.grid(row=4, column=2)

spacer1 = Label(master)
spacer1.grid(row=5, column=2)

stt = Label(master, textvariable=stat)
stt.grid(row=6, column=3)

root.mainloop()





