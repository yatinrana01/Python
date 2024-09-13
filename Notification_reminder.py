import time
from plyer import notification

if __name__ == "__main__":
    while True: #infinite loop
        notification.notify(
            title = "Title of notification",
            message = "Description of the message",
            timeout=5 #duration of notification
        )
        time.sleep(2) #60 sec *2(120 sec means 2 min)