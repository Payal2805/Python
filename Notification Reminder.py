import time            
from plyer import notification    #plyer module install in command prompt
if __name__ =='__main__':         #only this program output display
    while True:
        notification.notify(
            title="All Day Reminder",
            message ="Todya I have to created"
                     "Python Project and you have"
                     " not completed it till now",
            timeout = 5          #timeout use to read message time limit (seconds)
        )
        time.sleep(15)          #remind to time second (1 hour write is 60*60(min* sec))
