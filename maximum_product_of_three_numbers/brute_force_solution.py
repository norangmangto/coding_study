class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]*nums[1]*nums[2]

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if max_val < nums[i]*nums[j]*nums[k]:
                        max_val = nums[i]*nums[j]*nums[k]

        return max_val
