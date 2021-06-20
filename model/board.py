from model.color import Color
from model.guess import Guess
from random import randint, sample


class Board:
    def __init__(self, amount_of_positions: int = 4, amount_of_colors: int = 6, can_have_double_colors: bool = False) -> None:
        self.guesses: list = []
        if can_have_double_colors:
            self.correct_guess = Guess(
                [Color(randint(0, amount_of_colors))
                 for _ in range(amount_of_positions)]
            )
        else:
            self.correct_guess = Guess(
                [Color(n)
                 for n in sample(range(amount_of_colors), amount_of_positions)]
            )

        self.correct_guess = Guess([Color(2), Color(2), Color(1), Color(4)])

        self.add_guess(Guess([Color(n) for n in range(1, 5)]))
        self.add_guess(Guess([Color(n) for n in range(1, 5)]))

    def add_guess(self, guess: Guess) -> None:
        # if guess == self.correct_guess:
        #     self.guesses.append((guess, True))
        #     return

        self.guesses.append(
            (guess, sorted(
                (
                    [c in self.correct_guess for c in guess],
                    [g == gc for g, gc in zip(guess, self.correct_guess)]
                ),
            ))
        )
