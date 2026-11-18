class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(num):
            iterations = 0

            for pile in piles:
                iterations += (pile + num - 1) // num

            return h >= iterations 
        
        left, right = 1, max(piles)
        ans = float('inf')

        while left <= right:
            middle = (left + right) // 2

            if can(middle):
                right = middle - 1
                ans = min(ans, middle)
            else:
                left = middle + 1
        
        return ans
            