import time
import os

while True:
    time1 = time.strftime('%I:%M:%p')
    print(time1)

    if time1 == '07:30:AM':
        print("me works")
        os.startfile("school.mp3")
        time.sleep(5)
        os.startfile("wakeup.wav")
        time.sleep(10)

    if time1 == '08:00:AM':
        print("me works")
        os.startfile("scool.mp3")
        time.sleep(5)
        os.startfile("engineering.wav")
        time.sleep(10)

    if time1 == '10:00:AM':
        print("me works")
        os.startfile("school.mp3")
        time.sleep(5)
        os.startfile("math.wav")
        time.sleep(10)

    if time1 == '11:00:AM':
        print("me works")
        os.startfile("school.mp3")
        time.sleep(5)
        os.startfile("other.wav")
        time.sleep(10)

    if time1 == '11:30:AM':
        print("me works")
        os.startfile("school.mp3")
        time.sleep(5)
        os.startfile("schoolout.wav")
        time.sleep(10)
