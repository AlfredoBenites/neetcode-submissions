class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                return min(ans, nums[left])
            
            middle = (right + left) // 2
            ans = min(ans, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return ans