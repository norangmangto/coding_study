class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))

        return len(nums)

    def other_solution(self, nums: list[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
