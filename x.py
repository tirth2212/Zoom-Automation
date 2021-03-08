import time
from datetime import datetime
from data import lst
import webbrowser
Started = False
for i in lst:
    while True:
        if Started is False:
            if datetime.now().hour == int(i[1].split(':')[0]) and \
                 datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                print("Class opened")
                time.sleep(30)
                break
