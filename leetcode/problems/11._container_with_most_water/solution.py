class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_amount, left, right = 0, 0, len(height)-1

        while left < right:
            max_amount = max(max_amount, (right-left)*min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount

    def optimal_solution(self, height: list[int]) -> int:
        max_amount, left, right = 0, 0, len(height)-1
        max_height = max(height)

        while left < right:
            if (right-left)*max_height < max_amount:
                break

            max_amount = max(max_amount, (right-left)*min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_amount
