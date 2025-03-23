class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        voted = deque(list(senate))
        ready = deque()

        i = 0
        while voted:
            curr = voted.popleft()
            
            if not ready or ready[0] == curr:
                ready += [curr]
            else:
                voted.append(ready.popleft())
            i += 1

            # print(voted, ready)
            if len(ready) + len(voted) == 1:
                break
        val = ready[0] if ready else voted[0]
        return "Dire" if val == "D" else "Radiant"