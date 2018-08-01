# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: NextGreaterElementI.py
time: 2018/8/2 1:34
"""
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1:
            return nums1
        nums_pos = {}
        n = len(nums2)
        i = 0
        output = []
        for ele in nums2:
            nums_pos[ele] = i
            i += 1
        for ele in nums1:
            find = False
            for i in range(nums_pos[ele] + 1, n):
                if nums2[i] > ele:
                    output.append(nums2[i])
                    find = True
                    break
            if find == False:
                output.append(-1)
        return output

if __name__ == "__main__":
    s = Solution()
    nums1 = [1,2,3]
    nums2 = [2,4,1,3]
    res = s.nextGreaterElement(nums1, nums2)
    print(res)
# def stringToIntegerList(input):
#     return json.loads(input)
#
#
# def integerListToString(nums, len_of_list=None):
#     if not len_of_list:
#         len_of_list = len(nums)
#     return json.dumps(nums[:len_of_list])
#

# def main():
#     import sys
#     def readlines():
#         for line in sys.stdin:
#             yield line.strip('\n')
#
#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             nums1 = stringToIntegerList(line)
#             line = next(lines)
#             nums2 = stringToIntegerList(line)
#
#             ret = Solution().nextGreaterElement(nums1, nums2)
#
#             out = integerListToString(ret)
#             print(out)
#         except StopIteration:
#             break
#
#
# if __name__ == '__main__':
#     main()