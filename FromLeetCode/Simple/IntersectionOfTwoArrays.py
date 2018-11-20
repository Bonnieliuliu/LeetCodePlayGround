"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = IntersectionOfTwoArrays.py
time = 2018/8/11 22:18
more information
"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        res = set()
        nums1_set = set(nums1)
        for ele in nums2:
            if ele in nums1_set:
                res.add(ele)
        output = list(res)
        return output

def main():
    s = Solution()
    nums1 = [1,2,2]
    nums2 = [1,2,30]
    res = s.intersection(nums1, nums2)
    print(res)

if __name__ == "__main__":
    main()