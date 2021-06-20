from random import randint, sample

from model.color import Color
from model.guess import Guess


class Game:
    def __init__(self, amount_of_guesses, amount_of_positions, amount_of_colors, can_have_double_colors):
        self.amount_of_guesses = max(1, amount_of_guesses)
        self.amount_of_colors = max(1, min(amount_of_colors, 12))
        self.amount_of_positions = max(1, min(amount_of_colors, amount_of_positions))
        self.can_have_double_colors = can_have_double_colors
        self.guesses: list = []

        if can_have_double_colors:
            self.correct_guess = Guess(
                tuple(Color(randint(0, self.amount_of_colors)) for _ in range(self.amount_of_positions)))
        else:
            self.correct_guess = Guess(
                tuple(Color(n) for n in sample(range(self.amount_of_colors), self.amount_of_positions)))

        print(self.correct_guess)

    def add_guess(self, guess: Guess) -> None:
        # if guess == self.correct_guess:
        #     self.guesses.append((guess, True))
        #     return

        self.guesses.append((guess, sorted(
            (
                [c in self.correct_guess for c in guess],
                [g == gc for g, gc in zip(guess, self.correct_guess)]
            ),
        ))
                            )
