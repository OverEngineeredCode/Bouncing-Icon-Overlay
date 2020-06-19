import json
import os

# First, we need to change to the main directory
os.chdir(os.path.realpath(os.path.dirname(__file__) + "/.."))

print("Welcome to the Change Speed Assistant!")
print("This tool will allow you to change the movement speed of the overlay\n\n")

newSpd = input("Enter the new speed:")

configFile = open("config.js", "r")
configText = configFile.read()
configText = configText.replace("const config = ", "", 1)
configText = configText.replace(";", "", 1)

configJSON = json.loads(configText)
configFile.close()

configJSON["speed"] = int(newSpd)

configFileWrite = open("config.js", "w")
configFileWrite.write("const config = " + json.dumps(configJSON) + ";")

print("Done! Configuration has been written")
print("You may need to refresh to overlay for changes to take effect")
