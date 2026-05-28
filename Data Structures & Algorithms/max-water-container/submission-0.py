class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        if len(heights) < 2:
            return maxArea

        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                area = min(heights[i], heights[j]) * (j-i)
                maxArea = max(maxArea, area)

        return maxArea


        