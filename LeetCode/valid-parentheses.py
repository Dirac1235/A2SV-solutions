class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        dic = {'{':'}', '(':')', '[':']'}
        for i in s:
            if i in dic:
                mystack.append(i)
            else:
                if mystack:
                    if mystack[-1] in dic and dic[mystack[-1]] == i:
                        mystack.pop()
                    else:
                        mystack.append(i)
                else:
                    mystack.append(i)
        return len(mystack) == 0
