# input: str
import sys

LABELS = ["weak", "fair", "strong"]


def char_classes(pw):
    classes = 0
    if any(c.isupper() for c in pw):
        classes += 1
    if any(c.islower() for c in pw):
        classes += 1
    if any(c.isdigit() for c in pw):
        classes += 1
    return classes


def strength(pw):
    score = char_classes(pw)
    if len(pw) >= 8:
        score += 1
    if len(pw) >= 10:
        score += 1
    if len(pw) >= 12:
        score += 1
    return score


def main(argv):
    if len(argv) != 2:
        return -1
    pw = argv[1]
    score = strength(pw)
    return LABELS[score // 2]


if __name__ == "__main__":
    main(sys.argv)
