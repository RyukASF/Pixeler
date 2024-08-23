# Pixeler Tutorial (Install - Use)

_This is the detailed tutorial, so follow it carefully and if something goes wrong check this tutorial again._

## Installation

First, You need to have [Python](https://www.python.org) Installed, Download it from [Here](https://www.python.org/downloads/) and select `add python to PATH`

Downlaod .Zip file from GitHub, or from [Here](https://github.com/RyukASF/Pixeler/archive/refs/heads/main.zip)
and extract it.

![image](https://github.com/user-attachments/assets/dfa8a6cc-aacb-4654-bb25-e0814613261d)

Or if you already have [Git](https://git-scm.com/downloads) installed, use this command in terminal:

```bash
git clone https://github.com/RyukASF/Pixeler
```

## Setup

Inside the Pixeler Folder, run `pixelCounter.bat`

by using this program we will get the information about coordinates ingame and install necessary libraries_

When you run the program, first it is going to start installing libraries.

after it finishes you will see This:

![image2](https://github.com/user-attachments/assets/ed3d4082-b066-4a11-8ac2-a41446e1d77e)

Go into Starving Artists game and open Drawing Panel.

By pressing `F` Key, you will add your current mouse position as one of the pixels from drawing panel in Starving Artists.
One by one, You have to point your mouse to pixel on the grid and hit `F`, after you hear a _pop_ sound, move on to the next.

Here is how you should do it:

![RobloxScreenShot20240809_024936282](https://github.com/user-attachments/assets/fa5e4cdf-57aa-4f1d-b2b6-a18777138f51)

**First** you go from Left to Right adding all 32 pixels on the list.

**Then** you go from Top to Bottom adding all 32 pixels on the list.

_If you listen carefully, while adding pixels, Horizontal and Vertical pixels have different sound effects_

When you're done you should hear _ding_ sound.

After that, By pressing `T` Key, add Color Selector Button do the list.

![RobloxScreeddnShot20240809_024936282](https://github.com/user-attachments/assets/04bb4299-355e-4d8b-a969-a38b968626d9)

By pressing `Y` Key, add Input area to the list.

![imag3e](https://github.com/user-attachments/assets/21321ce9-c9a8-400e-814a-4ef97cb85c89)

By pressing `U` Key, add Close Button to the list.

![imag2e](https://github.com/user-attachments/assets/da16f7f1-3e3b-4bb9-8f13-6490fc837bc0)

Now when you're done, check the `pixelCounter` program. You should see something like This:

![imag4e](https://github.com/user-attachments/assets/51a62b1c-bdd0-4d77-bbb8-b99dad6f3087)

_DO NOT CLOSE THE PROGRAM YET_

Next, inside Pixeler Folder, go in python Folder and open `pixeler.py` by using **Any Text Editor** (I recommend using [Visual Stuido Code](https://code.visualstudio.com))

![Screenshot_3](https://github.com/user-attachments/assets/adc8ce53-b3c3-45ac-84ac-3fd6406666d9)

Inside the Code Look for This Code:

```python
# ----------------------------------------------------------------------------------------------------------------------

# Set Button coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
colorCord = 1093, 863  # Colour Select Button
inputCord = 1087, 761  # Input Text Area
closeCord = 1345, 471  # Close Button

# Set x and y coordinates //CHANGE THIS COORDINATES WITH YOUR COORDINATES (By using PixelCounter.py)
x = [646, 663, 686, 704, 723, 748, 765, 788, 804, 829, 845, 868, 889, 908, 931, 951, 969,
     985, 1012, 1031, 1051, 1074, 1091, 1113, 1134, 1154, 1173, 1193, 1214, 1235, 1255, 1273]
y = [165, 186, 204, 225, 245, 263, 282, 305, 327, 344, 364, 385, 405, 428, 444, 470,
     489, 509, 529, 552, 572, 586, 607, 632, 648, 669, 688, 710, 732, 755, 769, 793]

# ----------------------------------------------------------------------------------------------------------------------
```

**Replace the Values in Code with Your Values from pixelCounter Program And Save The Code** 

## Use

inside Pixeler Folder, run `pixeler.bat` file

![ima5ge](https://github.com/user-attachments/assets/f3ad7c57-15e9-4845-a4e0-d7ef9a74e4bc)

Enter your average Roblox FPS there and hit enter. (this is to make sure that program functions based on your pc's capabilities)

After This pops up you're ready to go

![imag11e](https://github.com/user-attachments/assets/f33ed3c7-2ec8-4fe2-bea0-935515b5fe72)

Press `H` to Select Image you want to draw

Press `F` to Start Drawing

Press `G` to Stop the Program

## Enjoy!
