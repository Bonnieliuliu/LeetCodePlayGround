# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: CountWays.py
time: 2018/11/18 15:27
"""
import math
from scipy.special import comb, perm

def CountWays(tinput_number, tinput_newly):
    output = []
    for i in range(len(tinput_number)):
        total = tinput_number[i]
        newly = tinput_newly[i]
        res = helper(total, newly)
        output.append(res)
    return output

def helper(total, newly):
    # count = math.factorial(2*total)
    # iter = 0
    # for i in range(newly, total+1):
    #     if iter%2 == 0:
    #         count -= 2**i*comb(total, i)*math.factorial(2*total-i)
    #     else:
    #         count += 2**i*comb(total, i)*math.factorial(2*total-i)
    #     iter +=1
    count = 0
    for i in range(newly+1):
        count+=comb(newly, i)*math.factorial(2*total-i)*2**i*(-1)**i
    return int(count%1000000007)


if __name__ == "__main__":
    name = "C-small-attempt0"
    with open(name+".in") as f:
        tests = int(f.readline())
        tinput_number = []
        tinput_newly = []
        for num in range(tests):
            total, newly = f.readline().strip().split(" ")
            total = int(total)
            newly = int(newly)
            tinput_number.append(total)
            tinput_newly.append(newly)
    output = CountWays(tinput_number, tinput_newly)
    wf = open(name+ ".out", "w")
    for i in range(len(output)):
        wf.writelines("Case #{0}: {1}\n".format(i+1, output[i]))
    wf.close()