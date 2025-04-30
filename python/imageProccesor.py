# =====================================================================================================
# ========================= Made By RyuKam1 & Ryuk_ASF(They're The Same Person) =======================
# =====================================================================================================
# ========= Please Do Not Change Any Parts Of The Code, If You Don't Know What You're Doing ===========
# =====================================================================================================


from collections import Counter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, filedialog
from win32 import win32clipboard
import io

pixels = []


def getpixels():
    return pixels


def getDominantColor(image):
    pixels = list(image.getdata())

    mostCommonColor = Counter(pixels).most_common(1)[0][0]
    # print("Dominant Color:", mostCommonColor)
    r, g, b, a = mostCommonColor
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)

    return color


def getInverseDominantColor(image):
    pixels = list(image.getdata())

    mostCommonInverseColor = Counter(pixels).most_common(1)[0][0]
    # print("Inverse Dominant Color:", mostCommonInverseColor)
    r, g, b, a = mostCommonInverseColor

    color = "#{:02x}{:02x}{:02x}".format(255-r, 255-g, 255-b)

    return color


def process_image(preview_frame, cMenu, preview_label):
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

    print(type(img))

    dominantColor = getDominantColor(img)
    invDominantColor = getInverseDominantColor(img)

    print("Dominant Color:", dominantColor)
    print("Inverse Dominant Color:", invDominantColor, "\n")

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = img.getpixel((x, y))

            color = "#{:02x}{:02x}{:02x}".format(r, g, b)

            pixels.append(color)

    preview_frame.config(
        highlightthickness=5, highlightbackground=dominantColor, highlightcolor=dominantColor)

    cMenu.config(activebackground=dominantColor,
                 activeforeground=invDominantColor)

    print(pixels)

    try:
        image = img
        # Resize image for preview
        image = image.resize((400, 400), Image.NEAREST)
        img = ImageTk.PhotoImage(image, Image.NEAREST)

        global pixelImg
        pixelImg = image

        preview_label.config(image=img)
        preview_label.image = img  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading image: {e}")


def save_image():
    path = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes=[("PNG files", "*.png")])
    if path:
        pixelImg.save(path)
        print(f"Saved to {path}")


def copy_image():
    try:
        output = io.BytesIO()
        pixelImg.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]  # BMP header skip
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        print("Copied to clipboard!")
    except Exception as e:
        print(f"Copy failed: {e}")
