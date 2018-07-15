# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: MinimumSumIdexOfTwoLists.py
time: 2018/7/15 15:01
"""

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        item_index_map = {}
        min_index = len(list1) + len(list2)
        output_list = []
        for i in range(len(list1)):
            item_index_map[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in item_index_map:
                cur_index = item_index_map[list2[i]]+i
                if min_index == cur_index:
                    output_list.append(list2[i])
                if min_index > cur_index:
                    min_index = cur_index
                    output_list = [list2[i]]
                else:
                    continue
        return output_list

if __name__ == "__main__":
    s = Solution()
    input1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    input2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    res = s.findRestaurant(input1, input2)
    assert res == ["Shogun"]