# 2406. Divide Intervals Into Minimum Number of Groups
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for s, e in intervals:
            events.append((s, 1))
            events.append((e, -1))
        print(events)
        events.sort(key=lambda x: (x[0], -x[1]))
        print(events)
        cnt, maxcnt = 0, 0
        for i, t in events:
            if t == 1:
                cnt += 1
            else:
                cnt -= 1
            maxcnt = max(maxcnt, cnt)
        return maxcnt

if __name__ == "__main__":
    print(Solution().minGroups(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
    print(Solution().minGroups(intervals=[[1, 3], [5, 6], [8, 10], [11, 13]]))
    print(Solution().minGroups(intervals=[[1, 3], [3, 6], [8, 10], [11, 13]]))