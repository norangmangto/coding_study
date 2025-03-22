class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        jump_map = {}

        def _update_jump_map(start: int, end: int, jumps: int) -> None:
            for i in range(start, end+1):
                jump_map[i] = jumps

        max_reachable_idx = nums[0]
        _update_jump_map(1, max_reachable_idx, 1)

        for i in range(1, len(nums)):
            if i+nums[i] > max_reachable_idx:
                _update_jump_map(max_reachable_idx+1, i+nums[i], jump_map[i]+1)
                max_reachable_idx = i+nums[i]

        return jump_map[len(nums)-1]

    def optimal_solution(self, nums: list[int]) -> int:
        jumps = current_jump_end = farthest = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])

            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest

        return jumps
