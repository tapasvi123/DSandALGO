class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num=[2,2,1,1,1,2,2]

        nums.sort()
        l=len(nums)
        max=nums[0]
        prev=0
        count=0

        for a in range(0,l):
            if nums[a]==max:
                count+=1
                prev=count
                
            else:
                count+=1
                if ((count-prev) > prev):
                    prev=count-prev
                    max=nums[a]
        return max


  
        #  1 2 2 2 2 3 3 3 3 4 4 4 4 4 4 4 4 4 5 5 5 5 
        
# [ Time taken: 29 m 4 s ]
# [ Memory Size: 15.65 MB]
# [ Run Time: 118ms ]
