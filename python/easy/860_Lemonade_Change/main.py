from typing import List
from unittest import TestCase

class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:
        w = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            w[bill] += 1
            change = bill - 5
            if change > 0:
                if change == 5:
                    if w[change] > 0:
                        w[change] -= 1
                    else:
                        return False
                elif change == 15:
                    if (w[10] > 0) and (w[5] > 0):
                        w[10] -= 1
                        w[5] -= 1
                    elif w[5] > 2:
                        w[5] -= 3
                    else:
                        return False
            print(f"bill: {bill}, change: {change}, wallet: {w}")
        return True



class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_true(self):
        bills = [5, 5, 5, 10, 20]
        self.assertTrue(self.solution.lemonadeChange(bills))

    def test_false(self):
        bills = [5, 5, 10, 10, 20]
        self.assertFalse(self.solution.lemonadeChange(bills))

    def test_false2(self):
        bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
        self.assertFalse(self.solution.lemonadeChange(bills))
