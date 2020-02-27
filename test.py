import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# create plot elements
fig = plt.figure()
ax = plt.axes()

# create empty list for circles
patches = []

# create circles centred at initial position and them append them to the list
patches.append(plt.Circle((0, math.sin(0)), 0.1, color = 'g', animated = True))
patches.append(plt.Circle((0, math.cos(0)), 0.1, color = 'b', animated = True))

# add circles to axes
for i in range(0, len(patches)):
    ax.add_patch(patches[i])

def init():
    # initialiser for animator
    return patches
     
def animate(i):
    # update the position of the circles
    xpos += xincr
    patches[0].center = (xpos, math.sin(xpos))
    patches[1].center = (xpos, math.cos(xpos))
    return patches
anim = FuncAnimation(fig, animate, init_func = init, frames = 50, repeat = False, interval = 50, blit = True)
plt.show()