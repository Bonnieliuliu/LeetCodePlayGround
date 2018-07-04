"""
author: Bonnie

date: 7/3/2018
name: EndsWith1Bit.py
"""
def EndsWith1Bit(given_list):
    i = 0
    while i <= len(given_list)-2:
        if given_list[i] == 1:
            i += 2
        else:
            i += 1
    if i == len(given_list) - 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(EndsWith1Bit([1, 1, 1, 0]))