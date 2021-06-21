from random import randint, sample
from datetime import datetime

from model.color import Color
from model.correct import Correct
from model.guess import Guess


class Game:
    def __init__(self, nickname: str, amount_of_guesses: int = 10, amount_of_positions: int = 4,
                 amount_of_colors: int = 6,
                 can_have_double_colors: bool = False) -> None:

        if not 0 < amount_of_guesses:
            raise ValueError("amount_of_guesses cannot be less then 1")

        if not 0 < amount_of_colors <= 12:
            raise ValueError("amount_of_colors must be between 1 and 12")

        if not 0 < amount_of_positions <= amount_of_colors:
            raise ValueError(
                "amount_of_positions must be between 1 and the amount of colors")

        self.nickname = nickname
        self.amount_of_guesses = amount_of_guesses
        self.amount_of_colors = amount_of_colors
        self.amount_of_positions = amount_of_positions
        self.can_have_double_colors = can_have_double_colors

        self.guesses: list = []
        self.cheated = False
        self.started = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        if can_have_double_colors:
            self.correct_guess = Guess(
                tuple(Color(randint(0, self.amount_of_colors)) for _ in range(self.amount_of_positions)))
        else:
            self.correct_guess = Guess(
                tuple(Color(n) for n in sample(range(self.amount_of_colors), self.amount_of_positions)))

    def add_guess(self, guess: Guess) -> None:
        correct = []
        checked = []

        for g, gc in zip(guess, self.correct_guess):
            if checked.count(g) >= self.correct_guess.count(g):
                correct.append(Correct.INCORRECT)
            elif g == gc:
                correct.append(Correct.CORRECT)
            elif g in self.correct_guess:
                correct.append(Correct.INCORRECT_PLACE)
            else:
                correct.append(Correct.INCORRECT)

            checked.append(g)

        self.guesses.append((guess, sorted(correct)))

    def has_won(self) -> bool:
        return [Correct.CORRECT for _ in range(self.amount_of_positions)] in [result for _, result in self.guesses]

    def has_lost(self) -> bool:
        return (not self.has_won()) and len(self.guesses) >= self.amount_of_guesses
