class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room is None:
                return

            visited.add(room)

            for key in rooms[room]:
                if key not in visited and 0 <= room < len(rooms):
                    dfs(key)

        dfs(0)
        # print(visited)
        return len(visited) == len(rooms)