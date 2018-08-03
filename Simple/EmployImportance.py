# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu, pkusp
email:fangyuanliu@pku.edu.cn

file: EmployImportance.py
time: 2018/7/6 1:26
"""

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        res = 0
        node_q = []
        position = self.FindPos(employees, id)
        if position == -1:
            return 0
        if id >= 0:
            node_q.append(employees[position])
        while len(node_q) > 0:
            head = node_q[0]
            res += head.importance
            if len(head.subordinates):
                for sub in head.subordinates:
                    sub_position = self.FindPos(employees, sub)
                    if sub_position != -1:
                        node_q.append(employees[sub_position])
            del node_q[0]
        return res
    def FindPos(self, employees, id):
        position = -1
        for i in range(len(employees)):
            if employees[i].id == id:
                position = i
        return position


if __name__ == "__main__":
    employees_list = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    employees = []
    id = 1
    for employee in employees_list:
        new = Employee(id=employee[0], importance=employee[1], subordinates=employee[2])
        employees.append(new)
    s = Solution()
    res = s.getImportance(employees, id)
    print('The subordinating Importance of employee of id = {0} is {1}'.format(id, res))