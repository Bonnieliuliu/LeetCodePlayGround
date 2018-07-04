"""
author: Bonnie

date: 7/3/2018
name: MinLengthSubStringWithSameDegree.py
"""
def MinSubStringWithSameDegree(given_list):
    position_map = {} # <element, [start_index, end_index]>
    freq_map = {} # <element, frequency>
    degree = 0
    for i in range(len(given_list)):
        freq_map[given_list[i]] = freq_map.get(given_list[i], 0) + 1
        if freq_map[given_list[i]] == 1:
            position_map[given_list[i]] = [i, i]
        else:
            position_map[given_list[i]][1] = i
        degree = max(degree, freq_map[given_list[i]])
    min_length = len(given_list)
    for (k, v) in freq_map.items():
        if degree == v:
            if min_length > position_map[k][1] - position_map[k][0] + 1:
                min_length = position_map[k][1] - position_map[k][0] + 1
    return min_length

if __name__ == "__main__":
    print(MinSubStringWithSameDegree([1, 2, 2, 3, 1, 4, 2]))