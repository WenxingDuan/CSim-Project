import math
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from numpy.linalg import norm


class simulation(object):
    def __init__(self, marsMass, marsIninitialPosition, marsIninitialVelocity,
                 phobosMass, phobosRadius, timestep):
        self.G = 6.67 * (10**(-11))
        self.m1 = marsMass
        self.r1 = marsIninitialPosition  #Array([0,0])
        self.v1 = marsIninitialVelocity  #Array([0,0])
        self.m2 = phobosMass
        self.r12_S = phobosRadius
        self.r12 = np.array([self.r12_S, 0])
        self.r2 = np.array([phobosRadius, 0])
        self.v2_S = math.sqrt((self.G * self.m1) / (self.r12_S))
        self.v2 = np.array([0, self.v2_S])
        self.timestep = timestep
        self.patches = []
        self.patches.append(plt.Circle((0, 0), 500000, color='b', animated=True))
        self.patches.append(plt.Circle((0, 0), 100000, color='r', animated=True))
        # 31968 sec

    def update(self, t):
        force2 = (self.G *
                  ((self.m1 * self.m2) / (norm(self.r2 - self.r1)**2))) * (
                      (self.r1 - self.r2) / norm((self.r2 - self.r1)))
        a2 = force2 / self.m2
        self.v2 = self.v2 + a2 * t
        self.r2 = self.r2 + self.v2 * t
        force1 = (self.G *
                  ((self.m1 * self.m2) / (norm(self.r2 - self.r1)**2))) * (
                      (self.r2 - self.r1) / norm((self.r1 - self.r2)))
        a1 = force1 / self.m1
        self.v1 = self.v1 + a1 * t
        self.r1 = self.r1 + self.v1 * t

    def animate(self, i):
        self.update(i)
        self.patches[0].center = (self.r1[0], self.r1[1])
        self.patches[1].center = (self.r2[0], self.r2[1])
        return self.patches

    def init(self):
        return self.patches

    def display(self):
        fig = plt.figure()
        ax = plt.axes()
        ax.set_xlim(-11**7, 11**7)
        ax.set_ylim(-11**7, 11**7)
        for i in range(0, len(self.patches)):
            ax.add_patch(self.patches[i])
        anim = FuncAnimation(fig,
                             self.animate,
                             init_func=self.init,
                             frames=60,
                             repeat=True,
                             interval=30,
                             blit=True)
        plt.show()


a = simulation(6.4185 * 10**23, np.array([0, 0]), np.array([0, 0]),
               1.06 * 10**16, 9.3773 * 10**6, 10)

a.display()