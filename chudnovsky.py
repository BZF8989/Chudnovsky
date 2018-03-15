"""

Chudnovsky's Algorithm to calculate pi!

Created by Bill on March 14, 2018

"""

from decimal import *


NUMERATOR_CONSTANT = 426880 * Decimal(10005).sqrt()

SUM_NUMERATOR_CONSTANT_1 = 6
SUM_NUMERATOR_CONSTANT_2 = 545140134
SUM_NUMERATOR_CONSTANT_3 = 13591409

SUM_DENOMINATOR_CONSTANT_1 = 3
SUM_DENOMINATOR_CONSTANT_2 = -262537412640768000


def pi(precision=100, k_max=10):
    getcontext().prec = precision  # set precision of Decimal library
    """
    Start at SUM_NUMERATOR_CONSTANT_3 as the sum because
    that is the only term remaining when k == 0
    """
    sumation = SUM_NUMERATOR_CONSTANT_3
    for k in range(1, k_max):
        top = Decimal(factorial(SUM_NUMERATOR_CONSTANT_1 * k)) * \
              Decimal((SUM_NUMERATOR_CONSTANT_2 * k + SUM_NUMERATOR_CONSTANT_3))
        bottom = Decimal(factorial(SUM_DENOMINATOR_CONSTANT_1 * k)) * \
                 Decimal((factorial(k) ** SUM_DENOMINATOR_CONSTANT_1)) * \
                 Decimal((SUM_DENOMINATOR_CONSTANT_2 ** k))

        sumation += Decimal(top/bottom)

    pi_num = Decimal(NUMERATOR_CONSTANT) / Decimal(sumation)
    # print("The value of pi is: ", pi_num)  # DEBUGGING
    return pi_num


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
