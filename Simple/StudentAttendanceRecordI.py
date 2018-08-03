# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: StudentAttendanceRecordI.py
time: 2018/7/23 22:24
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        resA = 0
        resL = 0
        for char in s:
            if char == "P":
                resL = 0
            elif char == "A":
                resA += 1
                if resA > 1:
                    return False
                resL = 0
            else:
                resL += 1
                if resL > 2:
                    return False
        return True

