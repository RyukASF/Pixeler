# Pixeler Tutorial (Install - Use)

_This is the detailed tutorial, so follow it carefully and if something goes wrong check this tutorial again._

## Installation

First, You need to have [Python](https://www.python.org) Installed, Download it from [Here](https://www.python.org/downloads/) and select `add python to PATH`

Downlaod .Zip file from GitHub, or from [Here](https://github.com/RyukASF/Pixeler/archive/refs/heads/main.zip)
and extract it.

![screenshot1](https://cdn.discordapp.com/attachments/842094820867571762/1272249865900134537/image.png?ex=66ba4a85&is=66b8f905&hm=d3818cea1b55e2e054d9c38c1fd13e49e4510150b9e4373f80ae3e653ff2d9db&)

Or if you already have [Git](https://git-scm.com/downloads) installed, use this command in terminal:

```bash
git clone https://github.com/RyukASF/Pixeler
```

## Setup

Inside the Pixeler Folder, run `pixelCounter.bat`

by using this program we will get the information about coordinates ingame and install necessary libraries_

When you run the program, first it is going to start installing libraries.

after it finishes you will see This:

![screenshot2](https://cdn.discordapp.com/attachments/842094820867571762/1272253443532132482/image.png?ex=66ba4dda&is=66b8fc5a&hm=976b898c5eec25a30eff24c8e8b9aa02232efb998446cbbb3c1e394b993f9226&)

Go into Starving Artists game and open Drawing Panel.

By pressing `F` Key, you will add your current mouse position as one of the pixels from drawing panel in Starving Artists.
One by one, You have to point your mouse to pixel on the grid and hit `F`, after you hear a _pop_ sound, move on to the next.

Here is how you should do it:

![screenshot3](https://cdn.discordapp.com/attachments/842094820867571762/1272257428079120405/RobloxScreenShot20240809_024936282.png?ex=66ba5190&is=66b90010&hm=de752fbddb8c7e62df1e6c2f5bf927aa25399163bef76be7a19ed57366574bb7&)

**First** you go from Left to Right adding all 32 pixels on the list.

**Then** you go from Top to Bottom adding all 32 pixels on the list.

_If you listen carefully, while adding pixels, Horizontal and Vertical pixels have different sound effects_

When you're done you should hear _ding_ sound.

After that, By pressing `T` Key, add Color Selector Button do the list.

![screenshot4](https://cdn.discordapp.com/attachments/842094820867571762/1272259090219012136/RobloxScreeddnShot20240809_024936282.png?ex=66ba531c&is=66b9019c&hm=7be276e0fa4621806b7537a0f48c3df416b8369ce39be8539f88454258c59aa9&)

By pressing `Y` Key, add Input area to the list.

![screnshot5](https://cdn.discordapp.com/attachments/842094820867571762/1272260968889585744/image.png?ex=66ba54dc&is=66b9035c&hm=74cf116a543b5ed88844ebee6b485d3c81da9669b523b716985cd63be9a0dd60&)

By pressing `U` Key, add Close Button to the list.

![screenshot6](https://cdn.discordapp.com/attachments/842094820867571762/1272261503331991623/image.png?ex=66ba555b&is=66b903db&hm=5ceb4699bc500adc9ed9f3ae8ec35dfe440c3ab8347960903ccc8e18e86a48a6&)

Now when you're done, check the `pixelCounter` program. You should see something like This:

![screenshot7](https://cdn.discordapp.com/attachments/842094820867571762/1272263553801523333/image.png?ex=66ba5744&is=66b905c4&hm=a831c417834b72e3bf0b153ef3e02e781ad7eb5d17142490519ebfafa6703858&)

_DO NOT CLOSE THE PROGRAM YET_

Next, inside Pixeler Folder, go in python Folder and open pixeler.py by using Any Text Editor (I recommend using [Visual Stuido Code](https://code.visualstudio.com))

![screenshot8](https://cdn.discordapp.com/attachments/842094820867571762/1272265287630061670/Screenshot_3.png?ex=66ba58e2&is=66b90762&hm=2625949fe2a44646e20bf0629a3bf60f0679e14db4e6364782673c020af837e1&)

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

**Replace the Values in Code with Your Values from pixelCounter Program**

## Use

inside Pixeler Folder, run pixeler.bat file

![screenshot9](https://cdn.discordapp.com/attachments/842094820867571762/1272267262933598268/image.png?ex=66ba5ab9&is=66b90939&hm=6c5d6fedc0311b25be3b3a349f99d9d4403ababc466406efccbb8734dcb36ba0&)

Enter your average Roblox FPS there and hit enter. (this is to make sure that program functions based on your pc's capabilities)

After This pops up you're ready to go

![screenshot10](https://cdn.discordapp.com/attachments/842094820867571762/1272268041350021151/image.png?ex=66ba5b72&is=66b909f2&hm=2d0711a28b79194bcc68db418c1c70f232c5feb9a15e11e5bcb00fa66a7595cd&)

Press `H` to Select Image you want to draw

Press `F` to Start Drawing

Press `G` to Stop the Program

## Enjoy!
