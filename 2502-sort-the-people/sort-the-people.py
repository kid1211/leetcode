class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ids = sorted(range(len(names)), key=lambda id: -heights[id] or names[id])
        return [names[i] for i in ids]