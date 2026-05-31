class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left, right):
            while left >=0 and right < len(s):
                if s[left] != s[right]:
                    return s[left+1:right]
                left-=1
                right+=1

            return  s[left+1: right]

        n = len(s)
        res = ""
        for i in range(n):
            res1 = expand(i, i)
            res2 = expand(i, i+1)

            if len(res1) > len(res):
                res = res1

            if len(res2) > len(res):
                res = res2
        return res


