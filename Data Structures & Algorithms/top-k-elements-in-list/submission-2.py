class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_nums = sorted(
            frequency,
            key=lambda num: frequency[num],
            reverse=True
        )

        return sorted_nums[:k]