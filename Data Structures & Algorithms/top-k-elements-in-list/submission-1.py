class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 0
            frequencies[n] = frequencies.get(n) + 1

        sorted_list = sorted(list(frequencies.items()), key=lambda tup: tup[1], reverse=True)

        return [tup[0] for tup in sorted_list][:k:]