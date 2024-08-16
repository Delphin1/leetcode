from typing import List
from unittest import TestCase

class Solution:

    def someMethod(self):
        pass




class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.someMethod)

