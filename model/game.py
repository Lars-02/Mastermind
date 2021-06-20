from model.correct import Correct
from random import randint, sample

from model.color import Color
from model.guess import Guess


class Game:
    def __init__(self, name: str, amount_of_guesses: int = 10, amount_of_positions: int = 4, amount_of_colors: int = 6, can_have_double_colors: bool = False) -> None:
        self.name = name

        if not 0 < amount_of_guesses:
            raise ValueError("amount_of_guesses cannot be less then 1")

        if not 0 < amount_of_colors <= 12:
            raise ValueError("amount_of_colors must be between 1 and 12")

        if not 0 < amount_of_positions <= amount_of_colors:
            raise ValueError(
                "amount_of_positions must be between 1 and the amount of colors")

        self.amount_of_guesses = amount_of_guesses
        self.amount_of_colors = amount_of_colors
        self.amount_of_positions = amount_of_positions
        self.can_have_double_colors = can_have_double_colors
        self.guesses: list = []

        if can_have_double_colors:
            self.correct_guess = Guess(
                tuple(Color(randint(0, self.amount_of_colors)) for _ in range(self.amount_of_positions)))
        else:
            self.correct_guess = Guess(
                tuple(Color(n) for n in sample(range(self.amount_of_colors), self.amount_of_positions)))

        self.correct_guess = Guess([Color(2), Color(1), Color(3), Color(3)])
        self.add_guess(Guess([Color(n) for n in range(1, 5)]))
        self.add_guess(Guess([Color(n) for n in range(1, 5)]))
        print(self.correct_guess)

    def add_guess(self, guess: Guess) -> None:
        # if guess == self.correct_guess:
        #     self.guesses.append((guess, True))
        #     return

        self.guesses.append((guess, sorted([Correct.CORRECT if g == gc else Correct.INCORRECT_PLACE if g in self.correct_guess else Correct.INCORRECT for g,
                                            gc in zip(guess, self.correct_guess)])))
