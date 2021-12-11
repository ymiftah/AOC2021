#%%
import numpy as np

scoreTable = {')': 3, ']':57, '}':1197, '>':25137}
scoreTable2 = {'(': 1, '[':2, '{':3, '<':4}

closingTable = {')': '(', ']':'[', '}':'{', '>':'<'}
openingTable = {val:key for key,val in closingTable.items()}

def check_line(line):
    opens = []
    for c in line.strip():
        if c in ('{', '[', '(', '<'):
            opens.append(c)
        else:
            if closingTable[c] == opens[-1]:
                opens.pop(-1)
            else:
                return opens, scoreTable[c]
    return opens, 0

def check_incomplete(remaining):
    score = 0
    for c in remaining[::-1]:
        score *= 5
        score += scoreTable2[c]
    return score

incomplete = []
with open('day_10_input.txt') as file:
    scores = 0
    for line in file:
        remains, score = check_line(line)
        scores += score
        if score == 0:
            incomplete.append(remains)
# %%
print('Part 1')
print(score)
# %%
a = [check_incomplete(line) for line in incomplete]
print('Part 2')
print(np.median(a))
# %%
