# input: ints
import sys


def median(values):
    ys = sorted(values)
    mid = len(ys) // 2
    if len(ys) % 2 == 1:
        return ys[mid]
    return (ys[mid] + ys[mid + 1]) // 2


def main(argv):
    xs = [int(a) for a in argv[1:]]
    if not xs:
        return -1
    m = median(xs)
    above = [x for x in xs if x > m]
    return len(above)


if __name__ == "__main__":
    main(sys.argv)
