class Solution
{
public:
    #include <bitset>
    vector<string> readBinaryWatch(int num)
    {
        vector<string> times;
        for (int i = 0; i < 12; i++) {
            bitset<4> h(i);//4位的二进制数
            for (int j = 0; j < 60; j++) {
                bitset<6> m(j);//6位的二进制数
                if (h.count() + m.count() == num)//h.count()函数判断h中1的个数
                    times.push_back(to_string(i) + (j < 10? ":0": ":") + to_string(j));
            }
        }
        return times;
    }
};