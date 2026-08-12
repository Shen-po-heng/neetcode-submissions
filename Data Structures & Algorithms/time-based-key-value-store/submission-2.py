class TimeMap:

    def __init__(self):
        self.node = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.node:
            self.node[key] = []

        self.node[key].append({
            "value": value,
            "timestamp": timestamp
        })

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.node:
            return ""

        left = 0
        right = len(self.node[key]) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            current_timestamp = self.node[key][mid]["timestamp"]

            if current_timestamp <= timestamp:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        if result == -1:
            return ""
        else:
            return self.node[key][result]["value"]

