from QA_Core.Utils.DerivativesUtils import *


class NewtonRaphsonOneDim:
    def __init__(self, func, x0: float, tol=1e-6, max_iter=1000):
        self.func = func
        self.x0 = x0
        self.tol = tol
        self.max_iter = max_iter

    def newton_raphson(self, diff_method: str) -> float:

        x = self.x0
        iter = 0
        while iter < self.max_iter:
            if abs(self.func(x)) < self.tol or self.func(x) == 0.0:
                return x
            x = x - self.func(x) / first_order_derivative(self.func, x, diff_method=diff_method)
            iter += 1
        raise ConvergenceNotSatisfied("Max iteration reached.")
        return x

