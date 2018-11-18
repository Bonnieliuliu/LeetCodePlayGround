# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: BigButtons.py
time: 2018/11/18 13:18
"""
def BigButtons(tinput_number, tinput_prefix):
    output = []
    i = 0
    for ele in tinput_number:
        N = ele[0]
        P = ele[1]
        count = 2**N
        prefix_list = sorted(tinput_prefix[i])
        for j in range(len(prefix_list)-1, -1, -1):
            for k in range(j-1, -1, -1):
                if prefix_list[j].startswith(prefix_list[k]):
                    del prefix_list[j]
                    break
                else:
                    continue
        for item in prefix_list:
            len_item = len(item)
            decrease = 2**(N-len_item)
            count -= decrease
        count = 0 if count<0 else count
        i+=1
        output.append(count)
    return output
if __name__ == "__main__":
    with open("A-large.in") as f:
        tests = int(f.readline())
        tinput_number = []
        tinput_prefix = []
        for num in range(tests):
            line = f.readline()
            N, P = line.split(" ")
            N = int(N)
            P = int(P)
            tinput_number.append([N, P])
            prefix_list = []
            for in_num in range(P):
                prefix = f.readline()
                prefix = prefix.strip()
                prefix_list.append(prefix)
            tinput_prefix.append(prefix_list)
    output = BigButtons(tinput_number, tinput_prefix)
    wf = open("A-large.out", "w")
    for i in range(len(output)):
        wf.writelines("Case #{0}: {1}\n".format(i+1, output[i]))
    wf.close()