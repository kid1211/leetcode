class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        unique = set()
        for item in arr:
            if item in unique:
                return True
            unique.add(item / 2)
            unique.add(item * 2)
        return False    