from win10toast import ToastNotifier
import time

toast = ToastNotifier()

while True:
    print("Notification Maker")

    notification_name = input("Enter the notification name: ")
    notification_body = input("Enter the notification body (content): ")
    notification_duration = input("Enter the notification duration: ")
    notification_timer = input("Choose after how many seconds to show the notification: ")

    try:
        time.sleep(int(notification_timer))

        toast.show_toast(
            notification_name,
            notification_body,
            duration = int(notification_duration),
            #icon_path = "icon.ico",
            threaded = True,
        )
        
    except Exception as e:
        print(f"Error: {e}")
        print("Please try again.")
