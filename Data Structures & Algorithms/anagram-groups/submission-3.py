class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:
            joined = ''.join(sorted(word))
            if joined in d:
                d[joined].append(word)
            else:
                d[joined] = [word]
        
        fArray = []
        for k, v in d.items():
            fArray.append(v)

        return fArray