# Horner's method


def Horner(x,*args):
    # Implement's horner's method for a given polynomial of coefficients *args in x.
    result = 0
    for coeff in args:
        result = result*x +coeff
    return result

