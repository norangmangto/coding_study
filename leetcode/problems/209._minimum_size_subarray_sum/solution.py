class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        lo = hi = 0
        cur_sum = nums[0]
        min_len = n+1

        while lo <= hi and hi < n:
            if cur_sum >= target:
                min_len = min(min_len, hi-lo+1)
                cur_sum -= nums[lo]
                lo += 1
            else:
                if (hi := hi+1) < n:
                    cur_sum += nums[hi]

        return 0 if min_len == n+1 else min_len
