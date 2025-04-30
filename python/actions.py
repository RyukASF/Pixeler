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

# Set Button coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
colorCord = 1093, 863  # Colour Select Button
# colorCord = 777, 611  # Colour Select Button
inputCord = 1087, 761  # Input Text Area
# inputCord = 773, 542  # Input Text Area
closeCord = 1345, 471  # Close Button
# closeCord = 957, 333  # Close Button

# Set x and y coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
x = [646, 663, 686, 704, 723, 748, 765, 788, 804, 829, 845, 868, 889, 908, 931, 951, 969,
     985, 1012, 1031, 1051, 1074, 1091, 1113, 1134, 1154, 1173, 1193, 1214, 1235, 1255, 1273]
y = [165, 186, 204, 225, 245, 263, 282, 305, 327, 344, 364, 385, 405, 428, 444, 470,
     489, 509, 529, 552, 572, 586, 607, 632, 648, 669, 688, 710, 732, 755, 769, 793]

cY, cX = colorCord
iY, iX = inputCord
clY, clX = closeCord

f_sleep_time = 0

pixels = []


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


def goTo(x, y, keyPerm, ConstandPress):  # TODO Rewrite Input System With Win32 API
    x+5
    y+5
    d = 0
    # s = 0

    if keyPerm == True:

        for i in range(6):
            # time.sleep(f_sleep_time)
            keyboard.press("a")

            autoit.mouse_move(x-i, y-i, d)

            if ConstandPress == True:
                # time.sleep(f_sleep_time)
                autoit.mouse_click()
                if i >= 3:
                    break
            if i == 5:
                time.sleep(f_sleep_time)
                keyboard.press("d")
                autoit.mouse_click()
                keyboard.release("d")
            keyboard.release("a")

    else:
        for i in range(6):
            autoit.mouse_move(x-i, y-i, d)

            if ConstandPress == True:
                # time.sleep(f_sleep_time)
                autoit.mouse_click()
                if i >= 3:
                    break
            if i == 5:
                time.sleep(f_sleep_time)
                autoit.mouse_click()

    # time.sleep(f_sleep_time)


def select_color():  # TODO If Previous Color And New One Are The Same, Make A Bypass Feature For More Speed
    global pIndex
    global canItRun

    if pIndex >= 1024:
        canItRun = False
        playsound("audio.ding.mp3")
    else:
        goTo(cY, cX, True, False)

        goTo(iY, iX, True, False)

        keyboard.write(pixels[pIndex])

        pIndex += 1

        goTo(clY, clX, False, False)
        # time.sleep(f_sleep_time)
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
                global pixels
                pixels = getpixels()
                for j in range(len(y)):
                    for i in range(len(x)):
                        start = time.time()
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
                        end = time.time()
                        print(f"Pixel Drawn in {end - start} Second")
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
