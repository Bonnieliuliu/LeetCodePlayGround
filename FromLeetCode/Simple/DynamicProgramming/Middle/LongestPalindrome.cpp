class Solution {
public:
    string longestPalindrome(string s) 
    {
        if (s.size()<=0) return s;
        int dp[s.size()][s.size()] = {0}, left = 0, right = 0, len = 0;
        for (int i = 0; i<s.size();++i)
        {
            for (int j = 0 ; j<i;++j)
            {
                dp[j][i] = (s[i] == s[j]) && (j>i-2||dp[j+1][i-1]);
                if(dp[j][i] && len<i-j+1)
                {
                    len = i-j+1;
                    left = j;
                    right = i;
                }
            }
            dp[i][i] = 1;
        }
        return s.substr(left, right-left+1);
    }
};