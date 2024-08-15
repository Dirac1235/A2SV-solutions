class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        count = collections.Counter(s)
        print(count)     
        for i in range(len(s)):
            if stack:
                if s[i] not in stack and stack[-1] < s[i]:
                    stack.append(s[i])
                    count[s[i]] -= 1

                elif s[i] not in stack and stack[-1] >= s[i]:
                    while stack and stack[-1] >= s[i] and count[stack[-1]] > 0:
                        stack.pop()
                    stack.append(s[i])
                    count[s[i]] -= 1
                else:
                    count[s[i]] -= 1

            else:
                stack.append(s[i])
                count[s[i]] -= 1


        return "".join(stack)
        
