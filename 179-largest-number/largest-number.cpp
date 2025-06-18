class Solution {
    private:
    static bool custom_sorting(string a, string b){
        return a+b>b+a;
    }
public:
    string largestNumber(vector<int>& nums) {
        vector<string> temp;
        for(auto &it: nums){
            temp.push_back(to_string(it));
        }
        sort(temp.begin(),temp.end(),custom_sorting);
        string ans = "";
        if (temp.size()>=1){
            if(temp[0]=="0") return ans+'0';
        }
        for(int i=0;i<temp.size();i++){
            ans+=temp[i];
        }
        return ans;
    }
};