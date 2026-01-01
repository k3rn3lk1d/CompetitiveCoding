class Solution:
    def missingNum(self, arr):
        sum_val = 0
        for i in arr:
            sum_val+=i
        length = len(arr)
        totalsum = ((length+1)*(length+2))//2
        return totalsum-sum_val