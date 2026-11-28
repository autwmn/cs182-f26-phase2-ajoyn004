# input: int
import sys

COMBINATION = [7, 3, 9, 1]


def main(argv):
    if len(argv) != 2:
        return -1
    n = int(argv[1])
    if n < 1000 or n > 9999:
        return -2
    dials = [int(d) for d in str(n)]
    if dials[0] != COMBINATION[0]:
        return 0
    if dials[1] != COMBINATION[1]:
        return 1
    if dials[2] != COMBINATION[2]:
        return 2
    if dials[3] != COMBINATION[3]:
        return 3
    raise RuntimeError("safe unlocked")


if __name__ == "__main__":
    main(sys.argv)
