import time

import pygame as pygame

pygame.init()
schoolbell = pygame.mixer.Sound("school.mp3")
wakeup = pygame.mixer.Sound("wakeup.wav")
engineering = pygame.mixer.Sound("engineering.wav")
math = pygame.mixer.Sound("math.wav")
other = pygame.mixer.Sound("other.wav")
schoolout = pygame.mixer.Sound("schoolout.wav")

while True:
    time1 = time.strftime('%I:%M:%p')
    print(time1)

    if time1 == '07:30:AM':
        print("me works")
        pygame.mixer.Sound.play(schoolbell)
        time.sleep(5)
        pygame.mixer.Sound.play(wakeup)
        time.sleep(60)

    if time1 == '08:00:AM':
        print("me works")
        pygame.mixer.Sound.play(schoolbell)
        time.sleep(5)
        pygame.mixer.Sound.play(engineering)
        time.sleep(60)

    if time1 == '10:00:AM':
        print("me works")
        pygame.mixer.Sound.play(schoolbell)
        time.sleep(5)
        pygame.mixer.Sound.play(math)
        time.sleep(60)

    if time1 == '11:00:AM':
        print("me works")
        pygame.mixer.Sound.play(schoolbell)
        time.sleep(5)
        pygame.mixer.Sound.play(other)
        time.sleep(60)

    if time1 == '11:30:PM':
        print("me works")
        pygame.mixer.Sound.play(schoolbell)
        time.sleep(5)
        pygame.mixer.Sound.play(schoolout)
        time.sleep(60)

    time.sleep(5)
