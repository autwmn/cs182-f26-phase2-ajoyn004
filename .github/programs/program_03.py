# input: str
import sys

PREREQS = {}
PREREQS["CS601"] = None
PREREQS["CS602"] = "CS601"
PREREQS["CS610"] = "CS601"
PREREQS["CS620"] = "CS610"
PREREQS["CS630"] = "CS620"


def course_number(code):
    if len(code) < 5:
        return 0
    if code[0] != "C":
        return 0
    if code[1] != "S":
        return 0
    if not code[2].isdigit():
        return 0
    if not code[3].isdigit():
        return 0
    if not code[4].isdigit():
        return 0
    return int(code[2:5])


def main(argv):
    if len(argv) != 2:
        return -1
    code = argv[1]
    number = course_number(code)
    if number < 100:
        return number
    chain = [code]
    while PREREQS[chain[-1]] is not None:
        chain.append(PREREQS[chain[-1]])
    return len(chain)


if __name__ == "__main__":
    main(sys.argv)
