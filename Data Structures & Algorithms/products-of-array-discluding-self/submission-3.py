class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        temp = 0
        for i in range(len(nums)):
            temp = nums[i]
            for k in range(len(nums)):
                if i != k:
                    product *= nums[k]
            res.append(product)
            product = 1
        return res