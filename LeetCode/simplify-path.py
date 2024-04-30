class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        
        stack = []
        for i in tokens:
            if i == "" or i == ".":
                continue
            if i == "..":
                if len(stack) > 0:
                    stack.pop()     
            else:
                stack.append(i)
            
                
        return "/" + "/".join(stack)
