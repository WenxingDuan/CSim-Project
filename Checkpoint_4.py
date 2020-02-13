import random
import matplotlib.pyplot as plt


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
                   extent=[0, self.roadLength, 0, self.totalTime],cmap=plt.cm.gray_r)
        
        plt.show()


theRoad = road(2, 5, 5)
theRoad.roadGenerate()
print(theRoad.timeLoop())
theRoad.drawPic()
