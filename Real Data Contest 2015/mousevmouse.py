# Kyle Wilson
# Disambiguation: Mouse vs Mouse
#
# Use NLP to determine whether a sentence is referring to a computer mouse or a biological mouse.

import re
import sys

computerMouseWords = ["click", "computer", "device", "input", "manipulate", "finger", "keyboard", "electronic", "hold", "left", "button", "scroll", "usb", "dongle", "drive", "hardware", "mousepad", "pc", "screen", "trackball", "port", "hand", "wrist", "wire", "screen", "display", "signal", "software", "grip", "program", "programmer", "development"]

biologicalMouseWords = ["tail", "genome", "species", "nose", "whisker", "life", "experiment", "rat", "cat", "mickey", "cheese", "lab", "quiet", "rodent", "mousetrap", "trap", "vermin", "poison", "environment", "result", "squeak", "hole", "teeth", "squeal", "kill", "exterminate", "exterminator", "nutcracker", "king", "paw", "feet", "eye", "scurry", "born", "birth"]

def whichMouse(x):
    wordList = re.sub("[^\w]", " ", x).split()
    lowerWordList = [word.lower() for word in wordList]
    score = 0
    for word in computerMouseWords:
        if (word or word + "s") in lowerWordList:
            score = score + 1
    for word in biologicalMouseWords:
        if (word or word + "s") in lowerWordList:
            score = score - 1
    return ("animal" if score <= 0 else "computer-mouse")

for line in sys.stdin.readlines()[1:]:
    n = line.split("\n")[0]
    print(whichMouse(n))
