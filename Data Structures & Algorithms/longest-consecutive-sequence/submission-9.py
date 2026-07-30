class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        s = set(nums)

        for n in s:
            counter = 1
            curr = n
            if curr-1 not in s:
                while curr+1 in s:
                    counter += 1
                    curr = curr+1
                longest_sequence = max(longest_sequence, counter)

        return longest_sequence
            