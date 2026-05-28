class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in solution:
                solution[sorted_s] = []
            
            solution[sorted_s].append(s)

        return [v for k, v in solution.items()]