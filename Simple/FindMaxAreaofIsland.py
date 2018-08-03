"""
author: Bonnie

date: 7/4/2018
name: FindMaxAreaofIsland.py
"""

def FindMaxAreaOfIsland(island):
    m = len(island)
    n = len(island[0])
    max_area = 0
    for i in range(m):
        for j in range(n):
            if island[i][j] != 1:
                continue
            cur_area = 0
            area = Helper(island, i, j, cur_area)
            max_area = max(max_area, area)
            print('max_area', max_area)
    return max_area

def Helper(island, i, j, area):
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    m = len(island)
    n = len(island[0])
    if (i < 0 or i >= m or j < 0 or j >= n or island[i][j] <= 0):
        return area
    island[i][j] *= -1
    area = area + 1
    for dir in dirs:
        area = Helper(island, i+dir[0], j+dir[1], area)
    return area

if __name__ == "__main__":
    island = [   [0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    island = [[0,0,0,0,0,0,0,0]]
    print(FindMaxAreaOfIsland(island))