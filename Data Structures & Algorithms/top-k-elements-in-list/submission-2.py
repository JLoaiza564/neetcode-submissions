class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        frequencies = {}

        for n in nums:
            if n not in frequencies:
                frequencies[n] = 0
            frequencies[n] = frequencies.get(n) + 1

        counts = [[] for _ in range(len(nums) + 1)]

        for k, v in frequencies.items():
            counts[v].append(k)

        solution = []

        for nums in reversed(counts):
            for n in nums:
                solution.append(n)
                if len(solution) == t:
                    return solution
            