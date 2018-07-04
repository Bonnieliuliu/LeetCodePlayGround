"""
author: Bonnie
date: 7/4/2018
name: IntAlternating.py
"""
def dec2bin(n):
    l = []
    if n < 0:
        return '-' + dec2bin(-n)
    while True:
        n, remainder = divmod(n, 2)
        l.append(str(remainder))
        if n == 0:
            return ''.join(l[::-1])
def divmod(beichushu, chushu):
    return beichushu // chushu, beichushu % chushu

if __name__ == "__main__":
    b = dec2bin(-5)
    print(b)
    print(bin(-5)[2:])

