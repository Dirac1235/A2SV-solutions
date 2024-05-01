class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spp = 0
        lis = []
        for i in range(len(s)):
            if spp < len(spaces) and i == spaces[spp] :
                lis.append(" ")
                spp += 1
            lis.append(s[i])
        return "".join(lis)
