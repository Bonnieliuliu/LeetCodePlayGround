
# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_18_p2.py
time: 2018/9/18 20:01
"""
class Solution(object):
    def Ways(self, op):
        id_num = 0
        res = []
        region = []
        for ele in op:
            if ele[0] == "T":
                region.append([ele[1], ele[2]])
            if ele[0] == "Q":
                id = ele[1]
                start_x = region[id][0][0]
                start_y = region[id][0][1]
                end_x = region[id][1][0]
                end_y = region[id][1][1]
                k = (end_y-start_y)/(end_x-start_x)
                for i in range(id):
                    temp1_x = region[i][0][0]
                    temp1_y = region[i][0][1]
                    temp2_x = region[i][1][0]
                    temp2_y = region[i][1][1]
                    k_temp = (temp2_y-temp1_y)/(temp2_x-temp1_x)
                    if k_temp == k:
                        if (temp1_x>=start_x or temp2_x<=end_x) and (temp1_y>=start_y or temp2_y<=end_y):
                            id_num+=1
                    else:
                        if k*k_temp<0:
                            id_num += 1
            res.append(id_num)
        return res


def main():
    n = int(input().strip())
    s = Solution()
    res = []
    for _ in range(n):
        op = []
        m = int(input().strip())
        for line in range(m):
            line = input().strip().split()
            if line[0] == "T":
                start = (int(line[1]), int(line[2]))
                end = (int(line[3]), int(line[4]))
                row = ["T", start, end]
            if line[0] == "Q":
                id = int(line[1])
                row = ["Q", id]
            op.append(row)
        ans = s.Ways(op)
        res.append(ans)
    for ans in res:
        for ele in ans:
            print(ele)
        print()

if __name__ == "__main__":
    main()