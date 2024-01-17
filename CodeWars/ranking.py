class User:
    _ranking = [i for i in range(-8, 9) if i != 0]
    def __init__(self):
        self.rank = self._ranking[0]
        self.progress = 0
        
    def inc_progress(self, prog):
        try:
            prog_idx = self._ranking.index(prog)
            rank_idx = self._ranking.index(self.rank)
            if self.rank != self._ranking[-1]:
                if prog_idx == (rank_idx - 1):
                    self.progress += 1
                elif prog_idx == rank_idx:
                    self.progress += 3
                elif prog_idx > rank_idx:
                    self.progress += 10 * (
                        (prog_idx - rank_idx)
                        ** 2)
                if self.progress > 99:
                    level, exp = divmod(self.progress, 100)
                    self.rank = self._ranking[rank_idx+level]
                    if self.rank != self._ranking[-1]:
                        self.progress = exp
                    else:
                        self.progress = 0
        except ValueError:
            raise Exception("Invalid ranking")

user = User()
user.inc_progress(-1)
print(user.progress)
print(user.rank)