class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackID = stack.pop()
                output[stackID] = i - stackID
            stack.append((t, i))
        return output