def readData():
    arr = []
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        line = line.split()
        values = list(map(int, line))
        values.pop()
        arr.append(values)
    return n, arr

def Partition(n, arr):
    output = []
    for i in range(len(arr)):
        for j in arr[i]:
            arr[i].extend([ele for ele in arr[j-1]])
        man_know = set(arr[i])
        man_know.add(i+1)
        output.append(man_know)
    output.sort()
    i = 0
    j = 1
    m = 0
    while (i < n):
        j = i+1
        while j>i and j<n:
            if output[i]&output[j]:
                output[j].update(output[i])
                i+=1
                break
            else:
                j+=1
        if j == n:
            m+=1
            i+=1
    return m

import sys
if __name__ == "__main__":
    n, arr = readData()
    final = Partition(n, arr)
    print(final)