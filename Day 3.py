'''trying np.sort'''
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

'''trying np.where'''
import numpy as np 
np.where([[True, False], [True, True]], 
[[1, 2], [3, 4]], [[5, 6], [7, 8]])