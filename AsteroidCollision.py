"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = AsteroidCollision.py
time = 2018/8/4 16:18
more information
"""
class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = asteroids
        while True:
            if len(res)<=1:
                return res
            tmp = [res[0]]
            for i in range(1, len(res)):
                planet = res[i]
                if (not tmp or planet * tmp[-1] > 0 or tmp[-1] < 0 and planet > 0):
                    tmp.append(planet)
                elif (planet+tmp[-1] == 0):
                    tmp.pop()
                elif (planet < 0 and tmp[-1] + planet < 0):
                    tmp[-1] = planet
            if res == tmp:
                break
            else:
                res = tmp
        return res

def main():
    input = [10, -2, -5]
    s = Solution()
    res = s.asteroidCollision(input)
    print(res)
if __name__ == "__main__":
    main()