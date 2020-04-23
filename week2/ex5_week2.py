import numpy as np
x1 = np.arange(8)
x2 = np.reshape(x1,(2,4))
print(np.roll(x2,1,axis=0))

