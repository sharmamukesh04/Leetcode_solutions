class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_s = {}
        dict_t = {}

        for x, y in zip(s, t):
            if x in dict_s:
                if dict_s[x]!=y:
                    return False
            else:
                dict_s[x]=y
            
            if y in dict_t:
                if dict_t[y]!=x:
                    return False
            else:
                dict_t[y]=x
        
        return True