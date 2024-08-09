import time
import pyautogui
import keyboard
import playsound

thing = False

x = []
y = []

print("Press F to add Mouse Coordinates to the List")
print("Cooldown for each press is 0.1s \n")


def printValues():
    print(f"x = {x} y = {y} \n")
    print("Amount of X values are:", len(x))
    print("Amount of Y values are:", len(y))
    time.sleep(0.3)


def printPercentage():
    percentage = len(x + y) / 64
    print(f"Progess: {round(percentage * 100)}%", end='\r')


while True:

    if keyboard.is_pressed("f"):
        if (thing == False):
            cordX, condY = pyautogui.position()
            if len(x) != 32:
                x.append(cordX)
                playsound.playsound("audio/xpop.wav")
                printPercentage()
                Thing = True
                time.sleep(0.1)
                thing = False

            elif len(x) == 32 and len(y) != 32:
                y.append(condY)
                playsound.playsound("audio/ypop.wav")
                printPercentage()
                Thing = True
                time.sleep(0.1)
                thing = False
                if len(x) == 32 and len(y) == 32:
                    playsound.playsound("audio/ding.mp3")
                    printValues()
                    exit()
