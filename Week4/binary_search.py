# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, (len(a) - 1)
    return binary_search_real(a, left, right, x)


def binary_search_real(a, left, right, x):
    if right < left:
        return -1
    mid = int(left + (right - left) / 2)
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_real(a, mid + 1, right, x)
    else:
        return binary_search_real(a, left, mid-1, x)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
