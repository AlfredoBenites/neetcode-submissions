class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use a dictionary where the key is the index and the value is the value of index
        # do diff = target - value
        # if diff in dictionary return that index and then current index
        # if not in dictionary then add value to dictionary

        d = {}

        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in d:
                return [d[diff], index]
            d[nums[index]] = index
