import matplotlib.pyplot as plt
from enum import Enum
import csv
import numpy as np

#maxSpeed = float(input('How fast is the robot at its fastest? (cm/s)\n')) #In cm/second
#maxAccel = float(input('How fast does the robot accelerate? (cm/s/s)\n')) #In cm/second/second 

#maxSpeed = 487 #Cm/s  
#maxAccel = 243.5 #Cm/s squared

maxSpeed = 105
maxAccel = 15

target = float(input('How far do you want to move?\n')) #In cm

outputFile = open('.\Outputs\\' + str(target) + '.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

secondsElapsed = 0
currentPosition = 0
currentSpeed = 0
currentAccel = 0

timeList = []
positionList = []
speedList = []
accelList = []

class States(Enum):
    ACCLERATING = 0
    COASTING = 1
    DECELERATING = 2

currentState = States.ACCLERATING

timePerIteration = 10 # In ms

millisecondsElapsed = 0

firstTime = True

while not (currentSpeed > -0.0001 and currentSpeed < 0.0001) or firstTime:
    firstTime = False

    distanceToDecelerate = (currentSpeed ** 2) / (2 * maxAccel) 
    distanceToTarget = target - currentPosition
    
    #Update values
    currentPosition += currentSpeed * (timePerIteration/1000)
    
    if distanceToTarget <= distanceToDecelerate:
        currentState = States.DECELERATING
    elif currentSpeed < maxSpeed:
        currentState = States.ACCLERATING
    else:
        currentState = States.COASTING

    #Update accleration based on state
    if currentState == States.ACCLERATING: currentAccel = maxAccel    
    if currentState == States.COASTING: currentAccel = 0
    if currentState == States.DECELERATING: currentAccel = -maxAccel

    #Update Speed
    currentSpeed += currentAccel * timePerIteration/1000

    #Add values to array
    timeList += [millisecondsElapsed]
    positionList += [currentPosition]
    speedList += [currentSpeed]
    accelList += [currentAccel]

    #Write time, speed, and position to file
    outputWriter.writerow([millisecondsElapsed, currentSpeed, currentPosition])

    millisecondsElapsed += timePerIteration


outputFile.close()

#Plot everything
ax = plt.subplot(111)

ax.set_prop_cycle('color',plt.cm.spectral(np.linspace(0,10,40)))

plt.plot(timeList, positionList)
plt.plot(timeList, speedList)
plt.plot(timeList, accelList)

plt.xlabel('Time (milliseconds)')
plt.legend(['Position (cm)', 'Speed (cm/s)', 'Acceleration (cm/s/s)'], loc='upper left')

plt.savefig('.\Graphs\\' + str(target) + 'CM.png')
plt.show()
