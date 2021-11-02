import numpy as np
from deap import base


class Problem(base.Fitness):
    def __init__(self, weights):
        self.weights = weights
        super().__init__()


class Individual(np.ndarray):
    def __init__(self, fitness) -> None:
        self.fitness = fitness
        super().__init__()
