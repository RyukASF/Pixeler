import keyboard
import autoit
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from colorama import Fore, Back, Style
import playsound

pIndex = 0
pixels = []
canItRun = False

# Set Button coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
colorCord = 1093, 863
inputCord = 1087, 761
closeCord = 1345, 471

# Set x and y coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
x = [646, 663, 686, 704, 723, 748, 765, 788, 804, 829, 845, 868, 889, 908, 931, 951, 969,
     985, 1012, 1031, 1051, 1074, 1091, 1113, 1134, 1154, 1173, 1193, 1214, 1235, 1255, 1273]
y = [165, 186, 204, 225, 245, 263, 282, 305, 327, 344, 364, 385, 405, 428, 444, 470,
     489, 509, 529, 552, 572, 586, 607, 632, 648, 669, 688, 710, 732, 755, 769, 793]

# This is to make sure that amount of coordinates are correct
print("resolution:", len(x), "x", len(y))

cY, cX = colorCord
iY, iX = inputCord
clY, clX = closeCord


# This Functions makes sure that it can run smooth without any problems based on Your FPS
def calculate_f_sleep_time(fps):
    frame_time = 1 / fps

    # We'll use a slightly longer sleep time to ensure the game registers the input
    f_sleep_time = frame_time * 1.2

    return f_sleep_time


def process_image():
    global pIndex
    global canItRun

    pixels.clear()

    # Create a file dialog
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    img = Image.open(file_path)

    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    img = img.resize((32, 32))

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = img.getpixel((x, y))

            color = "#{:02x}{:02x}{:02x}".format(r, g, b)

            pixels.append(color)
            pIndex = 0
    canItRun = True

    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print(pixels, Style.RESET_ALL)


def select_color():
    global pIndex
    global canItRun

    if pIndex >= 1024:
        canItRun = False
        playsound("audio.ding.mp3")
    else:
        autoit.mouse_move(cY, cX, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_move(cY+1, cX+1, 0)
        time.sleep(0.005)
        autoit.mouse_move(cY-1, cX-1, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_click()

        autoit.mouse_move(iY, iX, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_move(iY+1, iX+1, 0)
        time.sleep(0.005)
        autoit.mouse_move(iY-1, iX-1, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_click()

        keyboard.write(pixels[pIndex])

        pIndex += 1

        autoit.mouse_move(clY, clX, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_move(clY+1, clX+1, 0)
        time.sleep(0.005)
        autoit.mouse_move(clY-1, clX-1, 0)
        time.sleep(f_sleep_time)
        autoit.mouse_click()


def on_press():
    key = 'f'
    if key == 'f':
        autoit.mouse_click()
        for j in range(len(y)):
            for i in range(len(x)):
                if canItRun == True:
                    select_color()
                    # This many inputs is because roblox sucks
                    autoit.mouse_move(x[i], y[j], 0)
                    time.sleep(0.001)
                    autoit.mouse_click()
                    autoit.mouse_move(x[i]+1, y[j]+1, 0)
                    time.sleep(0.001)
                    autoit.mouse_click()
                    autoit.mouse_move(x[i]-1, y[j]-1, 0)
                    time.sleep(0.001)
                    autoit.mouse_click()
                    autoit.mouse_move(x[i], y[j], 0)
                    time.sleep(f_sleep_time)
                    autoit.mouse_click()

                    if keyboard.is_pressed("g"):
                        on_release()
                        break


def on_release():
    global canItRun
    key = 'g'
    if key == 'g':
        canItRun = False


fps = int(input("Enter your Roblox Average FPS: "))
f_sleep_time = calculate_f_sleep_time(fps)

print(f"Optimal delay is: {f_sleep_time:.4f} seconds")


print(Style.RESET_ALL)
print(Back.LIGHTBLACK_EX)
print("Press H To Select Image")
print("Press F To Start Drawing")
print("Press G To Stop Drawing", Style.RESET_ALL)

# Listen for hotkeys
keyboard.add_hotkey('f', on_press)
keyboard.add_hotkey('h', process_image)
keyboard.add_hotkey('g', on_release)
keyboard.wait()
