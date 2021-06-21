from model.color import Color
from typing import Generator


class Guess:
    def __init__(self, colors: tuple) -> None:
        self.colors = colors

    def count(self, color: Color):
        return self.colors.count(color)

    def __eq__(self, o: object) -> bool:
        return self.colors == o.colors

    def __iter__(self) -> Generator:
        for c in self.colors:
            yield c

    def __contains__(self, n: int) -> bool:
        return n in self.colors

    def __repr__(self) -> str:
        return f"Guess({ [str(c) for c in self] })".replace("'", "")

    def __str__(self) -> str:
        return repr(self)

    def __hash__(self) -> int:
        return hash(str(self))
