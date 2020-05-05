# Uses python3
import sys


def get_majority_element(a, left, right):
    if left + 1 == right:
        return [[a[left]], []]
    mid = int(left+(right-left)/2)
    left_half = get_majority_element(a, left, mid)
    right_half = get_majority_element(a, mid, right)

    return count_merge(left_half, right_half)


def similar(left_half, right_half):
    not_similar = []
    for ele in right_half:
        if left_half[0] == ele:
            left_half.append(ele)
        else:
            not_similar.append(ele)
    return [left_half, not_similar]


def count_merge(left_half, right_half):
    [left_majors, right_others] = similar(left_half[0], right_half[1])
    [right_majors, left_others] = similar(right_half[0], left_half[1])
    if left_majors[0] == right_majors[0]:
        return [left_majors + right_majors, left_others + right_others]
    elif len(left_majors) > len(right_majors):
        return [left_majors, right_majors + left_others + right_others]
    else:
        return [right_majors, left_majors + right_others + left_others]


n = int(input())
a = list(map(int, input().strip().split()))[:n]
x = get_majority_element(a, 0, n)

if len(x[0]) > n/2:
    print(1)
else:
    print(0)
