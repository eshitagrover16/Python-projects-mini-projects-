from plyer import notification
import time
while True:
    print("Please drink some water")
    notification.notify(title="Please drink some water",message="You need to drink some  water , it is really essential")
    time.sleep(3600)

