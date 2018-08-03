"""
author: Bonnie

date: 7/4/2018
name: CountBinarySubstrings.py
"""
def CountBinarySubstrings(binstr):
    count = 0
    if len(binstr) == 1:
        return count
    cur = 1
    pre = 0
    for i in range(1, len(binstr)):
        if binstr[i] == binstr[i-1]:
            cur += 1
        else:
            pre = cur
            cur = 1
        if cur <= pre:
            count += 1
    return count

if __name__ == "__main__":
    print(CountBinarySubstrings('10101'))