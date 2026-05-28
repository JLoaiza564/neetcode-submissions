class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> sol;
        for(int i = 0; i < 2; i++) {
            for(int num : nums) {
                sol.push_back(num);
            }

        }
        return sol;
    }
};