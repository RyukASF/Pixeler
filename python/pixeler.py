# =====================================================================================================
# ========================= Made By RyuKam1 & Ryuk_ASF(They're The Same Person) =======================
# =====================================================================================================
# ========= Please Do Not Change Any Parts Of The Code, If You Don't Know What You're Doing ===========
# =====================================================================================================

if __name__ == "__main__":

    import keyboard
    from configparser import ConfigParser
    import os

    from imageProccesor import getpixels, process_image
    from ui import displayUI
    from actions import startDrawing, stopDrawing

    dirc = os.path.dirname(os.path.realpath(__file__))
    path = '/'.join([dirc, "config/pixelerConfig.ini"])

    cFile = ConfigParser()
    conFile = cFile.read(path)

    print("\n================================================================================================================\n")
    print('Theme: ', cFile.get("visuals", "themeColor"))

    drawSpeed = 0

    pIndex = 0
    canItRun = False

    doubleDraw = False

    startKey = cFile.get("shortcuts", "startDrawing")
    imageKey = cFile.get("shortcuts", "imageSelect")
    stopKey = cFile.get("shortcuts", "stopDrawing")
    addKey = cFile.get("shortcuts", "addPoint")

    WDColor = "#000000"

    print(f"\nStart Key = {startKey.upper()} \nStop Key = {stopKey.upper()} \nImage Select = {imageKey.upper()} \nAdd Key = {addKey.upper()} \n")

    # ----------------------------------------------------------------------------------------------------------------------------------

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

    # x = [458, 473, 487, 502, 516, 530, 546, 560, 575, 588, 601, 617, 631, 646, 659, 676, 687, 704, 719, 732, 747, 762, 776, 790, 804, 819, 833, 849, 862, 876, 891, 909]
    # y = [115, 131, 143, 160, 173, 187, 205, 215, 230, 246, 260, 276, 290, 303, 317, 332, 347, 361, 376, 390, 405, 420, 435, 448, 463, 478, 491, 507, 521, 535, 551, 565]

    # ----------------------------------------------------------------------------------------------------------------------------------

    # This is to make sure that amount of coordinates are correct
    print("resolution:", len(x), "x", len(y))

    cY, cX = colorCord
    iY, iX = inputCord
    clY, clX = closeCord

    f_sleep_time = 0

    def handleKeyPress(event):
        # print(f"Key pressed: {event.name}")
        key = ""
        if event.event_type == keyboard.KEY_DOWN:
            # Check for common modifiers
            modifiers = []
            if keyboard.is_pressed('ctrl'):
                modifiers.append('ctrl')
            if keyboard.is_pressed('shift'):
                modifiers.append('shift')
            if keyboard.is_pressed('alt'):
                modifiers.append('alt')

            if modifiers:
                key = f"{'+'.join(modifiers)}+{event.name}"
            else:
                key = f"Single key: {event.name}"

            # print(key)

            if key == startKey:
                startDrawing(drawSpeed)
            elif key == stopKey:
                stopDrawing()
            elif key == imageKey:
                process_image()

    keyboard.hook(handleKeyPress)

    displayUI()

    keyboard.wait()
