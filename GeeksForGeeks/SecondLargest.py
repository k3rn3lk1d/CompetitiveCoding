class Solution:
    def getSecondLargest(self, arr):
        first_max = -2
        second_max = -1
        for i in arr:
            if(i>first_max):
                second_max = first_max
                first_max = i
            elif(i>second_max and i<first_max):
                second_max=i
        return second_max
            