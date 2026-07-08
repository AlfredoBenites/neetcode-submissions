class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if same size
        # use sorted and .join and then compare

        if len(s) != len(t):
            return False

        word1 = ''.join(sorted(s))
        word2 = ''.join(sorted(t))

        if word1 == word2:
            return True
        
        return False