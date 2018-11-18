# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Mural.py
time: 2018/11/18 14:07
"""

def Mural(tinput_number, tinput_score):
    output = []
    for iter in range(len(tinput_number)):
        scores = tinput_score[iter]
        N = len(scores)
        half_sum = 0
        maxi = 0
        len_seq = int(N/2)+1 if N%2==1 else int(N/2)
        for i in range(len_seq):
            half_sum += scores[i]
        maxi = half_sum
        for i in range(len(scores)- len_seq):
            half_sum = half_sum - scores[i] + scores[i+len_seq]
            maxi = max(maxi, half_sum)
        output.append(maxi)
    return output


if __name__ == "__main__":
    name = "B-large"
    with open(name+".in") as f:
        tests = int(f.readline())
        tinput_number = []
        tinput_score = []
        for num in range(tests):
            N = f.readline().strip()
            N = int(N)
            tinput_number.append(N)
            line = f.readline().strip()
            score = []
            for s in line:
                score.append(int(s))
            tinput_score.append(score)
    output = Mural(tinput_number, tinput_score)
    wf = open(name+ ".out", "w")
    for i in range(len(output)):
        wf.writelines("Case #{0}: {1}\n".format(i+1, output[i]))
    wf.close()