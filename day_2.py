position = dict(forward=0, down=0, up=0)

with open('day_2_input.txt') as file:
    for line in file:
        direction, length = line.split()
        position[direction] += int(length)

final_horizontal, final_vertical = position['forward'], position['down'] - position['up']
answer = final_horizontal * final_vertical
print('Part 1' , answer)

position = dict(horizontal=0, depth=0, aim=0)

with open('day_2_input.txt') as file:
    for line in file:
        direction, length = line.split()
        if direction == 'down':
            position['aim'] += int(length)
        elif direction == 'up':
            position['aim'] -= int(length)
        elif direction == 'forward':
            position['horizontal'] += int(length)
            position['depth'] += position['aim'] * int(length)

final_horizontal, final_vertical = position['horizontal'], position['depth']
answer = final_horizontal * final_vertical
print('Part 2' , answer)