from decimal import Decimal
from fractions import Fraction

from justbases import Radices

import matplotlib.pyplot as plt

def main():
    ratio = Fraction(1024, 1000)

    exponents = range(0, 9)

    increases = [ratio ** exp - 1 for exp in exponents]

    percentages = [100 * x for x in increases]

    radices = [Radices.from_rational(x, 10, 2)[0] for x in percentages] 

    rationals = [x.as_rational() for x in radices] 

    percent_values = \
       [Decimal(x.numerator)/Decimal(x.denominator) for x in rationals]

    plt.xticks(exponents, ['B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'])
    plt.ylabel("Percent Increase: (SI - IEC)/IEC")
    plt.xlabel("Unit Size")
    plt.plot(exponents, percent_values) 

    plt.show()


if __name__ == "__main__":
    main()


    
