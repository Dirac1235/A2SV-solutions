class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        leng = len(p)
        i = 0
        lis = []
        sor = sorted(p)
        while i + leng <= len(s):
            if sorted(s[i: i + leng]) == sor:
                lis.append(i)
            i += 1
        return lis
