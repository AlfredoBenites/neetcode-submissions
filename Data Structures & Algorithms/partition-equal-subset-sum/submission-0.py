class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = {0}
        target = sum(nums) // 2
        for i in range(len(nums)):
            temp_dp = set()

            for num in dp:
                if (num + nums[i]) == target:
                    return True
                temp_dp.add(num + nums[i])
                temp_dp.add(num)

            dp = temp_dp

        return True if target in dp else False 