from typing import List
from unittest import TestCase

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_len = len(nums)
        sum_r = sum(nums[1:nums_len])
        sum_l = 0
        for i in range(nums_len):
            if sum_l == sum_r:
                return i
            sum_l += nums[i]
            if i+1 < nums_len:
                sum_r -= nums[i+1]
        return -1


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 7, 3, 6, 5, 6]
        self.assertTrue(self.solution.pivotIndex(nums) == 3)

    def test_2(self):
        nums = [1, 2, 3]
        self.assertTrue(self.solution.pivotIndex(nums) == -1)

    def test_3(self):
        nums = [2, 1, -1]
        self.assertTrue(self.solution.pivotIndex(nums) == 0)

    def test_4(self):
        nums = [-1, -1, 0, 1, 1, 0]
        self.assertTrue(self.solution.pivotIndex(nums) == 5)
