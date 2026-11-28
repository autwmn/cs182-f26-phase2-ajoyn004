# input: ints
import sys

DISTINCT_SIDES = {"equilateral": 1, "scalene": 3}


def classify(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"
    if a + b <= c or b + c <= a or a + c <= b:
        return "not a triangle"
    if a == b:
        if b == c:
            return "equilateral"
        return "isosceles"
    if b == c or a == c:
        return "isosceles"
    return "scalene"


def main(argv):
    xs = [int(a) for a in argv[1:]]
    if len(xs) != 3:
        return -1
    a, b, c = xs
    if a < 1 or a > 10:
        return -2
    if b < 1 or b > 10:
        return -3
    if c < 1 or c > 10:
        return -4
    kind = classify(a, b, c)
    if kind == "invalid" or kind == "not a triangle":
        return 0
    return DISTINCT_SIDES[kind]


if __name__ == "__main__":
    main(sys.argv)
