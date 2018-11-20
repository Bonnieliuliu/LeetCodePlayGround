# -*- coding:utf-8 -*-
"""
author:Bonnieliuliu
email:fangyuanliu@pku.edu.cn

file: 1.py
time: 2018/9/7 19:49
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听
"""
import re
from collections import defaultdict
class Solution(object):
    def read(self):
        relation = raw_input().strip().split(";")
        sentence = raw_input()
        relation_dict = dict()
        name_lst = list()
        entitymapping = {}
        namemapping = defaultdict(list)
        for ele in relation:
            ele = ele.split("_")
            title = ele[0]
            entity = ele[1]
            entitymapping[title] = entity.split("|")
        for k, v in entitymapping.items():
                for val in v:
                    namemapping[val].append(k)
                    name_lst.append(val)
        name_lst = sorted(name_lst, key = lambda x: len(x), reverse=True)
        return namemapping , name_lst, sentence

    def match(self, rela, name_lst, sen):
        pattern = "|".join(name_lst)
        pattern = re.compile(pattern)
        res = re.findall(pattern, sen)
        for ele in res:
            start = sen.find(ele)
            end = start + len(ele)
            print(rela[ele])
            tag = ",".join(rela[ele])
            sen = sen[:start]+" "+sen[start:end]+"/"+tag+" "+sen[end:]
        return sen

    def Relation(self, rela, word):
        ans = []
        for k, v in rela.items():
            if v == word:
                ans.append(k)
        ans.sort()
        return ans

def main():
    s = Solution()
    rela, name_lst, sen = s.read()
    res = s.match(rela, name_lst, sen)
    print(res)

if __name__ == "__main__":
    main()
