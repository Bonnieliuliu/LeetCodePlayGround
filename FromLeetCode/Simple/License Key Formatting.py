"""
author = Bonnieliuliu
email = fangyuanliu@pku.edu.cn

file = License Key Formatting.py
time = 2018/8/2 20:29
more information
"""


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "")
        n = len(S)
        first = n % K
        slash = n // K
        if first == 0:
            output = ""
        else:
            output = S[0:first]
        for i in range(slash):
            if i == 0:
                if first == 0:
                    output += S[first + i * K: first + (i + 1) * K]
                else:
                    output += "-" + S[first + i * K: first + (i + 1) * K]
            else:
                output += "-" + S[first + i * K: first + (i + 1) * K]
        return output.upper()

def main():
    input = "59F3Z-2e-9-w"
    K = 4
    s = Solution()
    res = s.licenseKeyFormatting(input, K)
    print(res)
if __name__ == "__main__":
    main()