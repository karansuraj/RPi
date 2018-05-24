from gpiozero import Button, RGBLED
import time
btnRed = Button(19)
btnBlue = Button(26)
#btnRed.is_pressed
RGB = RGBLED(22,27,17)
i = .01
j = 0.1
try:
    while(1):
        '''if btnRed.is_pressed and i!=0 :
        i = 0
        RGB.color = (1,0,0)
        time.sleep(j)'''
        '''time.sleep(i)
        RGB.color = (0,1,0)
        time.sleep(i)
        RGB.color = (0,0,1)
        time.sleep(i)'''
        '''elif btnRed.is_pressed and i==0:
        RGB.off()
        i = 1
        time.sleep(j)'''
        RGB.color = (1,0,0)
        #time.sleep(j)
        time.sleep(i)
        RGB.color = (0,1,0)
        time.sleep(i)
        RGB.color = (0,0,1)
        time.sleep(i)
except KeyboardInterrupt:
    RGB.off()
