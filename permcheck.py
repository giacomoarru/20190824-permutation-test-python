# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

'''
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

is a permutation, but array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

is not a permutation, because value 2 is missing.
The goal is to check whether array A is a permutation.

Write a function:

    def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2

the function should return 1.

Given array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3

the function should return 0.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [1..1,000,000,000].
'''

def solution(A):
    A.sort()
    if A[0] != 1:
        return 0

    Alen = len(A)-1
    serieSum = int(((A[Alen])*(A[Alen] +1))/2)
    currentSum = 1

    for i in range(2, Alen+2):
        if i != A[i-1]:
            return 0
        else:
            currentSum += i

    if serieSum == currentSum:
        return 1
    else:
        return 0

    pass

array = [1,2,3,4,5]
print(solution(array))