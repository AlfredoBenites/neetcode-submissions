class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [-4, -1, -1, 0, 1, 2]
        '''
        nums.sort()
        curr, l, r = 0, 1, len(nums)-1
        res = []

        while l < r:
            target = nums[curr] * -1
            left = l
            right = r
            while left < right:
                if nums[left] + nums[right] == target:
                    if [nums[curr], nums[left], nums[right]] not in res:
                        res.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            curr += 1
            l += 1

        return res
