import numpy as np
from QA_Core.Utils.Exceptions import *


def first_order_derivative(f, *args, j=0, diff_method='forward', h=1e-4) -> float:
    x = np.asarray(args)
    x_fwd_j = x + (h * np.eye(1, len(args), j)).flatten()
    x_bwd_j = x - (h * np.eye(1, len(args), j)).flatten()
    x_fwd2_j = x + (2 * h * np.eye(1, len(args), j)).flatten()
    x_bwd2_j = x - (2 * h * np.eye(1, len(args), j)).flatten()

    if diff_method == 'forward':
        return (f(*x_fwd_j.flatten()) - f(*args)) / h
    elif diff_method == 'backward':
        return (f(*args) - f(*x_bwd_j.flatten())) / h
    elif diff_method == 'central':
        # Richardson's approximation when h is too small
        return (-f(*x_fwd2_j.flatten()) + 8 * f(*x_fwd_j.flatten()) -
                8 * f(*x_bwd_j.flatten()) + f(*x_bwd2_j.flatten())) / 12 * h
    else:
        raise NullDerivative(f"{diff_method} is not 'forward', 'backward', or 'central'")
