# =====================================================================================================
# ========================= Made By RyuKam1 & Ryuk_ASF(They're The Same Person) =======================
# =====================================================================================================
# ========= Please Do Not Change Any Parts Of The Code, If You Don't Know What You're Doing ===========
# =====================================================================================================

import tkinter as tk
from tkinter import ttk, Menu
import keyboard
import autoit
from configparser import ConfigParser
import os
import sys
from screeninfo import get_monitors
from PIL import Image, ImageTk

from splash import splashDraw
from themes import THEMES

from imageProccesor import process_image, save_image, copy_image
from actions import calculate_f_sleep_time, robloxRunning, startDrawing

dirc = os.path.dirname(os.path.realpath(__file__))
path = '/'.join([dirc, "config/pixelerConfig.ini"])

cFile = ConfigParser()
conFile = cFile.read(path)

programVersion = cFile.get("basicInfo", "version")

pIndex = 0
canItRun = False

doubleDraw = False

startKey = cFile.get("shortcuts", "startDrawing")
imageKey = cFile.get("shortcuts", "imageSelect")
stopKey = cFile.get("shortcuts", "stopDrawing")
addKey = cFile.get("shortcuts", "addPoint")

WDColor = "#000000"


def apply_theme(theme_name, root):
    theme = THEMES[theme_name]
    root.config(bg=theme["bg"])

    cFile.set("visuals", "themecolor", theme_name)

    with open(path, "w") as conf:
        cFile.write(conf)

    # HWND = windll.user32.GetParent(root.winfo_id())
    # windll.dwmapi.DwmSetWindowAttribute(HWND,32,byref(c_int(theme["title_bg"])),sizeof(c_int))

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook",
                    foreground=theme["fg"],
                    background=theme["bg"])
    style.configure("Custom.TButton",
                    background=theme["button_bg"],
                    foreground=theme["button_fg"])
    style.configure("Custom.TLabel",
                    background=theme["bg"],
                    foreground=theme["fg"])

    style.configure("Custom.TFrame", background=theme["bg"])

    # Apply theme to all widgets
    for widget in root.winfo_children():
        # Apply to frames
        if isinstance(widget, tk.Frame):
            try:
                widget.config(bg=theme["bg"])
            except tk.TclError:
                pass

            # Apply to children of frames
            for child in widget.winfo_children():
                apply_theme_to_widget(child, theme)

        # Apply to other widgets
        else:
            apply_theme_to_widget(widget, theme)


def apply_theme_to_widget(widget, theme):
    if isinstance(widget, tk.Button):
        try:
            widget.config(bg=theme["button_bg"], fg=theme["button_fg"])
        except tk.TclError:
            pass
    elif isinstance(widget, tk.Label):
        try:
            widget.config(bg=theme["bg"], fg=theme["fg"])
        except tk.TclError:
            pass

    elif isinstance(widget, ttk.Label):
        try:
            widget.config(style="Custom.TLabel")
        except tk.TclError:
            pass

    elif isinstance(widget, ttk.Button):
        try:
            widget.config(style="Custom.TButton")
        except tk.TclError:
            pass

    elif isinstance(widget, ttk.Combobox):
        try:
            widget.config(foreground="#000000")
        except tk.TclError:
            pass
    elif isinstance(widget, ttk.Frame):
        try:
            # Apply the custom style to ttk.Frame
            widget.config(style="Custom.TFrame")
        except tk.TclError:
            pass
        for child in widget.winfo_children():
            apply_theme_to_widget(child, theme)

    elif isinstance(widget, ttk.Notebook):
        widget.config(style="TNotebook")  # Set style for ttk.Notebook
        for tab in widget.tabs():
            tab_frame = widget.nametowidget(tab)
            apply_theme_to_widget(tab_frame, theme)


