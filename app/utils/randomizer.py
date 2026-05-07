import random


class SeededRandom:
    """
    Wrapper around Python random for reproducible simulations.
    """

    def __init__(self, seed: int):
        self._random = random.Random(seed)

    def probability(self) -> float:
        """
        Returns float between 0 and 1.
        """
        return self._random.random()

    def choice(self, items):
        """
        Select random item from list.
        """
        return self._random.choice(items)