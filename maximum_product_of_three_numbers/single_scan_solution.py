class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        min1 = min2 = sys.maxsize
        max1 = max2 = max3 = -1*sys.maxsize-1

        for i in nums:
            if i <= min1:
                min2, min1 = min1, i
            elif i < min2: min2 = i

            if i >= max1:
                max3, max2, max1 = max2, max1, i
            elif i >= max2:
                max3, max2 = max2, i
            elif i > max3: max3 = i

        return max(min1*min2*max1, max1*max2*max3)
