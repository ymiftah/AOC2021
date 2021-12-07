#%%
import numpy as np

init_fishes = np.fromfile('day_6_input.txt', sep=',', dtype=np.int64)

def fishes_after_n_days(n):
    fishes = np.zeros(9)
    for i in init_fishes:
        fishes[i] += 1
    for _ in range(n):
        roll = fishes[0]
        fishes[:-1] = fishes[1:]
        fishes[8] = roll
        fishes[6] += roll
    print('Number of fishes after {} days :'.format(n), np.sum(fishes))
# %%
fishes_after_n_days(80)
fishes_after_n_days(256)
# %%
