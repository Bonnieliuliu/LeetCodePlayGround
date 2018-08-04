# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: SubdomainVisitCount.py
time: 2018/8/4 13:17
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dicts = {}
        n = len(cpdomains)
        for item in cpdomains:
            array = item.split(' ')
            num = (int)(array[0])
            domain = array[1]
            domainLen = len(domain.split('.'))
            for i in range(domainLen):
                tmp = domain.split('.', i).pop()
                print(domain.split(".", i), tmp)
                if tmp in dicts.keys():
                    dicts[tmp] = dicts[tmp] + num
                else:
                    dicts[tmp] = num

        domainList = []
        for key in dicts:
            tmp = (str)(dicts[key]) + " " + key
            domainList.append(tmp)
        return domainList

def main():
    input = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    s = Solution()
    res = s.subdomainVisits(input)
    print(res)

if __name__ == "__main__":
    main()