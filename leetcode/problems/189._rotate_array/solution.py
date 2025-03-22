class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        for _ in range(k):
            nums.insert(0, nums.pop(-1))

    def optimal_solution1(self, nums: list[int], k: int) -> None:
        # n = len(nums)
        # k = k % n
        # if k != 0:
        #     nums[:k], nums[k:] = nums[-k:], nums[:-k]

        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

    def other_solution(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = []
        i = (n - k) % n

        for _ in range(n):
            rotated.append(nums[i])
            i += 1
            i %= n

        for i in range(n):
            nums[i] = rotated[i]
