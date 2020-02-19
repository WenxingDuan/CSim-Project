import matplotlib.pyplot as plt
import matplotlib.patches as patches

# set up plot   
ax = plt.axes()

r = 0.2

for i in range(1, 5):
    for j in range(1, 4):
        ax.add_patch(patches.Circle((i,j), r, color = 'r'))

# scale axis for correct aspect ratio


# set axis limits
plt.xlim(0, 5)
plt.ylim(0, 4)

plt.show()

