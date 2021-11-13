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
COIN_COLORS = ((72, 54, 0), (249, 255, 220), (255, 247, 28), (255, 134, 32), (185, 49, 0), (255, 185, 126))
PURPLE_COIN_COLORS = ((32, 0, 72), (250, 220, 255), (179, 28, 255), (65, 0, 185), (126, 32, 255), (146, 126, 255))
ROCK_COLORS = ((62, 67, 88), (87, 94, 124), (160, 165, 188), (124, 131, 163))

lane = 1
width, height = size()
obstacleCheckHeight = 7*height/10
coinCheckHeight = height/2
inc = 2
lastObstaclePixel = BACKGROUND_COLOR

def findObject():
    global lane
    global obstacleCheckHeight, inc
    # check lane 0
    #px = readPixel(0)
    for ROCK_COLOR in ROCK_COLORS:
        if pixelMatchesColor(int(width/2 - 342), checkHeightInt, ROCK_COLOR, tolerance=25) and lane == 0: # avoid rock if in lane 0
            move("right")
            obstacleCheckHeight -= inc
            print("Obstacle check height: {}".format(obstacleCheckHeight))
    
    # check lane 1
    #px = readPixel(1)
    for ROCK_COLOR in ROCK_COLORS:
        if pixelMatchesColor(int(width/2 - 114), checkHeightInt, ROCK_COLOR) and lane == 1: # avoid rock if in lane 1
            move("right")
            obstacleCheckHeight -= inc
            print("Obstacle check height: {}".format(obstacleCheckHeight))
    
    # check lane 2
    #px = readPixel(2)
    for ROCK_COLOR in ROCK_COLORS:
        if pixelMatchesColor(int(width/2 + 114), checkHeightInt, ROCK_COLOR) and lane == 2: # avoid rock if in lane 2
            move("right")
            obstacleCheckHeight -= inc
            print("Obstacle check height: {}".format(obstacleCheckHeight))
    
    # check lane 3
    #px = readPixel(3)
    for ROCK_COLOR in ROCK_COLORS:
        if pixelMatchesColor(int(width/2 + 342), checkHeightInt, ROCK_COLOR) and lane == 3: # avoid rock if in lane 3
            move("left")
            obstacleCheckHeight -= inc
            print("Obstacle check height: {}".format(obstacleCheckHeight))

def readPixel(readLane):
    global obstacleCheckHeight, coinCheckHeight
    global lastObstaclePixel
    obstacleCheckHeightInt, coinCheckHeightInt = int(obstacleCheckHeight), int(coinCheckHeight)
    if readLane == 0:
        obstaclePixel = pixel(int(width/2 - 342), obstacleCheckHeightInt)
    elif readLane == 1:
        obstaclePixel = pixel(int(width/2 - 114), obstacleCheckHeightInt)
    elif readLane == 2:
        obstaclePixel = pixel(int(width/2 + 114), obstacleCheckHeightInt)
    else:
        obstaclePixel = pixel(int(width/2 + 342), obstacleCheckHeightInt)
    
    if obstaclePixel != lastObstaclePixel:
        print(obstaclePixel)
    lastObstaclePixel = obstaclePixel
    return obstaclePixel

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