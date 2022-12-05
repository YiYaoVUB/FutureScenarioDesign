import numpy as np
import scipy.io as scio

grid_frac = np.zeros([2, 2])
scio.savemat('C:\Research2\Output_data\grid_frac.mat', {'grid_frac': grid_frac})