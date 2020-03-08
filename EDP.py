import numpy as np

class EDP:
    pr: np.ndarray
    ih: np.ndarray
    wage: np.ndarray
    GINI: np.ndarray
    Disc: np.ndarray

    @classmethod
    def init(cls, pr, ih, wage):
        cls.pr = pr
        cls.ih = ih
        cls.wage = wage

    def __init__(self, religion):
        self.religion = religion

    def select(self):
        p = EDP.pr.dot(EDP.ih)
        return np.argmax(p)

    def deltaWage(self, deltaN):
        return deltaN * EDP.wage

    def pres(self):
        return .5 * (EDP.GINI + EDP.Disc)
