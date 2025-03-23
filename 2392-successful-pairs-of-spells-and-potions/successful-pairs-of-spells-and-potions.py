class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions, 
        # find the mid and see if it greater, if not keep get_origin
        # use the index
        potions.sort()

        def findPairs(val):
            n = len(potions)
            left, right = 0, n - 1

            while left + 1 < right:
                mid = (left + right) // 2

                if potions[mid] * val < success:
                    left = mid
                else:
                    right = mid

            if potions[left] * val >= success:
                return n - left
            elif potions[right] * val >= success:
                return n - right
            else:
                return 0

        return [findPairs(spell) for spell in spells]
