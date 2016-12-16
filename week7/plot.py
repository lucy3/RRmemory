import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.zeros([30,30])
Y = np.zeros([30,30])
Z = np.zeros([30,30])

with open(sys.argv[1], 'r') as f:
    i = 0
    for line in f:
        if i == 0:
            i += 1
            continue
        numcat, numobs, err = tuple(line[:-1].split())
        X[int(numcat)-1,int(numobs)-1] = float(numcat)
        Y[int(numcat)-1,int(numobs)-1] = float(numobs)
        Z[int(numcat)-1,int(numobs)-1] = float(err)

#print result

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('# categories')
ax.set_ylabel('timestep (# observation)')
ax.set_zlabel('Mean square deviation')
plt.show()
