import math


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


# Calculate pi using Srinivasa Ramanujan's formula
def estimate_pi():
    total = 0
    k = 0
    fact = 2*math.sqrt(2)/9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)      # the numerator in the second fraction
        den = factorial(k)**4 * 396**(4*k)           # the denominator in the second fraction
        term = fact * num / den
        total = total + term

        if abs(term) < 1e-15:                        # calculate until the summation of term is smaller than 1e-15
            break
        k = k + 1
    return 1 / total


# Calculate pi using math.pi
def check_pi():
    return math.pi


if __name__ == '__main__':
    print("Calculate pi using Srinivasa Ramanujan's formula:", estimate_pi())
    print("Calculate pi using math.pi:", check_pi())
