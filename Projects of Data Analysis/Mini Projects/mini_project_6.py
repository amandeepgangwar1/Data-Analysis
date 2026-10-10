print("__________Water Drinking Reminder__________")

import time
from plyer import notification

def water_remainder():
    while True:
        notification.notify(
            title = "Water Remainder for Amandeep", 
            message = "Time to sip some Water! 💧🥤",
            timeout = 10
        )
        time.sleep(3600)   # Remind every hour
        # time.sleep(3)

water_remainder()