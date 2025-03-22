class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()

        for i, v in enumerate(citations):
            if v >= n-i:
                return n-i

        return 0
