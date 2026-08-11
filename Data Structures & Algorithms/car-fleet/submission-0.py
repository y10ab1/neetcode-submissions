class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, v) for p, v in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, v in pair:
            time = (target-p)/v
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)