class Solution {
public:
    int hammingDistance(int x, int y)
    {
        int res = 0;
        for(int i = 0; i<=31; ++i)
        {
            if ((x& (1<<i))^(y&(1<<i))) res ++ ;

        }
    return res;
    }

};