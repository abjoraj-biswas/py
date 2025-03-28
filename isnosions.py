import numpy as np
import math
pointsMatrix=np.array([[1,2],[0,0],[0,0]])
R_z = np.array([[math.cos(theta),    -math.sin(theta),    0],
                    [math.sin(theta),    math.cos(theta),     0],
                    [0,                     0,                      1]
                    ])
rotatedPoints=np.dot(R_z,pointsMatrix)

print("Rotated points \n",rotatedPoints)
