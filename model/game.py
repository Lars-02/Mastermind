from model.board import Board


class Game:
    def __init__(self, amount_of_guesses, amount_of_positions, amount_of_colors, can_have_double_colors):
        self.amount_of_guesses = amount_of_guesses
        self.amount_of_colors = amount_of_colors
        self.amount_of_positions = amount_of_positions
        self.can_have_double_colors = can_have_double_colors

        self.board = Board(self.amount_of_positions,
                           self.amount_of_colors, self.can_have_double_colors)
