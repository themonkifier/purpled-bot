from pyautogui import *
from PIL import Image
#import numpy as np
from time import sleep
#import random
#import keyboard
#import math

# center of boat is at 9*height/10
BACKGROUND_COLOR = (149, 191, 219)
LANE_COLOR = (163, 200, 224)
DEAD_COLOR = (30, 38, 44)
COIN_COLOR_1 = (72, 54, 0)
PURPLE_COIN_COLOR_1 = (32, 0, 72)
ROCK_COLOR_1 = (62, 67, 88)

lane = 1
width, height = size()
checkHeight = 3*height/4
inc = 2
def findObject():
    global lane
    global checkHeight
    checkHeightInt = int(checkHeight)
    global inc
    
    if lane == 0:
        if pixelMatchesColor(int(width/2 - 342), checkHeightInt, ROCK_COLOR_1):
            move("right")
            checkHeight -= inc
            print("Obstacle check height: {}".format(checkHeight))
            moveTo(int(width/2 - 114), checkHeightInt)
    elif lane == 1:
        if pixelMatchesColor(int(width/2 - 114), checkHeightInt, ROCK_COLOR_1):
            move("right")
            checkHeight -= inc
            print("Obstacle check height: {}".format(checkHeight))
            moveTo(int(width/2 + 114), checkHeightInt)
    elif lane == 2:
        if pixelMatchesColor(int(width/2 + 114), checkHeightInt, ROCK_COLOR_1):
            move("right")
            checkHeight -= inc
            print("Obstacle check height: {}".format(checkHeight))
            moveTo(int(width/2 + 342), checkHeightInt)
    else:
        if pixelMatchesColor(int(width/2 + 342), checkHeightInt, ROCK_COLOR_1):
            move("left")
            checkHeight -= inc
            print("Obstacle check height: {}".format(checkHeight))
            moveTo(int(width/2 + 114), checkHeightInt)

def move(direction="left"):
    global lane
    if direction == "right":
        keyDown("d")
        print("\nObstacle in lane {}".format(lane))
        lane += 1
        print("Currently in lane {}".format(lane))
        keyUp("d")
    else:
        keyDown("a")
        print("\nObstacle in lane {}".format(lane))
        lane -= 1
        print("Currently in lane {}".format(lane))
        keyUp("a")
try:
    while True:
        findObject()
except KeyboardInterrupt:
        pass