class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
# Storing all the positive profit pairs, finding the maximum.
# Negative profit (loss) pairs ignored, and min updated to find new profit pairs.  
        profit=[]
        low=10001
        flag=0
        for x in prices:
            if x<low:
                low=x
            else:
                flag=1
                profity=x-low
                profit.append(profity)
        if flag==0:
            profit_made=0
            return (profit_made)
        
        return (max(profit))

# SPCL. TEST CASES

# [7,6,3,2,1,4,3,2]  ignore everything before lower
# [7,3,4,6,4,2,1] profit possible
# [7,6,5,3,2,1] completely descending. not possible

sol= Solution()
list1=[7,6,3,2,1,4,3,2]
list2=[7,3,4,6,4,2,1]
list3=[7,6,5,3,2,1] 
print(sol.maxProfit(list1))
print(sol.maxProfit(list2))
print(sol.maxProfit(list3))

# Runtime: [792 ms]
# Space consumed: [22.58 MB] 

# Not very optimised -- Check leetcode for other atempts you made, its still commented