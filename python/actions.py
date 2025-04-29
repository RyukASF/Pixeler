# =====================================================================================================
# ========================= Made By RyuKam1 & Ryuk_ASF(They're The Same Person) =======================
# =====================================================================================================
# ========= Please Do Not Change Any Parts Of The Code, If You Don't Know What You're Doing ===========
# =====================================================================================================


from tkinter import messagebox
import autoit
import keyboard
import time
import playsound

from imageProccesor import getpixels

x = []
y = []

cY = 0
cX = 0
clY = 0
clX = 0


def calculate_f_sleep_time(drawSpeed):
    global f_sleep_time
    try:
        print(f"Speed is set to: {drawSpeed}")
        frame_time = 1 / drawSpeed
        f_sleep_time = frame_time * 1.2
        print(f"Claculated Delay is {f_sleep_time}")
        return f_sleep_time
    except ValueError:
        print("Invalid FPS value. Please enter an integer.")
        return None


def goTo(x, y, d, f):
    x+5
    y+5
    d = 0
    s = 0

    for i in range(5):
        autoit.mouse_move(x-i, y-i, d)
        time.sleep(f_sleep_time)
        if f == True:
            autoit.mouse_click()
        elif i == 3:
            autoit.mouse_click()


def select_color():
    global pIndex
    global canItRun

    if pIndex >= 1024:
        canItRun = False
        playsound("audio.ding.mp3")
    else:
        goTo(cY, cX, 0, False)

        keyboard.write(getpixels(pIndex))

        pIndex += 1

        goTo(clY, clX, 0, False)
        time.sleep(f_sleep_time)
    # print("color select?")


def robloxRunning():
    win = "Roblox"

    if autoit.win_exists(win):
        autoit.win_activate(win)
        return True
    else:
        return False


def startDrawing(drawSpeed):
    calculate_f_sleep_time(drawSpeed)
    global canItRun
    global pIndex

    canItRun = True
    pIndex = 0

    if robloxRunning():

        if f_sleep_time != 0:

            # print("ies")
            print("Start Drawing Initialized")
            try:
                for j in range(len(y)):
                    for i in range(len(x)):
                        if canItRun:
                            # Select color
                            select_color()

                            # Perform mouse clicks with error handling
                            try:
                                # Move to position and click multiple times for reliability
                                goTo(x[i], y[j], 0, True)
                            except Exception as e:
                                print(f"Error during mouse operation: {e}")
                                continue

                            # Emergency stop
                            if keyboard.is_pressed("p"):
                                stopDrawing()
                                break

                        print(f"Processed coordinate: ({x[i]}, {y[j]})")

                print("Drawing completed successfully")
            except Exception as e:
                print(f"Error in StartDrawing: {e}")
            finally:
                canItRun = False

        else:
            canItRun = False
            print("Speed Value Is Empty, Enter Speed :(")
            messagebox.showwarning(
                "Warning", "Speed Value Is Empty, \n Enter Speed ")

    else:
        # print("no")
        canItRun = False
        messagebox.showwarning("Warning", "Roblox Game Isn't Open")
        print("Roblox Wasn't Open :/")


def stopDrawing():
    global canItRun
    if canItRun == True:
        canItRun = False

        print("Stopped Drawing")
