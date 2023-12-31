from collections import defaultdict

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        # """
        h=defaultdict(int)
      

        for i in nums:
            print(h.keys())
            h[i]=0
            for key in h.keys():
                if i>=0:
                    if i<key:
                        print("for if ", i)
                        h[i]+=1
                    if key<i:
                        print("for else", i)
                        h[key]+=1
            
                print(h.items())
            
        print(h.items())
        for key, value in h.items():
            if value==k-1:
                print("answwer is ",key)
                return key
            if len(h.keys())==1:
                return key

# Runtime ERROR