def open_settings(root):
    themeColor = cFile.get("visuals", "themeColor")
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("400x300")
    settings_window.resizable(False, False)
    center_window(root, settings_window, 400, 300)

    # Apply theme to the settings window
    apply_theme(cFile.get("visuals", "themeColor"), root)

    theme = THEMES[themeColor]

    # Tabs for settings
    notebook = ttk.Notebook(settings_window)
    notebook.pack(fill="both", expand=True)

    tabs = ["General", "Audio", "Hotkeys", "Theme", "SYS"]
    for tab_name in tabs:
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=tab_name)

        # Apply theme to the frame
        apply_theme_to_widget(
            frame, THEMES[themeColor])

        if tab_name == "Theme":
            hotkeys_label = tk.Label(
                frame, text="Select Theme:", font=("Arial", 12, "bold"))
            hotkeys_label.pack(pady=10)

            theme_var = tk.StringVar(
                value=f"{themeColor}")
            theme_dropdown = ttk.Combobox(
                frame, textvariable=theme_var, values=list(THEMES.keys()))
            theme_dropdown.pack(pady=5)

            apply_button = tk.Button(frame, text="Apply Theme",
                                     command=lambda: apply_theme(theme_var.get(), root))
            apply_button.pack(pady=10)

        if tab_name == "Hotkeys":
            # Add hotkeys display
            hotkeys_label = ttk.Label(
                frame, text="Key Shortcuts:", font=("Arial", 12, "bold"))
            hotkeys_label.pack(pady=10)

            start_key_label = tk.Label(
                frame, text=f"Start Drawing: {startKey.upper()}", bg="white")
            start_key_label.pack(pady=5)

            stop_key_label = tk.Label(
                frame, text=f"Stop Drawing: {stopKey.upper()}", bg="white")
            stop_key_label.pack(pady=5)

            image_key_label = tk.Label(
                frame, text=f"Image Select: {imageKey.upper()}", bg="white")
            image_key_label.pack(pady=5)

            add_key_label = tk.Label(
                frame, text=f"Add Point: {addKey.upper()}", bg="white")
            add_key_label.pack(pady=5)

            info_label = tk.Label(
                frame, text=f"You Can Modify |Pixler.ini| File \n Inside |Config| Folder To Change Shortcut Keys")
            info_label.pack(pady=30)

        if tab_name == "SYS":
            sys_tab = notebook.nametowidget(notebook.tabs()[-1])
            tk.Label(sys_tab, text=f"Version | {programVersion}",
                     bg="white", font=(12)).pack(pady=10)


def is_position_on_any_screen(x, y):
    for monitor in get_monitors():
        if (monitor.x <= x <= monitor.x + monitor.width and
                monitor.y <= y <= monitor.y + monitor.height):
            return True
    return False


