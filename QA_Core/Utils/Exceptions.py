class InvalidDateRepresentation(Exception):
    """ Raised when a date cannot be constructed """

    def __init__(self, message=""):
        super().__init__(message)


class NullDerivative(Exception):
    """ Raised when the derivative is equal to 0"""

    def __init__(self, message=""):
        super().__init__(message)


class ConvergenceNotSatisfied(Warning):
    """ Raised when the convergence is not satisfied"""

    def __int__(self, message=""):
        super().__init__(message)
