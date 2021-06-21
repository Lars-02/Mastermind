class Player:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Player({self.name})"

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: object):
        return hasattr(other, 'name') and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
