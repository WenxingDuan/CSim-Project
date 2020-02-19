import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class road(object):
    def __init__(self, carNum, roadLength, totalTime):
        self.carNun = int(carNum)
        self.totalTime = int(totalTime)
        self.roadLength = int(roadLength)
        self.roadList = []
        self.finalList = []
        self.roadTimeList = []

    def roadGenerate(self):
        for i in range(self.roadLength):
            self.roadList.append(0)

        while (sum(self.roadList) != self.carNun):
            rand = random.randrange(self.roadLength)
            self.roadList[rand] = 1

    def nextTime(self, oldRoadList):
        newList = []
        for i in range(len(oldRoadList)):
            newList.append(0)
        for i in range(len(oldRoadList)):
            if (i == 0) or (i == len(oldRoadList) - 1):
                #===============================
                # i == 0
                if i == 0:
                    if oldRoadList[i] == 1:
                        if oldRoadList[i + 1] == 1:
                            newList[i] = 1
                        else:
                            newList[i] = 0
                    else:
                        if oldRoadList[len(oldRoadList) - 1] == 1:
                            newList[i] = 1
                        else:
                            newList[i] = 0
                #===============================
                # i == len(oldRoadList)-1
                else:
                    if oldRoadList[i] == 1:
                        if oldRoadList[0] == 1:
                            newList[i] = 1
                        else:
                            newList[i] = 0
                    else:
                        if oldRoadList[i - 1] == 1:
                            newList[i] = 1
                        else:
                            newList[i] = 0
            else:
                if oldRoadList[i] == 1:
                    if oldRoadList[i + 1] == 1:
                        newList[i] = 1
                    else:
                        newList[i] = 0
                else:
                    if oldRoadList[i - 1] == 1:
                        newList[i] = 1
                    else:
                        newList[i] = 0

        return newList

    def timeLoop(self):
        self.finalList = []
        returnList = []
        self.finalList.append(self.roadList)
        for i in range(self.totalTime):
            self.finalList.append(self.nextTime(self.finalList[i]))

        for i in range(len(self.finalList)):
            returnList.append(self.finalList[len(self.finalList) - 1 - i])

        self.finalList = returnList
        return self.finalList

    def drawPic(self):
        plt.imshow(self.finalList,
                   extent=[0, self.roadLength, 0, self.totalTime],
                   cmap=plt.cm.gray_r)
        plt.show()


def averageSpeed(carNum, roadLength):
    theRoad = road(carNum, roadLength, roadLength*2)
    theRoad.roadGenerate()
    roadList = list(reversed(theRoad.timeLoop()))
    difference = 0
    i= roadLength*2 - 1
    for j in range(0, len(roadList[i])):
        difference = difference + abs(roadList[i + 1][j] - roadList[i][j])
    return (difference / 2) / sum(roadList[0])


def main():
    carNum = int(input("Car Numer: "))
    roadLength = int(input("Road Length: "))
    time = int(input("Time: "))
    theRoad = road(carNum, roadLength, time)
    theRoad.roadGenerate()
    theRoad.timeLoop()
    theRoad.drawPic()
    speedList = []
    for i in range(1, roadLength + 1):
        speedList.append((i, averageSpeed(i, roadLength)))
    # print(speedList)
    ax = plt.axes()
    for i in speedList:
        ax.add_patch(patches.Circle(i, 0.01, color='r'))
    plt.xlim(0, roadLength)
    plt.ylim(0, 1)
    plt.show()

if __name__ == '__main__':
    main()