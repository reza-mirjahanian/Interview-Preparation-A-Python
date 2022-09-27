from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        idx1, idx2 = 0, 0
        while idx2 < len(trainers):
            if idx1 < len(players) and trainers[idx2] >= players[idx1]:
                idx1 += 1
            idx2 += 1
        return idx1


if __name__ == '__main__':
    # 2
    print(Solution().matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]))
    # 1
    print(Solution().matchPlayersAndTrainers([1, 1, 1], [10]))
