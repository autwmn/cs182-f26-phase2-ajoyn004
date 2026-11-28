# input: str
import sys

VOWELS = "aeiouAEIOU"


def main(argv):
    if len(argv) != 2:
        return -1
    word = argv[1]
    vowels = 0
    for c in word:
        if c in VOWELS:
            vowels += 1
    if len(word) < 4:
        return vowels
    return len(word) // vowels


if __name__ == "__main__":
    main(sys.argv)
