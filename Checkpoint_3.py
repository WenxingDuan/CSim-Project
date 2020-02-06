import numpy as np
import matplotlib.pyplot as plt


class mandelbrot(object):
    def __init__(self, xMin, xMax, yMin, yMax, resolution, nMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.resolution = resolution
        self.nMax = nMax

    def checkMandelbrot(self, c):
        z = 0
        for i in range(0, self.nMax):
            z = z**2 + c

            if (abs(z) > 2):
                return i
        return self.nMax
        # Check if c in Mandelbrot set. If not, return iteration number

    def drawMandelbrot(self):
        x = np.linspace(self.xMin, self.xMax, self.resolution)
        y = np.linspace(self.yMin, self.yMax, self.resolution)
        #generate two lists with resolution numbers each
        mandelbrot = []
        for j in y:
            trans = []
            for i in x:
                c = i + 1j * j
                trans.append(self.checkMandelbrot(c))
            mandelbrot.append(trans)
        #generate the mandelbrot set as a 500*500 list
        plt.imshow(mandelbrot,
                   extent=[self.xMin, self.xMax, self.yMin, self.yMax])
        plt.ylabel('Im(c)')
        plt.xlabel('Re(c)')
        plt.show()


class julia(object):
    def __init__(self, cX, cY, xMin, xMax, yMin, yMax, resolution, nMax):
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.resolution = resolution
        self.nMax = nMax
        self.cX = cX
        self.cY = cY

    def checkJulia(self, z, cx, cy):
        c = cy + 1j * cy
        for i in range(0, self.nMax):
            z = z**2 + c
            if (abs(z) > 2):
                return i
        return self.nMax

    def drawJulia(self):
        x = np.linspace(self.xMin, self.xMax, self.resolution)
        y = np.linspace(self.yMin, self.yMax, self.resolution)

        Julia = []
        for i in x:
            trans = []
            for j in y:
                z = i + 1j * j
                trans.append(self.checkJulia(z, self.cX, self.cY))
            Julia.append(trans)
        # print(len(Julia))
        plt.imshow(Julia,extent=[self.xMin, self.xMax, self.yMin, self.yMax])
        plt.ylabel('Im(c)')
        plt.xlabel('Re(c)')
        plt.show()


def main():
    mandelbrot(-2.025, 0.6, -1.125, 1.125, 500, 255).drawMandelbrot()
    julia(0, -1,-2.025, 0.6, -1.125, 1.125, 500, 255).drawJulia()


if __name__ == '__main__':
    main()




    