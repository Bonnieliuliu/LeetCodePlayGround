# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn
2
5 7
1 3
1 5
2 3
2 5
3 4
4 5
3 5
4 3
1 2
2 3
3 4
file: Sep_09_j2.py
time: 2018/9/9 20:16
"""
import sys
import os
import re
from collections import defaultdict



def solve(vertex, edges):
    vertex_mapping = defaultdict(list)
    partition = list()
    part = 0
    for edge in edges:
        vertex_mapping[edge[0]].append(edge[1])
        vertex_mapping[edge[1]].append(edge[0])
    for k, v in vertex_mapping.items():
        if v not in partition:
            partition.append(v)
            part += 1
        else:
            pass
    part_mem = []
    i = -1
    for ele in partition:
        i += 1
        row = []
        for k, v in vertex_mapping.items():
            if vertex_mapping[k] == ele:
                row.append(k)
        part_mem.append(row)
    len_list = []
    res = 0
    for i in range(len(part_mem)):
        len_list.append(len(part_mem[i]))
    for i in range(len(len_list)):
        cur = 0
        for j in range(i+1, len(len_list)):
           cur += len_list[i]*len_list[j]
        res += cur
    return res == len(edges)


def main():
    m = int(input())
    ans = []
    for i in range(m):
        row = sys.stdin.readline().strip()
        row = map(int, row.split())
        vertex = row[0]
        lines = row[1]
        edges = []
        for i in range(lines):
            line = sys.stdin.readline().strip()
            line = map(int, line.split())
            edges.append(line)
        res = solve(vertex, edges)
        ans.append(res)
    for ele in ans:
        if ele:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()