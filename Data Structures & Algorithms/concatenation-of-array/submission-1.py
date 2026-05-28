class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        solution = []
        for _ in range(2):
            for n in nums:
                solution.append(n)
        return solution
        