from pyautogui import *
from PIL import Image
import time

START_TIME = [time.time(), 0]

BACKGROUND_COLOR = (149, 191, 219)
LANE_COLOR = (163, 200, 224)
DEAD_COLORS = ((30, 38, 44), (12, 13, 18))
COIN_COLORS = ((72, 54, 0), (249, 255, 220), (255, 247, 28), (255, 134, 32), (185, 49, 0), (255, 185, 126))
PURPLE_COIN_COLORS = ((32, 0, 72), (250, 220, 255), (179, 28, 255), (65, 0, 185), (126, 32, 255), (146, 126, 255))
ROCK_COLORS = ((62, 67, 88), (87, 94, 124), (160, 165, 188), (124, 131, 163))
COLORS = (BACKGROUND_COLOR, LANE_COLOR, DEAD_COLORS, COIN_COLORS, PURPLE_COIN_COLORS, ROCK_COLORS)

lane = 1

width, height = size()

# center of boat is at 9*height/10
obstacleCheckHeight = 0.72 * height # should be between 0.6 - 0.75
coinCheckHeight = 7*height/10 # my favorite number is 72. did you know that?
inc = 1.5 # tested: 0, 0.5, 1, 1.5, 2, 3, 4
lastObstaclePixel = BACKGROUND_COLOR

def findObstacle(lane, mode=0):
    # returns True if there is a rock, False otherwise
    global obstacleCheckHeight
    
    if not mode:
        px = readPixel(lane, obstacleCheckHeight)
        if px in ROCK_COLORS: # rock is in lane i
            changeCheckHeight()
            return True
        return False # no rock
    else:
        global coinCheckHeight
        px = readPixel(lane, coinCheckHeight)
        if px in ROCK_COLORS:
            changeCheckHeight()
            return True
    return False

def findCoin():
    global lane
    global coinCheckHeight
    
    # check lane 0
    px = readPixel(0, coinCheckHeight)
    if (px in COIN_COLORS or px in PURPLE_COIN_COLORS) and not findObstacle(0, 1): # found coin or purple coin (doesn't really matter)
        if lane == 0:
            pass # no movement necessary
        elif lane == 1:
            move("left")
        elif lane == 2 and px in PURPLE_COIN_COLORS:
            move("left", 2)
        """elif px in PURPLE_COIN_COLORS:
            move("left", 3)""" # moving over three lanes doesn't really work
        #return 0
    
    # check lane 1
    px = readPixel(1, coinCheckHeight)
    if (px in COIN_COLORS or px in PURPLE_COIN_COLORS) and not findObstacle(1, 1):
        if lane == 0:
            move("right")
        elif lane == 1:
            pass # no movement necessary
        elif lane == 2:
            move("left")
        elif lane == 3 and px in PURPLE_COIN_COLORS:
            move("left", 2)
        #return 1
    
    # check lane 2
    px = readPixel(2, coinCheckHeight)
    if (px in COIN_COLORS or px in PURPLE_COIN_COLORS) and not findObstacle(2, 1):
        if lane == 0 and px in PURPLE_COIN_COLORS:
            move("right", 2)
        elif lane == 1:
            move("right")
        elif lane == 2:
            pass # no movement necessary
        elif lane == 3:
            move("left")
        #return 2
    
    # check lane 3
    px = readPixel(3, coinCheckHeight)
    if (px in COIN_COLORS or px in PURPLE_COIN_COLORS) and not findObstacle(3, 1):
        """if lane == 0 and px in PURPLE_COIN_COLORS:
            move("right", 3)"""
        if lane == 1 and px in PURPLE_COIN_COLORS:
            move("right", 2)
        elif lane == 2:
            move("right")
        elif lane == 3:
            pass # no movement necessary
        #return 3
    
    # end script if you die
    if px in DEAD_COLORS:
        raise KeyboardInterrupt
    #return -1

def changeCheckHeight():
    global START_TIME, inc, obstacleCheckHeight
    
    if START_TIME[1] == 0 and time.time() - START_TIME[0] >= 20:
        inc += 2
        START_TIME[1] += 1
    elif START_TIME[1] == 1 and time.time() - START_TIME[0] >= 30:
        inc += 2
        START_TIME[1] += 1
    elif START_TIME[1] == 2 and time.time() - START_TIME[0] >= 35:
        inc += 2
        START_TIME[1] += 1
    elif START_TIME[1] == 3 and time.time() - START_TIME[0] >= 40:
        inc += 2
        START_TIME[1] += 1
    
    obstacleCheckHeight -= inc
    print(inc)

def readPixel(lane, checkHeight):
    global lastObstaclePixel
    checkHeightInt = int(checkHeight)
    
    if lane == 0:
        obstaclePixel = pixel(int(width/2 - 342), checkHeightInt)
    elif lane == 1:
        obstaclePixel = pixel(int(width/2 - 114), checkHeightInt)
    elif lane == 2:
        obstaclePixel = pixel(int(width/2 + 114), checkHeightInt)
    else:
        obstaclePixel = pixel(int(width/2 + 342), checkHeightInt)
    """
    if (obstaclePixel != lastObstaclePixel) and (obstaclePixel not in COLORS):
        print(obstaclePixel)
    lastObstaclePixel = obstaclePixel
    """
    return obstaclePixel

def move(direction="left", distance=1):
    global lane
    
    for i in range(distance):
        if direction == "right":
            keyDown("d")
            lane += 1
            #print("Currently in lane {}".format(lane))
            keyUp("d")
        else:
            keyDown("a")
            lane -= 1
            #print("Currently in lane {}".format(lane))
            keyUp("a")


try:
    while True:
        if findObstacle(lane):
            if lane <= 1:
                move("right")
            else:
                move()
        elif time.time() - START_TIME[0] <= 30:
            findCoin()
except KeyboardInterrupt:
        pass