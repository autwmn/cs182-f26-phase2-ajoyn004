# input: int
import sys


def digits_of(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def main(argv):
    if len(argv) != 2:
        return -1
    n = abs(int(argv[1]))
    digits = digits_of(n)
    if len(digits) < 3:
        return sum(digits)
    evens = [d for d in digits if d % 2 == 0]
    return sum(evens) // len(evens)


if __name__ == "__main__":
    main(sys.argv)
