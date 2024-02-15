import re
class Solution(object):
    def reverseWords(self, s):
        # print(s)
        str=re.split("[\s]+", s)
        # print(str)
        for x in str:
            # print("read word: "+ x)
            ind=str.index(x)
            if x=='':
                str.pop(ind)
        # print("The new string with out spaces.")
        # print(str)

        # print(str+" is the new string without spaces.")        
        i=0
        str2=[]
        for x in range(len(str)-1, -1, -1):
                str2.append(str[x])
                # print(str[x]+" is read at ",x )
        str3=" ".join(str2)
        # print(str3)
        return str3


# [ Time taken: 20 m 48 s ]
# Runtime: 26ms
# Memory:13.56 MB
#  This solution uses regEx to Split the words based on a single white space or multiple ones. Additionally, it uses an if block to pop the characters with extra whitespaces that were missed.

# Lists is used to store the splitted string and manual reversing is done and the string is merged using the join method of strings. 

# New functions learnt but logically this is very poor. Need to try using other languages.