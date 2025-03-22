class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True

        last_index = len(nums) - 1
        max_reachable_idx = nums[0]
        i = 1

        while i <= max_reachable_idx and max_reachable_idx < last_index:
            if nums[i] + i > max_reachable_idx:
                max_reachable_idx = nums[i] + i

            i += 1

        return True if max_reachable_idx >= last_index else False

    def other_solution(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False
