"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = MaxConsecutiveOnes.py
time = 2018/8/2 20:27
more information
"""

import json
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        max_count = 0
        for ele in nums:
            if ele == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            ret = Solution().findMaxConsecutiveOnes(nums)
            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()