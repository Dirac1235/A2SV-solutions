class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        prefixArr = []
        st = ""
        for lis in shifts:
            arr[lis[0]] += 1 if lis[2] == 1 else -1
            arr[lis[1] + 1] += -1 if lis[2] == 1 else 1
        for i in arr:
            if len(prefixArr) == 0:
                prefixArr.append(i)
            else:
                prefixArr.append(prefixArr[-1] + i)
        
        for i in range(len(prefixArr) - 1):
           st += chr((ord(s[i]) - 97 + prefixArr[i]) % 26 + 97)


        return st
