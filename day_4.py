#%%
import numpy as np

class Board(object):
    def __init__(self, np_array, tag):
        self.table = np_array
        self.tag = tag
        self.checked = np.zeros_like(np_array)
        self.won = False
        self.score = 0

    def _check_number(self, number):
        self.checked[self.table == number] = 1

    def _is_game_over(self):
        horizontal = np.prod(self.checked, axis=1)
        vertical = np.prod(self.checked, axis=0)
        return np.any(horizontal) or np.any(vertical)

    def draw_number(self, number):
        self._check_number(number)
        if self._is_game_over():
            self.won = True
            self.score =  np.sum(self.table * (1 - self.checked)) * number
            return self.score
        return 0


class BingoGame(object):
    def __init__(self, file_path):
        with open(file_path) as file:
            lines=file.readlines()
        self.plays = np.fromstring(lines[0].strip(), dtype=np.int32, sep=',')

        a = ''.join(lines[2:])
        tables = np.fromstring(a.replace('\n', ' '), sep=' ', dtype=np.int32).reshape((-1,5))
        X,Y = tables.shape
        self.n_tables = int(X/5)
        tables = [tables[i:i+5, :] for i in range(0, X, 5)]
        self.boards = [Board(array, i+1) for i, array in enumerate(tables)]

    def play_game(self):
        for p in self.plays:
            for b in self.boards:
                score = b.draw_number(p)
                if score > 0:
                    return b.tag, score

    def play_to_lose(self):
        n_in_play = self.n_tables
        for p in self.plays:
            for b in self.boards:
                if b.won:
                    continue
                score = b.draw_number(p)
                if score > 0:
                    n_in_play -= 1
                if n_in_play == 0:
                    return b.tag, score
#%%
print('PART 1')
board, score = BingoGame('day_4_input.txt').play_game()
print('Winner is board {} with score {}'.format(board, score))

# %%

print('PART 2')
board, score = BingoGame('day_4_input.txt').play_to_lose()
print('Loser is board {} with score {}'.format(board, score))
# %%
