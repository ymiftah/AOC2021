#%%
import numpy as np
positions = np.fromfile('day_7_input.txt', sep=',', dtype=np.int64)

# Part 1
# Minimiser is the median
print('Part 1 - Total Fuel: ', np.linalg.norm(positions - np.median(positions),1))

# Part 2
# Minimiser is one of two options
tests = np.floor(np.mean(positions)), np.ceil(np.mean(positions))
def f(x):
    ns = abs(positions - x)
    return sum(ns*(ns+1)/2)
print('Part 2 - Total Fuel: ', min(map(f, tests)))

# %%
