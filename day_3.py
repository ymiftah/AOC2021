#%%
import numpy as np

##########################
##  PART 1
##########################

# Read file

sum_ = 0
n_lines = 0
with open('day_3_input.txt') as file:
    for line in file:
        n_lines += 1
        sum_   += np.array(list(line.strip()), dtype=int) 
gamma = np.round(sum_/n_lines).astype(int)
gamma = int(''.join(str(g) for g in gamma),2)
epsilon = np.round(1 - sum_/n_lines).astype(int)
epsilon = int(''.join(str(e) for e in epsilon), 2)
print(gamma * epsilon)

################
# PART 2
################
def decode_oxygen(all_values, pos):
    values = set(all_values)
    if len(values) > 1:
        ones = set(v for v in values if v[pos] == '1')
        zeros = values - ones
        if len(ones) >= len(zeros):
            return decode_oxygen(ones, pos+1)
        else:
            return decode_oxygen(zeros, pos+1)
    else:
        return int(min(values).strip(),2)

def decode_co2(all_values, pos):
    values = set(all_values)
    if len(values) > 1:
        ones = set(v for v in values if v[pos] == '1')
        zeros = values - ones
        if len(ones) < len(zeros):
            return decode_co2(ones, pos+1)
        else:
            return decode_co2(zeros, pos+1)
    else:
        return int(min(values).strip(),2)

with open('day_3_input.txt') as file:
    all_values = file.readlines()
oxygen = decode_oxygen(all_values,0)
co2 = decode_co2(all_values, 0)
print('Part 2 ', oxygen * co2)

# %%
