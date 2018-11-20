# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: PlanetDistance.py
time: 2018/11/18 11:52
"""
from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, vertices, dis, res):
        self.V = vertices  # No. of vertices
        self.distance = dis
        self.res = res
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list

    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):

        # Mark the current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif parent != i:
                self.res.append(v)
                return True

        return False

    # Returns true if the graph contains a cycle, else false.
    def isCyclic(self):
        # Mark all the vertices as not visited
        visited = [False] * (self.V + 1)
        # Call the recursive helper function to detect cycle in different
        # DFS trees
        for i in range(1, self.V + 1):
            if visited[i] == False:  # Don't recur for u if it is already visited
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True
        return False



    def judge(self, u, v):
        visited = [False] * (self.V + 1)
        distance = [0 for i in range(self.V + 1)]
        queue = []
        queue.append(u)
        visited[u] = True
        while queue:
            x = queue.pop(0)
            for i in self.graph[x]:
                if visited[i] == False:
                    distance[i] = distance[x] + 1
                    queue.append(i)
                    visited[i] = True
        return distance[v]


    def count_dis(self):
        cycle_list = []
        for i in self.graph[self.res[0]]:
            cycle_list.append(i)
        cycle_list.append(self.res[0])
        visited = [False] * (self.V + 1)
        for i in range(1, self.V + 1):
            if i in cycle_list:
                self.distance[i] = 0
            else:
                len_min = self.V + 1
                for j in cycle_list:
                    tem_min = self.judge(i, j)
                    if tem_min < len_min:
                        len_min = tem_min
                self.distance[i] = len_min


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Kickstart problems.
    t = int(input())  # read a line with a single integer
    for ti in range(1, t + 1):
        n = int(input())
        dis = [0 for i in range(n + 1)]
        res = []
        g = Graph(n, dis, res)
        for i in range(n):
            n, m = [int(s) for s in input().split(" ")]
            g.addEdge(n, m)
        if g.isCyclic():
            g.count_dis()
            print("Case #{0}:".format(ti), end='')
            for x in dis[1:]:
                print(' ',x, end='')
            print('\n', end='')



        # check out .format's specification for more formatting options