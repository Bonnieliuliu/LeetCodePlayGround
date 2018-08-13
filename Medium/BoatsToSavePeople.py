"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = BoatsToSavePeople.py
time = 2018/8/11 22:35
more information
"""


class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0
        while (left <= right):
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                right -= 1
        return count