def center_window(parent, child, width, height):
    parent.update_idletasks()

    px = parent.winfo_x()
    py = parent.winfo_y()
    pw = parent.winfo_width()
    ph = parent.winfo_height()

    # Center the child relative to the parent
    x = px + (pw // 2) - (width // 2)
    y = py + (ph // 2) - (height // 2)

    child.geometry(f"{width}x{height}+{x}+{y}")


def center_root(win):
    cFile.read(conFile)

    if cFile.has_section("Window"):
        try:
            x = int(cFile.get("Window", "x"))
            y = int(cFile.get("Window", "y"))
            w = int(cFile.get("Window", "width"))
            h = int(cFile.get("Window", "height"))

            if is_position_on_any_screen(x, y):
                win.geometry(f"{w}x{h}+{x}+{y}")
                return True
        except:
            pass
    return False


def selectResolution(event, res):
    cFile.read(path)

    if not cFile.has_section("userinfo"):
        cFile.add_section("userinfo")

    cFile.set("userinfo", "resolution", str(res))

    with open(path, "w") as f:
        cFile.write(f)
    print(f"Resolution is set to: {res}")


def showCMenu(event, cMenu):
    try:
        cMenu.tk_popup(event.x_root, event.y_root)
    finally:
        cMenu.grab_release()


def displayUI():

    root = tk.Tk()
    root.withdraw()

    # root.iconbitmap("img/logo.ico")
    ico = Image.open('/'.join([dirc, 'img/logo.ico']))

    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)

    root.title("Pixeler")
    root.geometry("600x400")
    root.resizable(False, False)

    center_root(root)
    root.deiconify()

    cMenu = Menu(root, tearoff=0, borderwidth=0, relief="flat")
    cMenu.add_command(label="Save Image", command=save_image)
    cMenu.add_separator()
    cMenu.add_command(label="Copy Image", command=copy_image)

    # Left Panel
    left_frame = tk.Frame(root)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Custom.TCombobox",
                    foreground="#000000",
                    background="#ffffff")

    resolution_label = tk.Label(left_frame, text="Resolution")

    resolution_dropdown = ttk.Combobox(
        left_frame, values=["1920 x 1080", "1280 x 1024", "1280 x 720", "800 x 600"], style="Custom.TCombobox")
    res = cFile.get("userinfo", "resolution")
    resolution_dropdown.set(f"{res}")

    resolution_dropdown.bind("<<ComboboxSelected>>",
                             lambda event: selectResolution(event, resolution_dropdown.get()))

    speed = cFile.get("userinfo", "speed")
    entry_var = tk.StringVar(value=f"{speed}")
    fps_label = tk.Label(left_frame, text="Speed")

    fps_entry = tk.Entry(
        left_frame, textvariable=entry_var, foreground="#000000",)

    fps_entry.bind("<Return>", lambda event: selectSpeed(fps_entry.get()))

    # Custom Grid Button
    custom_grid = tk.Button(
        left_frame, text="Custom Grid", command=lambda: customGrid())

    # Image Preview
    preview_frame = tk.Frame(root, relief="solid", bd=0, width=300,
                             height=300, highlightbackground="#ffffff", highlightthickness=1)

    preview_label = tk.Label(
        preview_frame, text="Pixelated Image Preview", anchor="center")

    image_button = tk.Button(left_frame, text="Select Image", command=lambda: process_image(
        preview_frame, cMenu, preview_label))

    # Settings Button
    settings_button = tk.Button(
        left_frame, text="Settings", command=lambda: open_settings(root))

    start_button = tk.Button(left_frame, text=f"Start |{startKey}|",
                             command=lambda: startDrawing(int(speed)))

    # Packing
    left_frame.pack(side="left", padx=10, pady=10, fill="y")
    image_button.pack(pady=5)
    resolution_label.pack()
    resolution_dropdown.pack(pady=5)
    fps_label.pack()
    fps_entry.pack(pady=5)
    custom_grid.pack(pady=5)
    preview_frame.pack(side="left", padx=15, pady=15, fill="both", expand=True)
    preview_label.pack(fill="both", expand=True)
    settings_button.pack(pady=5)
    start_button.pack(pady=50)

    preview_label.bind("<Button-3>", lambda event: showCMenu(event, cMenu))

    root.protocol("WM_DELETE_WINDOW", lambda: (
        save_window_position(root)))

    apply_theme(cFile.get("visuals", "themeColor"), root)

    root.mainloop()


def selectSpeed(speed):
    cFile.read(path)

    if not cFile.has_section("userinfo"):
        cFile.add_section("userinfo")

    cFile.set("userinfo", "speed", str(speed))

    with open(path, "w") as f:
        cFile.write(f)
        calculate_f_sleep_time(int(speed))


def customGrid():
    sPoints = []

    print("Custom Grid Mode")
    c = 0
    while len(sPoints) != 2:
        if keyboard.is_pressed("f"):
            sPoints.append(autoit.mouse_get_pos())
            c += 1
            print(c)

            while keyboard.is_pressed('f'):
                pass
    splashDraw(sPoints[0], sPoints[1])


def save_window_position(win):
    cFile.read(path)

    if not cFile.has_section("Window"):
        cFile.add_section("Window")

    cFile.set("Window", "x", str(win.winfo_x()))
    cFile.set("Window", "y", str(win.winfo_y()))
    cFile.set("Window", "width", str(win.winfo_width()))
    cFile.set("Window", "height", str(win.winfo_height()))

    with open(path, "w") as f:
        cFile.write(f)
        sys.exit()
