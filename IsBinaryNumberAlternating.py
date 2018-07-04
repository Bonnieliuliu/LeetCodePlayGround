"""
author: Bonnie

date: 7/4/2018
name: IsBinaryNumberAlternating.py
"""
def IsBinaryNumberAlternating(n):
    if n < 0:
        return IsBinaryNumberAlternating(-n)
    if n == 0:
        return True
    binary = bin(n)[2:]
    for i in range(1, len(binary)):
        if binary[i] == binary[i-1]:
            return False
        else:
            continue
    return True

if __name__ == "__main__":
    print(IsBinaryNumberAlternating((-14)))