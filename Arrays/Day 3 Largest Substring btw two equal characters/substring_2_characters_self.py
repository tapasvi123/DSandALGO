# LARGEST SUBSTRING BTW TWO EQUAL CHARACTERS

from collections import defaultdict

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        h=defaultdict(list)
        l=len(s)
        # print(l)
        for index, char in enumerate(s):
            h[char].append(index)

        print(h.items())

        max_diff=-1
        for key, values in h.items():
            if (max(values)-(min(values)+1))>max_diff:
                max_diff=max(values)-(min(values)+1)
        return max_diff
            

#TEST CASES
# "abcdauytsahisuhiuhau"
# "aaaaaa"
# "ydngowmdhaop" 

# Runtime: 11ms  (17.18%)
# Memory: 13.29 MB  (89.09%)

# First attempt. Used a dictionary. max and min functions take up time. Can be improved..