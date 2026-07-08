class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        for values in my_dict.values():
            if values != 1:
                return True

        return False