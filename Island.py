import numpy as np
from typing import Callable

class Island:
    l: float
    r: float
    s: float
    alpha: float
    theta: float
    num: int
    fun: Callable

    @classmethod
    def bind(cls, fun: Callable):
        cls.fun = fun

    def __init__(self, num: int, s5: float, s: float):
        r = np.sqrt(s / np.pi)
        r_0 = np.sqrt((s - s5) / np.pi)
        h = 5 * r / (r - r_0)
        l = np.sqrt(r ** 2 + h ** 2)
        alpha = np.arctan2(h, r)
        theta = 2 * np.pi * r / l
        self.l = l
        self.r = r
        self.alpha = alpha
        self.theta = theta
        self.num = num
        self.s = s

    def deltaS(self, t):
        dH = Island.fun(t) - Island.fun(0)
        dL = dH / np.cos(self.alpha)
        return .5 * self.theta * dL * (self.l * 2 - dL)

    def delta2S(self, t):
        if t < 1:
            raise Exception("t should >= 1")
        return self.deltaS(t) - self.deltaS(t - 1)

    def deltaN(self, t):
        return self.delta2S(t) / self.s * self.num
