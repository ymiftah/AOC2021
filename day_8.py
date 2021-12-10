
#%%
display = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg')
}

uniques = []
values = []
with open('day_8_input.txt') as file:
    for line in file:
        left, right = line.split('|')
        uniques.append([''.join(sorted(s)) for s in left.strip().split(' ')])
        values.append([''.join(sorted(s)) for s in right.strip().split(' ')])


def find_easies(uniques):
    easy = dict()
    for i in uniques:
        if len(i) == 2:
            easy[1] = i
        elif len(i) == 4:
            easy[4] = i
        elif len(i) == 3:
            easy[7] = i
        elif len(i) == 7:
            easy[8] = i
    return easy

def match_easies(easies, values):
    a = set(easies.values())
    b = set(values)
    return len([_ for _ in values if _ in a.intersection(b)])

#%%
print('Part 1')
result = sum([match_easies(find_easies(u), val)for u, val in zip(uniques, values)])
print(result)
# %%
def find_3(unique, decoded):
    seven = decoded[7]
    temp = [u for u in unique
        if len(u) == 5 and
        set(seven) < set(u) and
        not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_9(unique, decoded):
    three = decoded[3]
    temp = [u for u in unique
        if len(u) == 6 and
        set(three) < set(u) and
        not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_5(unique, decoded):
    nine = decoded[9]
    temp = [u for u in unique
        if len(u) == 5 and
        set(u) < set(nine) and
        not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_6(unique, decoded):
    five = decoded[5]
    temp = [u for u in unique
        if len(u) == 6 and
        set(five) < set(u) and
        not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_0(unique, decoded):
    temp = [u for u in unique
        if len(u) == 6 and
        not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_2(unique, decoded):
    temp = [u for u in unique
        if not u in decoded.values()]
    assert len(temp) == 1
    return temp[0]

def find_all(unique):
    decoded = find_easies(unique)
    decoded[3] = find_3(unique, decoded)
    decoded[9] = find_9(unique, decoded)
    decoded[5] = find_5(unique, decoded)
    decoded[6] = find_6(unique, decoded)
    decoded[0] = find_0(unique, decoded)
    decoded[2] = find_2(unique, decoded)
    return decoded

decoded = []
for un, code in zip(uniques, values):
    decode = {val: key for key,val in find_all(un).items()}
    number = ''.join([str(decode[key]) for key in code])
    decoded.append(number)
# %%
print('Part 2:')
print(sum([int(d) for d in decoded]))

