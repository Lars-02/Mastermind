from random import randint, sample


class Board:
    def __init__(self, amount_of_positions=4, amount_of_colors=6, can_have_double_colors=False):
        self.guesses = {}
        if can_have_double_colors:
            self.colors = [randint(0, amount_of_colors)
                           for _ in range(amount_of_positions)]
        else:
            self.colors = sample(range(amount_of_colors), amount_of_positions)

        print(self.colors)
