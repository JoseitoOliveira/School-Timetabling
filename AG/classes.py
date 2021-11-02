from copy import copy, deepcopy
import numpy as np
import json

import ujson


class Fitness:
    def __init__(self) -> None:
        self.values = ()

    @property
    def valid(self):
        """Assess if a fitness is valid or not."""
        return len(self.values) != 0

    def __hash__(self):
        return hash(self.values)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.values <= other.values

    def __lt__(self, other):
        return self.values < other.values

    def __eq__(self, other):
        return self.values == other.values

    def __ne__(self, other):
        return not self.__eq__(other)

    def __delattr__(self, name: str) -> None:
        if name == 'values':
            self.values = ()
        else:
            del self.__dict__[name]

    def __deepcopy__(self, memo):
        """Replace the basic deepcopy function with a faster one.

        It assumes that the elements in the :attr:`values` tuple are
        immutable and the fitness does not contain any other object
        than :attr:`values` and :attr:`weights`.
        """
        copy_ = self.__class__()
        copy_.values = self.values
        return copy_

    def __str__(self):
        """Return the values of the Fitness object."""
        return str(self.values if self.valid else tuple())

    def __repr__(self):
        """Return the Python code to build a copy of the object."""
        return "%s.%s(%r)" % (self.__module__, self.__class__.__name__,
                              self.values if self.valid else tuple())


class Individual():

    def __init__(self, genes: np.ndarray):
        self.genes = genes
        self.fitness = Fitness()

    def __getitem__(self, key):
        return self.genes[key]

    def __setitem__(self, key, value):
        self.genes[key] = value
    
    def __repr__(self) -> str:
        return f"Individual({self.genes})"

    def __iter__(self):
        return self.genes.__iter__()
