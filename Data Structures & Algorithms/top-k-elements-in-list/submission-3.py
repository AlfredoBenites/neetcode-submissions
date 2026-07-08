class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        a = sorted(d, key=lambda x: d[x])

        r = []
        i = len(a)-1
        while k != 0:
            r.append(a[i])
            k -= 1
            i -= 1

        return r