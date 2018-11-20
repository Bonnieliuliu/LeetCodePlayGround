class Solution {
public:
    int findComplement(int num)
    {
        bool flag = false;
        for (int i = 31; i >= 0; --i)
        {

            if (num & (1<<i)) flag = true;
            if (flag == true)
            {
                num ^= (1<<i);
            }
        }
        return num;
    }
};