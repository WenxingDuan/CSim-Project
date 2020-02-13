import random


class road(object):
    def __init__(self, carNum, roadLength, totalTime):
        self.carNun = carNum
        self.totalTime = totalTime
        self.roadLength = roadLength
        self.roadList = []

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

theRoad = road(5,10,10)
print(theRoad.nextTime([1,1,0,1,0]))
