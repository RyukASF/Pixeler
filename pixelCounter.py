import time
import pyautogui
import keyboard
import playsound
import math

thing = False

x = []
y = []

print("Press F to add Mouse Coordinates to the List")
print("Cooldown for each press is 0.1s \n")


def printValues():
    print(f"x = {x} y = {y}")
    print("Amount of X values are:", len(x))
    print("Amount of Y values are:", len(y))
    time.sleep(0.3)


while True:

    if keyboard.is_pressed("f"):
        if (thing == False):
            cordX, condY = pyautogui.position()
            x.append(cordX)
            y.append(condY)
            percentage = len(x) / 32
            print(f"Progess: {round(percentage * 100)}%", end='\r')

            if len(x) == 32 and len(y) == 32:
                playsound.playsound("audio/ding.mp3")
                printValues()
                exit()

            playsound.playsound("audio/pop.wav")
            Thing = True
            time.sleep(0.1)
            thing = False
