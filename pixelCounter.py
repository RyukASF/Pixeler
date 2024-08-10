import time
import pyautogui
import keyboard
import playsound

thing = False

x = []
y = []

print("\nPress F to add Mouse Coordinates to the List")
print("Cooldown for each press is 0.1s \n")
print("Press |T| to to add Color Button Coordinates to the List")
print("Press |Y| to add Input area Coordinates to the List")
print("Press |U| to add Close Button Coordinates to the List \n")


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
            cordX, cordY = pyautogui.position()
            if len(x) != 32:
                x.append(cordX)
                playsound.playsound("audio/xpop.wav")
                printPercentage()
                Thing = True
                time.sleep(0.1)
                thing = False

            elif len(x) == 32 and len(y) != 32:
                y.append(cordY)
                playsound.playsound("audio/ypop.wav")
                printPercentage()
                if len(x) == 32 and len(y) == 32:
                    playsound.playsound("audio/ding.mp3")
                    printValues()
                    exit()
                Thing = True
                time.sleep(0.1)
                thing = False

    elif keyboard.is_pressed("t"):
        if (thing == False):
            cordX, cordY = pyautogui.position()
            colorButton = cordX, cordY
            print("Colour Select Button: ", colorButton)
            playsound.playsound("audio/ypop.wav")

    elif keyboard.is_pressed("y"):
        if (thing == False):
            cordX, cordY = pyautogui.position()
            inputArea = cordX, cordY
            print("Input Text Area: ", inputArea)
            playsound.playsound("audio/ypop.wav")

    elif keyboard.is_pressed("u"):
        if (thing == False):
            cordX, cordY = pyautogui.position()
            closeButton = cordX, cordY
            print("Close Button: ", closeButton)
            playsound.playsound("audio/ypop.wav")
