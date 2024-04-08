class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = Counter(students)

        for i in range(len(sandwiches)):
            item = sandwiches[i]
            if counter[item] == 0:
                return len(sandwiches) - i
            counter[item] -= 1
            # print(item, counter)
        return 0