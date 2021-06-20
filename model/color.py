class Color:
    def __init__(self, n: int) -> None:
        if n < 0 or n > 11:
            raise ValueError("Color number too high or low")
        self.n = n

    def __eq__(self, o: object) -> bool:
        return self.n == o.n

    def __repr__(self) -> str:
        return f"Color({ self.n })"

    def __str__(self) -> str:
        if self.n == 0:
            return "red"
        elif self.n == 1:
            return "green"
        elif self.n == 2:
            return "blue"
        elif self.n == 3:
            return "yellow"
        elif self.n == 4:
            return "brown"
        elif self.n == 5:
            return "orange"
        elif self.n == 6:
            return "black"
        elif self.n == 7:
            return "white"
        elif self.n == 8:
            return "pink"
        elif self.n == 9:
            return "aqua"
        elif self.n == 10:
            return "burlywood"
        elif self.n == 11:
            return "purple"
