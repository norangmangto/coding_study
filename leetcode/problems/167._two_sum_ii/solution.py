class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        head, tail = 0, len(numbers)-1

        while head < tail:
            while numbers[head] + numbers[tail] > target:
                tail -= 1

            # numbers[head] + numbers[tail] is either bigger than the target
            # or equal to the target
            if numbers[head] + numbers[tail] == target:
                return [head+1, tail+1]
            else:
                head += 1

        return []  # error case

    def simpler_solution(self, numbers: list[int], target: int) -> list[int]:
        head, tail = 0, len(numbers)-1

        while head < tail:
            if numbers[head] + numbers[tail] == target:
                return [head+1, tail+1]
            elif numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1

        return []
