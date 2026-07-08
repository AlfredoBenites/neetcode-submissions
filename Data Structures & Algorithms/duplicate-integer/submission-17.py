class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set
        # if i already in set return true

        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False