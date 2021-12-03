#%%
import numpy as np

##########################
##  PART 1
##########################

# Read file
depth_measurements = np.genfromtxt('day_1_input.txt', delimiter=',')

# Compute depth increments
depth_increments = np.diff(depth_measurements)

# Answer is the sum of positive increments
answer = np.sum(depth_increments > 0)

# Display answer
print('Part 1 answer :', answer)

######################################
## Part 2
#################################

# Compute rolling sum as a convolution product
sliding_window = np.convolve(depth_measurements, np.ones(3),'valid')
# Compute increments as before
sliding_window_increments = np.diff(sliding_window)
# Answer is the sum of positive increments
answer = np.sum(sliding_window_increments > 0)
print('Part 2 Answer :', answer)
