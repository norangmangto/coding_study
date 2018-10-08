class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_area = 0
        i = 0
        j = n-1
        while i != j:
            area = (j-i) * min(height[i], height[j])
            if area > max_area: max_area = area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area

    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def calc_area(i, ai, j, aj):
            """
            :type i: int
            :type ai: int
            :type j: int
            :type aj: int
            :rtype: int
            """
            return min(ai, aj) * abs(j-i)

        n = len(height)
        max_container_size = 0

        for i in range(n-1):
            for j in range(i+1, n):
                area = calc_area(i, height[i], j, height[j])
                if area > max_container_size:
                    max_container_size = area

        return max_container_size
