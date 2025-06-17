class Solution:
    def reverseVowels(self, s: str) -> str:
        l = ['A', 'E', 'I', 'O', "U", 'a', 'e', 'i', 'o', 'u']
        s = list(s)
        left = 0
        right = len(s)-1

        while left<right:
            if s[left] not in l:
                left+=1
            elif s[right] not in l:
                right-=1
            else:
                s[left], s[right] = s[right], s[left]
                left+=1
                right-=1

        s = ''.join(s)
        return s