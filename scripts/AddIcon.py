import os
import sys

import json

fileName = ""
iconId = ""
altText = ""


# First, we need to change to the main directory
os.chdir(os.path.realpath(os.path.dirname(__file__) + "/.."))

print("Welcome to the Add Icon Assistant!")
print("This tool will allow you to add an icon to the overlay\n\n")

input("Before continuing, please move or copy the desired icon to the icons folder in the overlay directory, and hit enter when done...")

print("\n")
fileName = input(
    "Please enter the filename, including extension, that you just copied:")

if not os.path.isfile(os.path.realpath("./icons/" + fileName)):
    print("E: That doesn't seem to be a valid file. Please make sure the file name is correct")
    quit(-1)

print("\nDetected your file successfully")
iconId = input("Please enter the name for your new icon:")
altText = input(
    "[OPTIONAL] Please enter the text to display in the case of an error (alt text):")

print("\nReady to add icon")
print("Before continuing, please verify the following is correct:\n")

print("Icon file: " + fileName)
print("Icon name: " + iconId)
print("Error (alt) text: " + altText)

print("\n")
confirm = input("Does the above look correct [y/n]?")

if confirm.lower() != "y":
    print("E: User cancelled operation")
    quit(-1)

print("Processing, please wait...")


indexFile = open("main.html", "r+")

currentIndex = indexFile.read()
initialSep = currentIndex.split("<div id=\"icons\">")
iconTags = initialSep[1].split("</div>")
icons = iconTags[0].split("\n")

icons.append("        <img style=\"display: none; width: 100px; height: 100px\" src=\"icons/" + fileName + "\" alt=\"" +
             altText + "\" id=\"" + iconId + "\">")

indexFile.close()

toWrite = """
<!DOCTYPE html>

<head>
    <title>Bouncing Ball - Stream Overlay</title>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <script src="config.js"></script>
    <script src="main.js"></script>

    <link rel="stylesheet" href="styles.css">
</head>

<body onload="runOverlay()">
    <div id="icons">
"""

for i in range(0, len(icons)):
    toWrite += icons[i]
    toWrite += "\n"

toWrite += """
    </div>
    
    <canvas id="drawSurface" class="drawCanvas"></canvas>
</body>
"""


writeIndexFile = open("main.html", "w")
writeIndexFile.write(toWrite)


configFile = open("config.js", "r")
configText = configFile.read()
configText = configText.replace("const config = ", "", 1)

configJSON = json.loads(configText)
configFile.close()

configJSON["icons"].append(iconId)

configFileWrite = open("config.js", "w")
configFileWrite.write("const config = " + json.dumps(configJSON) + ";")

print("Done! Configuration has been written and files have been updated")
print("You may need to refresh to overlay for changes to take effect")
