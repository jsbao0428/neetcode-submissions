class Solution:
    def encode(self, strs: List[str]) -> str:
        # 把 List[str] 包裝成一個字串
        res = ""
        for string in strs:
            length = len(string)
            res = res + f"{length}#{string}"
        return res


    def decode(self, s: str) -> List[str]:
        # 把字串還原成 List[str]
        res = []
        n = len(s)

        length = 0
        i=0
        while i < n:
            while s[i] != "#":
                length = length*10 + int(s[i])
                i+=1
            i+=1
            string = ""
            for _ in range(length):
                string+=s[i]
                i+=1

            res.append(string)
            length = 0

        return res