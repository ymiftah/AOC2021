# %%#%%
import numpy as np

def data_reader(file_path):
    with open(file_path) as file:
        segments = []
        diagonals = []
        dimensions = (0,0)
        for line in file:
            A, B = line.split(' -> ')
            x1, y1 = [int(a) for a in A.split(',')]
            x2, y2 = [int(b) for b in B.split(',')]
            if  (x1 != x2) and (y1!=y2):
                diagonals.append(sorted(((x1,y1),(x2,y2))))
            else:
                segments.append(sorted(((x1,y1),(x2,y2))))
            X = max(x1+1, x2+1, dimensions[0])
            Y = max(y1+1, y2+1, dimensions[1])
            dimensions = (X,Y)
    return segments, diagonals, dimensions

segments, diagonals, dimensions = data_reader('day_5_input.txt')
field = np.zeros(dimensions)
for (x1,y1),(x2,y2) in segments:
     field[x1:x2+1,y1:y2+1] += 1
print('No diagonals ', np.sum(field >= 2))

for (x1,y1),(x2,y2) in diagonals:
    yr = 1 if y2 > y1 else -1
    x_range = range(x1,x2+1)
    y_range = list(range(min(y1,y2),max(y1,y2)+1))[::yr]
    coords = zip(x_range, y_range)
    for x,y in coords: field[x,y] += 1
print('With diagonals ', np.sum(field >= 2))

# # %%


# %%
