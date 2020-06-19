# Bouncing stream icons - OBS Studio Overlay

Bouncing stream overlay - an incredibly simple, yet useful, stream overlay for bouncing icons.

Sometimes, you will want to have something bouncing around on your screen while you either record or stream using OBS Studio (or it's family programs.)

Luckily, you don't need OBS plugins or scripts. This simple web application can be added as a browser source and will cause small images to bounce around the bounds of the browser source. These images can be customized easily with scripts and are performance light.

## Features

* **Minimalist, easy-to-use overlay** The overlay should work out of the box with the majority of OBS setups
* **Automatic resolution adjustment** The overlay automatically adjusts to your resolution in order to not stretch the content. However, you have the option to scale up your content if wanted
* **Randomized behavior** Every time the overlay loads, the icon displayed will be different.
* **Very customizable** Scripts can automatically customize for you with
* **Little to no OBS setup** Works with default OBS browser sources out of the box

## Downloading and installation

### Setting up the widget

This widget does not need any installation, but you will need to configure OBS for the best experience.

To get the widget on your computer, either download the source or clone using the following command:

    git clone https://github.com/OverEngineeredCode/Bouncing-Icons

This will get all the files required to run the overlay on your computer, including some nice default icons.

### Setting up OBS

In OBS, you will need to create a browser source. In the create dialog box, you will need to check the option which reads "Local file". In the box labelled "Local file", browse to the location you saved/cloned the code. Then, set the file to **main.html** in the code.

Underneath, set the width and height to the scaled size (output resolution) of your recording or stream. Finally, in the *Custom CSS* box, delete all the contained text: the widget handles this for you.

After you click OK, you may see a bouncing icon. If you do not, right click on the source in the sources view and select **Transform**>**Stretch to screen**

After you did all of this, move the widget to the top of all other elements (if applicable) and you should see an icon bouncing around the viewport. The widget automatically adjusts for your stream's resolution based on the size of the browser source.

## Customizing

> **Important:** In order to run our scripts, you must have *Python 3.6* or later installed on your system. If you do not, please visit <https://python.org> and install the latest version.

I've included scripts which automatically perform actions such as adding icons and disabling them. You can have an icon added but not disabled at the same time.

The defaults are good for programming/coding streams (not much else though).
