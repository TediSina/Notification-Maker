from win10toast import ToastNotifier
from tkinter import *
import threading
import time

submittedName = "Hello World!"
submittedBody = "This is a notification."
submittedDuration = 5
submittedTimer = 0

def submitName():
    try:
        global submittedName
        submittedName = nameEntryVar.get()
        print(f"Submitted name: {submittedName}")

    except Exception as e:
        print(f"Error: {e}")
        nameOutput.config(text="An error occurred while submitting the notification name. Please try again.", fg="red")
    
    else:
        nameOutput.config(text="Notification name was submitted successfully.", fg="green")

def submitBody():
    try:
        global submittedBody
        submittedBody = bodyEntryVar.get()
        print(f"Submitted body (content): {submittedBody}")

    except Exception as e:
        print(f"Error: {e}")
        bodyOutput.config(text="An error occurred while submitting the notification body (content). Please try again.", fg="red")
    
    else:
        bodyOutput.config(text="Notification body (content) was submitted successfully.", fg="green")

def submitDuration():
    try:
        global submittedDuration
        submittedDuration = float(durationEntryVar.get())
        print(f"Submitted duration: {submittedDuration}")

    except Exception as e:
        print(f"Error: {e}")
        durationOutput.config(text="An error occurred while submitting the notification duration. Please make sure that a number is provided and try again.", fg="red")
    
    else:
        durationOutput.config(text="Notification duration was submitted successfully.", fg="green")

def submitTimer():
    try:
        global submittedTimer
        submittedTimer = float(timerEntryVar.get())
        print(f"Submitted timer: {submittedTimer}")
    
    except Exception as e:
        print(f"Error: {e}")
        timerOutput.config(text="An error occurred while submitting the notification timer. Please make sure that a number is provided and try again.", fg="red")

    else:
        timerOutput.config(text="Notification timer was submitted successfully.", fg="green")

def createNotification():
    try:
        time.sleep(submittedTimer)

        toast.show_toast(
            submittedName,
            submittedBody,
            duration = submittedDuration,
            threaded = True,
        )

        print("---------------------------------------")
        print(f"Submitted name: {submittedName}")
        print(f"Submitted body (content): {submittedBody}")
        print(f"Submitted duration: {submittedDuration}")
        print(f"Submitted timer: {submittedTimer}")

    except Exception as e:
        print(f"Error: {e}")
        notificationCreationOutput.config(text="An error occurred while creating the notification. Please try again.", fg="red")
    
    else:
        notificationCreationOutput.config(text="Notification created successfully.", fg="green")

toast = ToastNotifier()

root = Tk()
root.title("Notification Maker")
root.geometry("800x700")
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

enterDurationLabel = Label(root, text="Enter the notification duration (after how many seconds it will self-destruct):", font=("Arial", 15))
enterDurationLabel.grid(row=9, pady=5)

durationEntryVar = StringVar()
durationEntry = Entry(root, width=75, textvariable=durationEntryVar)
durationEntry.grid(row=10, pady=5)

durationSubmitButton = Button(root, text="Submit", width=10, bg="red", fg="white", command = lambda : threading.Thread(target=submitDuration).start())
durationSubmitButton.grid(row=11, pady=5)

durationOutput = Label(root, text="", fg="red", font=("Arial", 10))
durationOutput.grid(row=12, pady=5)

enterTimerLabel = Label(root, text="Enter the notification timer (after how many seconds it will execute):", font=("Arial", 15))
enterTimerLabel.grid(row=13, pady=5)

timerEntryVar = StringVar()
timerEntry = Entry(root, width=75, textvariable=timerEntryVar)
timerEntry.grid(row=14, pady=5)

timerSubmitButton = Button(root, text="Submit", width=10, bg="red", fg="white", command = lambda : threading.Thread(target=submitTimer).start())
timerSubmitButton.grid(row=15, pady=5)

timerOutput = Label(root, text="", fg="red", font=("Arial", 10))
timerOutput.grid(row=16, pady=5)

notificationCreationButton = Button(root, text="Create the notification", width=18, bg="red", fg="white", command = lambda : threading.Thread(target=createNotification).start())
notificationCreationButton.grid(row=17, pady=5)

notificationCreationOutput = Label(root, text="", fg="red", font=("Arial", 10))
notificationCreationOutput.grid(row=18, pady=5)

root.mainloop()
