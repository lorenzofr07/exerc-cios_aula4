import time
import winsound

cont = 100
while cont >= 0:
    print('cont')
    cont -= 1
    time.sleep(1)
    winsound.Beep(4000, 1500)
print('boommm')
winsound.Beep(1500, 1000)
