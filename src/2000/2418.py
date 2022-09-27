from typing import List
# 2418. Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuple = zip(names, heights)
        sortedTuple = sorted(tuple, key=lambda x: x[1], reverse=True)
        print(sortedTuple)
        return [i[0] for i in sortedTuple]


if __name__ == '__main__':
    func = Solution().sortPeople
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]
    print(func(names, heights))