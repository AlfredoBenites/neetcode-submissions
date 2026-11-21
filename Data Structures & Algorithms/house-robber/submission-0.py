class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for house in nums:
            curr_max = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = curr_max

        return rob2