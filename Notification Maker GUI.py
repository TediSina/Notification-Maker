from win10toast import ToastNotifier
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
import threading

submittedName = ""
submittedBody = ""

def submitName():
    try:
        submittedName = nameEntryVar.get()
        print(f"Submitted name: {submittedName}")

    except Exception as e:
        print(f"Error: {e}")
        nameOutput.config(text="An error occurred while submitting the notification name. Please try again.", fg="red")
    
    else:
        nameOutput.config(text="Notification name was submitted successfully.", fg="green")

def submitBody():
    try:
        submittedBody = bodyEntryVar.get()
        print(f"Submitted body (content): {submittedBody}")

    except Exception as e:
        print(f"Error: {e}")
        bodyOutput.config(text="An error occurred while submitting the notification body (content). Please try again.", fg="red")
    
    else:
        bodyOutput.config(text="Notification body (content) was submitted successfully.", fg="green")

def createNotification():
    try:
        toast.show_toast(
            nameEntryVar.get(),
            bodyEntryVar.get(),
            duration = 5,
            threaded = True,
        )

    except Exception as e:
        print(f"Error: {e}")
        notificationCreationOutput.config(text="An error occurred while creating the notification. Please try again.", fg="red")
    
    else:
        notificationCreationOutput.config(text="Notification created successfully.", fg="green")

toast = ToastNotifier()

root = Tk()
root.title("Notification Maker")
root.geometry("500x500")
root.columnconfigure(0, weight=1)

notificationMakerLabel = Label(root, text="Notification Maker", font=("Arial", 30))
notificationMakerLabel.grid(row=0)

enterNameLabel = Label(root, text="Enter the notification name:", font=("Arial", 15))
enterNameLabel.grid(row=1)

nameEntryVar = StringVar()
nameEntry = Entry(root, width=75, textvariable=nameEntryVar)
nameEntry.grid(row=2, pady=5)

nameSubmitButton = Button(root, text="Submit", width=10, bg="red", fg="white", command = lambda : threading.Thread(target=submitName).start())
nameSubmitButton.grid(row=3, pady=5)

nameOutput = Label(root, text="", fg="red", font=("Arial", 10))
nameOutput.grid(row=4, pady=5)

enterBodyLabel = Label(root, text="Enter the notification body (content):", font=("Arial", 15))
enterBodyLabel.grid(row=5, pady=5)

bodyEntryVar = StringVar()
bodyEntry = Entry(root, width=75, textvariable=bodyEntryVar)
bodyEntry.grid(row=6, pady=5)

bodySubmitButton = Button(root, text="Submit", width=10, bg="red", fg="white", command = lambda : threading.Thread(target=submitBody).start())
bodySubmitButton.grid(row=7, pady=5)

bodyOutput = Label(root, text="", fg="red", font=("Arial", 10))
bodyOutput.grid(row=8, pady=5)

notificationCreationButton = Button(root, text="Create the notification", width=18, bg="red", fg="white", command = lambda : threading.Thread(target=createNotification).start())
notificationCreationButton.grid(row=9, pady=5)

notificationCreationOutput = Label(root, text="", fg="red", font=("Arial", 10))
notificationCreationOutput.grid(row=10, pady=5)

root.mainloop()
