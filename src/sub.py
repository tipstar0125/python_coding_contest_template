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
INF = 10**20
MOD = 10**9 + 7


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


def align_heap(A: list[int], start: int, end: int):
    k = start
    while True:
        if 2 * k + 2 < end:
            p = A[k]
            l = A[2 * k + 1]
            r = A[2 * k + 2]
            m = max(p, l, r)
            if m == p:
                break
            elif m == l:
                A[k], A[2 * k + 1] = A[2 * k + 1], A[k]
                k = 2 * k + 1
            else:
                A[k], A[2 * k + 2] = A[2 * k + 2], A[k]
                k = 2 * k + 2

        elif 2 * k + 1 < end:
            p = A[k]
            l = A[2 * k + 1]
            m = max(p, l)
            if m == p:
                break
            else:
                A[k], A[2 * k + 1] = A[2 * k + 1], A[k]
                k = 2 * k + 1
        else:
            break


def build_heap(A: list[int]):
    N = len(A)
    for x in range(N // 2 - 1, -1, -1):
        align_heap(A, x, N)


def heap_sort(A: list[int], M: int):
    build_heap(A)
    N = len(A)
    for i in range(N - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        align_heap(A, 0, i)
        if i == M:
            print(*A)
    print(*A)


# @lru_cache
# def f(x: int) -> int:
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     return f(x - 1) + f(x - 2)


def dfs(pos: int, G: list[list[int]], visited: list[bool], is_chosen: list[bool]):
    ok = True
    for nxt in G[pos]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, G, visited, is_chosen)
            ok &= not is_chosen[nxt]
    is_chosen[pos] = ok


def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return (0, 1, b)
    x, y, g = ext_gcd(b % a, a)
    return (y - b // a * x, x, g)


def solve():

    N, X = read_int_list()
    A = read_int_list()
    A.sort()

    for i in range(N):
        pos = bisect.bisect_left(A, X + A[i])
        if pos < N and A[pos] == X + A[i]:
            print("Yes")
            return
    print("No")


def main():
    solve()
    # t = read_int()
    # for _ in range(t):
    #     solve()


main()
