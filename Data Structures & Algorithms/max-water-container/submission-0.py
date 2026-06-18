class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        
        while l < r:
            short = min(heights[l], heights[r])
            area = (r - l) * short
            if area > maxArea:
                maxArea = area
            if heights[r] < heights[l]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                l += 1
        
        return maxArea
            



