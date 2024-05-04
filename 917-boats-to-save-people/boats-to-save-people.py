class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        res = []
        left, right = 0, len(people) - 1
        while left < right:
            if people[left] + people[right] <= limit:
                res += [[
                        people[left],
                        people[right]
                        ]]
                left += 1
                right -= 1
            elif people[right] > limit:
                return -1
            else:
                res += [[people[right]]]
                right -= 1
        # print(res, left, right)
        if left == right:
            res += [people[left]]
        return len(res)
