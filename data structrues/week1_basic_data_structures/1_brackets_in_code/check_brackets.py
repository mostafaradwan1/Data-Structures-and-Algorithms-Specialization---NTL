# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            top = opening_brackets_stack.pop(-1)
            if (not are_matching(top, next)):
                return i+1

    if len(opening_brackets_stack) == 0:
        return "Success"
    if len(opening_brackets_stack) == 1 and next == opening_brackets_stack[-1]:
        return i+1
    return text.find(top)+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
