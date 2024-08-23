# Pixeler Tutorial (Install - Use)

_This is the detailed tutorial, so follow it carefully and if something goes wrong check this tutorial again._

## Installation

First, You need to have [Python](https://www.python.org) Installed, Download it from [Here](https://www.python.org/downloads/) and select `add python to PATH`

Downlaod .Zip file from GitHub, or from [Here](https://github.com/RyukASF/Pixeler/archive/refs/heads/main.zip)
and extract it.

![screenshot1]([https://drive.google.com/file/d/1imKV0_o2TjuvE7XRGOZE3tujLoh9PlnT/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

Or if you already have [Git](https://git-scm.com/downloads) installed, use this command in terminal:

```bash
git clone https://github.com/RyukASF/Pixeler
```

## Setup

Inside the Pixeler Folder, run `pixelCounter.bat`

by using this program we will get the information about coordinates ingame and install necessary libraries_

When you run the program, first it is going to start installing libraries.

after it finishes you will see This:

![screenshot2]([https://drive.google.com/file/d/1miIfknPfNUcbkQb8JmnLaoInAs3Ju7N9/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

Go into Starving Artists game and open Drawing Panel.

By pressing `F` Key, you will add your current mouse position as one of the pixels from drawing panel in Starving Artists.
One by one, You have to point your mouse to pixel on the grid and hit `F`, after you hear a _pop_ sound, move on to the next.

Here is how you should do it:

![screenshot3]([https://drive.google.com/file/d/1ndNBZlQM8PeGP2gQ/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

**First** you go from Left to Right adding all 32 pixels on the list.

**Then** you go from Top to Bottom adding all 32 pixels on the list.

_If you listen carefully, while adding pixels, Horizontal and Vertical pixels have different sound effects_

When you're done you should hear _ding_ sound.

After that, By pressing `T` Key, add Color Selector Button do the list.

![screenshot4]([https://drive.google.com/file/d/1_8d6JEbkGoZF6D5DvpdPwpKd9QDr5Kp/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

By pressing `Y` Key, add Input area to the list.

![screnshot5]([https://drive.google.com/file/d/1bdvjVuV53iSg8pdo4U1zvX4uAkK00yb3/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

By pressing `U` Key, add Close Button to the list.

![screenshot6]([https://drive.google.com/file/d/1H7vRl0cmAp16F8IMKcyxM0e1wwwc1dhl/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

Now when you're done, check the `pixelCounter` program. You should see something like This:

![screenshot7]([https://drive.google.com/file/d/1fIFQWcyjb7OF3Us1962Bj7DKJanAwG2/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

_DO NOT CLOSE THE PROGRAM YET_

Next, inside Pixeler Folder, go in python Folder and open pixeler.py by using Any Text Editor (I recommend using [Visual Stuido Code](https://code.visualstudio.com))

![screenshot8]([https://drive.google.com/file/d/1lrQDf9uNLfG1368AxLtJlHAHrhLSenyP/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

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

inside Pixeler Folder, run pixeler.bat file

![screenshot9]([https://drive.google.com/file/d/1uZdh8OJ_web4fvYJJLn8OULyR8BcIDqI/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

Enter your average Roblox FPS there and hit enter. (this is to make sure that program functions based on your pc's capabilities)

After This pops up you're ready to go

![screenshot10]([https://drive.google.com/file/d/15EBHHcGWlI_FMrrpe-EjACZ4jmcLmbBW/view](https://drive.google.com/file/d/File_ID/view?usp=sharing))

Press `H` to Select Image you want to draw

Press `F` to Start Drawing

Press `G` to Stop the Program

## Enjoy!
