from gpiozero import Button, RGBLED
import time, random
#init buttons and RGB object
btnRed = Button(19)
btnBlue = Button(26)
RGB = RGBLED(22,27,17)

#init color tuples
r = (1,0,0)
g = (0,1,0)
b = (0,0,1)

def monButt(secs):
    timeEnd = time.time() + secs
    while time.time() < timeEnd:
        if btnRed.is_pressed:
            return announceWinner(btnRed)
        if btnBlue.is_pressed:
            return announceWinner(btnBlue)
    return False

def announceWinner(btn):
    if RGB.color == g:
        winner = r if btn == btnRed else b
    else:
        winner = b if btn == btnRed else r

    RGB.blink(on_color = winner, n = 2, background = 0)
    #print("Done")

try:
    btnPressed = False
    while 1: #btnPressed == False:
        ledColor = random.choice([r,g,b])
        RGB.color = ledColor
        btnPressed = monButt(.5)
except KeyboardInterrupt:
    RGB.off()
