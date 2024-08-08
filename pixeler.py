import keyboard
import autoit
import time
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from colorama import Fore, Back, Style

pIndex = 0
pixels = []
canItRun = False

# Set x and y coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
x = [646, 663, 686, 704, 723, 748, 765, 788, 804, 829, 845, 868, 889, 908, 931, 951, 969,
     985, 1012, 1031, 1051, 1074, 1091, 1113, 1134, 1154, 1173, 1193, 1214, 1235, 1255, 1273]
y = [165, 186, 204, 225, 245, 263, 282, 305, 327, 344, 364, 385, 405, 428, 444, 470,
     489, 509, 529, 552, 572, 586, 607, 632, 648, 669, 688, 710, 732, 755, 769, 793]

print("resolution:", len(x), "x", len(y))


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
    else:
        autoit.mouse_move(1093, 863)
        autoit.mouse_click()
        time.sleep(0.2)

        autoit.mouse_move(1087, 761)
        autoit.mouse_click()

        keyboard.write(pixels[pIndex])

        pIndex += 1

        autoit.mouse_move(1345, 471)
        autoit.mouse_click()
        time.sleep(0.1)


def on_press():
    key = 'f'
    if key == 'f':
        for i in range(len(x)):
            if canItRun == True:
                select_color()
                autoit.mouse_move(x[i], y[0])
                autoit.mouse_click()
                time.sleep(0.1)

                if keyboard.is_pressed("g"):
                    on_release()
                    break

        for j in range(len(y) - 1):
            for i in range(len(x)):
                if canItRun == True:
                    keyboard.add_hotkey('g', on_release)
                    select_color()
                    autoit.mouse_move(x[i], y[j + 1])
                    autoit.mouse_click()
                    time.sleep(0.1)

                    if keyboard.is_pressed("g"):
                        on_release()
                        break


def on_release():
    global canItRun
    key = 'g'
    if key == 'g':
        canItRun = False


print(Style.RESET_ALL)
print(Back.LIGHTBLACK_EX)
print("Press H To Select Image")
print("Press F To Start Drawing")
print("Press G To Stop Drawing", Style.RESET_ALL)

# Listen for hotkeys
keyboard.add_hotkey('f', on_press)
keyboard.add_hotkey('h', process_image)
keyboard.wait()
