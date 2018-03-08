import matplotlib.pyplot as plt
from enum import Enum

class States(Enum):
    ACCLERATING = 0
    COASTING = 1
    DECELERATING = 2

maxSpeed = 152 #In cm/second
maxAccel = 60 #In cm/second/second 
target = 2000 #In cm


secondsElapsed = 0
currentPosition = 0
currentSpeed = 0

currentState = States.ACCLERATING

timeList = []
positionList = []
speedList = []

timePerIteration = 0.1 # In seconds


while currentPosition < target:
    if currentSpeed >= maxSpeed: 
        currentState == States.COASTING
    

    if currentPosition >= target - (currentSpeed/timePerIteration):
        currentState == States.DECELERATING
    
    if currentState == States.ACCLERATING:
        currentSpeed += maxAccel * timePerIteration

    if currentState == States.DECELERATING:
        currentSpeed -= maxAccel * timePerIteration

    secondsElapsed += timePerIteration
    currentPosition += currentSpeed * timePerIteration

    print('Seconds Elapsed: ' + str(secondsElapsed))
    print('Current Pos: ' + str(currentPosition))
    print('Current Speed: ' + str(currentSpeed))

    timeList += [secondsElapsed]
    positionList += [currentPosition]
    speedList += [currentSpeed]


plt.plot(timeList, speedList)

plt.xlabel('Time (seconds)')
plt.ylabel('Speed List')


plt.show()