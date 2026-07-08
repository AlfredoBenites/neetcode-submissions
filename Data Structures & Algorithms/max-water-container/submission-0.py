class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l, r = 0, len(heights)-1
        temp = 0
        newl, newr = 0, 0

        while l < r:
            if heights[l] > heights[r]:
                temp = heights[r]
            else:
                temp = heights[l]
            if (r-l)*temp > maxi:
                maxi = (r-l)*temp
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maxi
            