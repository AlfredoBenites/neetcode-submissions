class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        s = set()

        for n in nums:
            s.add(n)

        for n in s:
            counter = 1
            while n-1 in s:
                n = n-1
            while n+1 in s:
                counter += 1
                n = n+1
            longest_sequence = max(longest_sequence, counter)

        return longest_sequence
            