class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}

        t_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for x in t:
            if x in t_dict:
                t_dict[x] += 1
            else:
                t_dict[x] = 1

        for key, values in s_dict.items():
            if key in t_dict:
                if values != t_dict[key]:
                    return False
            else:
                return False

        for key, values in t_dict.items():
            if key in s_dict:
                if values != s_dict[key]:
                    return False
            else:
                return False
        
        return True
                