class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 1 or n > 3*10000:
            raise ValueError("The list nums is shorter than 1 or longer than 3*10_000")

        if n < 3:
            return n

        curr = 1

        for i in range(2, n):
            if nums[curr] == nums[i]:
                if nums[curr] != nums[curr-1]:
                    curr += 1
                    nums[curr] = nums[i]
            else:
                curr = curr+1
                nums[curr] = nums[i]

        return curr+1

    def optimal_solution(self, nums: list[int]) -> int:
        c = 2

        for i in range(c, len(nums)):
            if nums[i] != nums[c-2]:
                nums[c] = nums[i]
                c += 1

        return c
