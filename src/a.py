from __future__ import annotations

import array
import bisect
import copy
import fractions
import heapq
import itertools
import math
import random
import re
import string
import sys
import time
from collections import defaultdict, deque
from functools import lru_cache

sys.setrecursionlimit(10**6)


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return list(input().split())


def read_str():
    return input()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    ok = True
    while i * i <= n:
        if n % i == 0:
            ok = False
        i += 1
    return ok


def eratosthenes(n: int) -> list[bool]:

    is_prime_list = ([False, True] * (n // 2 + 1))[0 : n + 1]
    is_prime_list[1] = False
    is_prime_list[2] = True
    for i in range(3, n + 1, 2):
        if not (is_prime_list[i]):
            continue
        if i * i > n:
            break
        for k in range(i * i, n + 1, i):
            is_prime_list[k] = False
    return is_prime_list


def legendre(n: int, p: int) -> int:
    cnt = 0
    pp = p
    while pp <= n:
        cnt += n // pp
        pp *= p

    return cnt


def prime_factorize(n: int) -> defaultdict[int, int]:
    nn = n
    i = 2
    d: defaultdict[int, int] = defaultdict(int)
    while i * i <= n:
        while nn % i == 0:
            d[i] += 1
            nn //= i
        i += 1
    if nn != 1:
        d[nn] += 1
    return d


def make_divisors(n: int) -> list[int]:
    i = 1
    ret = []
    while i * i <= n:
        if n % i == 0:
            ret.append(i)
            if i != n // i:
                ret.append(n // i)
        i += 1
    ret.sort()
    return ret


def gcd(a: int, b: int) -> int:

    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return (0, 1, b)
    x, y, g = ext_gcd(b % a, a)
    return (y - b // a * x, x, g)


def solve():
    N = read_int()
    print(N)


def main():
    t = read_int()
    for _ in range(t):
        solve()


main()
