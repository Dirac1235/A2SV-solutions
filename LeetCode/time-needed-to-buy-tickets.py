class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        de = deque(tickets)
        count = 0
        while de[k] != 0:
            for i in range(len(tickets)):
                val = de.popleft() - 1
                if val + 1 != 0:
                    de.append(val)
                    count += 1
                else:
                    de.append(val + 1)
                if val == 0 and i == k:
                    return count
        return count
                
