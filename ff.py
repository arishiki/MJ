# ff stands for "fundamental functions"

import math

def nCm(n, m):
    dividee = 1
    for x in range(n, n-m, -1):
        dividee *= x
    return dividee//math.factorial(m)
