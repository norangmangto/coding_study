class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        exp_vals = {}

        for idx, val in enumerate(nums):
            if val in exp_vals:
                return [exp_vals[val], idx]
            else:
                exp_vals[target-val] = idx
