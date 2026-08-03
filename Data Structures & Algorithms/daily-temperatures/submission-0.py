class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for current_day in range(len(temperatures)):
            while (
                stack
                and temperatures[current_day] > temperatures[stack[-1]]
            ):
                previous_day = stack.pop()

                # 在這裡更新 answer[previous_day]
                answer[previous_day] = current_day - previous_day
            stack.append(current_day)
        return answer