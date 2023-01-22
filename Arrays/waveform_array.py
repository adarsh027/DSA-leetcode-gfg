#logic: think of them in triplets such that the every even indexed value is greeater
#than adjacent odd indexed values.Thus for every even indexed i, the following 2 conditions
#should be met:
# 1. arr[i-1]<arr[i]
# 2. arr[i]>arr[i+1]
#note: waveform can also be formed by having every odd indexed value greater
# than adjacent even indexed values. In such case, you will use the range function() as
# range(1,len(arr),2) to loop through all odd indexed values


class Solution:
    def convertToWave(self, arr, n):
        for i in range(0,n,2):
            
            # If current even element is smaller than previous
            if i>0 and arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                
            # If current even element is smaller than next
            if i< n-1 and arr[i]<arr[i+1]: # index=0 gets considered here
                 arr[i], arr[i+1] = arr[i+1], arr[i]
        return arr
    
Solution().convertToWave([1,2,3,4,5], 5)


    
#Ref: https://www.enjoyalgorithms.com/blog/sort-an-array-in-a-waveform
# https://www.geeksforgeeks.org/sort-array-wave-form-2/
    
    
