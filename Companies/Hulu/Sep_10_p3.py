# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: Sep_10_p3.py
time: 2018/9/10 18:51
"""
from collections import defaultdict
class Solution(object):
    def LeastDaysCons(self, dep, m, n):
        """

        :param dep: dependency
        :param m: m tasks
        :param n: n workers
        :return: least days of construction
        """
        tasks = list(range(1, m+1))
        work_in = defaultdict(list)  # 工作：[依赖他的工作]
        work_dep = defaultdict(list) # 工作：[所依赖的工作]
        work_done = []
        work_todo = []
        for pair in dep:
            work_dep[pair[0]].append(pair[1])
            work_in[pair[1]].append(pair[0])
        cnt_days = 1
        cnt_workers = 0
        for i in range(len(tasks)):
            if cnt_workers > n:
                cnt_days+=1
                cnt_workers = 0
            if tasks[i] not in work_dep:
                pass
            else:
                for needdone in work_dep[tasks[i]]:
                    if needdone in work_done:
                        pass
                    else:
                        cnt_workers+=1
                        work_done.append(needdone)
            work_done.append(tasks[i])
            cnt_workers+=1
        if cnt_workers%2:
            rem_days = int(cnt_workers/2)+1
        else:
            rem_days = int(cnt_workers/2)
        return cnt_days + rem_days

def main():
    tinput = list(map(int, input().split()))
    m = tinput[0]
    n = tinput[1]
    k = tinput[2]
    dependency = []
    for i in range(k):
        dependency.append(list(map(int, input().split())))
    s = Solution()
    res = s.LeastDaysCons(dependency, m, n)
    print(res)

if __name__== "__main__":
    main()
