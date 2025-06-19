class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int evenPos = 0;
        for(int i=0;i<nums.size();i++){
            if(~nums[i]&1){
                swap(nums[i],nums[evenPos]);
                evenPos+=1;
            }
        }
        return nums;
    }
};