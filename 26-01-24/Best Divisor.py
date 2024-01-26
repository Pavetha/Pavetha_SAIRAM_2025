'''Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints

Output Format

Print an integer denoting the best divisor of .

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (which, having only one digit, sums to itself). Thus, we print  as our answer.'''

PROGRAM CODE:

import math
import os
import random
import re
import sys
def d(num):
    return sum(int(i) for i in str(num))

def b(n):
    best_divisor = 1
    max_sum = 1
    
    for j in range(2, n + 1):
        if n % j == 0:
            c = d(j)
            if c > max_sum or (c == max_sum and j < best_divisor):
                max_sum = c
                best_divisor = j

    return best_divisor



if __name__ == '__main__':
    n = int(input().strip())
    result = b(n)
    print(result)
