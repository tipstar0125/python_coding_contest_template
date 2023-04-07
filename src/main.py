from __future__ import annotations

import array
import bisect
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
from typing import List, Optional

sys.setrecursionlimit(5 * 10**5)
INF = 10**20
MOD = 10**9 + 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.l1: List[Optional[int]] = []
        self.l2: List[Optional[int]] = []

    def solveList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = current = ListNode(0)
        prev = None
        while head:
            n = head.val
            head = head.next
            if prev is None or prev != n:
                prev = n
                current.next = current = ListNode(n)

        return dummy.next

    def solveTree(self, root: Optional[TreeNode]) -> bool:
        def check(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False

            return check(p.left, q.right) and check(p.right, q.left)

        if root is None:
            return True

        p = root.left
        q = root.right

        return check(p, q)

    def dfs1(self, root: Optional[TreeNode]) -> None:
        if root is None:
            self.l1.append(None)
            return
        self.l1.append(root.val)
        self.dfs1(root.left)
        self.dfs1(root.right)

    def dfs2(self, root: Optional[TreeNode]) -> None:
        if root is None:
            self.l2.append(None)
            return
        self.l2.append(root.val)
        self.dfs2(root.left)
        self.dfs2(root.right)

    def solve(self, columnNumber: int) -> str:

        d = defaultdict(int)
        ret = ""

        while columnNumber > 0:
            columnNumber -= 1
            num = columnNumber % 26
            ret = chr(num + ord("A")) + ret
            columnNumber = columnNumber // 26
        return ret


if __name__ == "__main__":

    solution = Solution()
    l1 = [1, 1, 2, 3, 3]
    head = current = ListNode(0)
    for x in l1:
        current.next = current = ListNode(x)
    list1 = head.next

    l2 = [1, 3, 4]
    head = current = ListNode(0)
    for x in l2:
        current.next = current = ListNode(x)
    list2 = head.next

    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(3)
    tree1.left.right = TreeNode(4)
    tree1.right = TreeNode(2)
    tree1.right.left = TreeNode(4)
    tree1.right.right = TreeNode(3)
    # tree2 = TreeNode(1)
    # tree2.left = TreeNode(2)
    # tree2.right = TreeNode(3)

    # ret = solution.solveList(list1)
    ret = solution.solve(52)
    # ret = solution.soveTree(tree1)
    print(ret)

    # while ret:
    #     print(ret.val)
    #     ret = ret.next
