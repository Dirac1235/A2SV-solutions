class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p = 0
        t = 0
        count = 0
        while t < len(trainers) and p < len(players):
            if players[p] <= trainers[t]:
                p += 1
                t += 1
                count += 1
            else:
                t += 1
        return count
        
