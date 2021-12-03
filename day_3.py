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
def decode(all_values, pos, type='oxygen'):
    values = set(all_values)
    if len(values) > 1:
        ones = set(v for v in values if v[pos] == '1')
        zeros = values - ones
        if type == 'oxygen':
            return decode(ones, pos+1, type=type) \
                    if len(ones) >= len(zeros) else decode(zeros, pos+1, type=type)
        else:
            return decode(ones, pos+1, type=type) \
                    if len(ones) < len(zeros) else decode(zeros, pos+1, type=type)
    else:
        return int(min(values).strip(),2)


with open('day_3_input.txt') as file:
    all_values = file.readlines()
oxygen = decode(all_values, 0, type='oxygen')
co2 = decode(all_values, 0, type='co2')
print('Part 2 ', oxygen * co2)

# %%
