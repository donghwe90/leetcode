# Given Two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must be unique and you may return the result in any order.

def arr_inter(nums1, nums2):
    arr = []
    s = set()

    s = nums1

    for n in s:
        if n not in nums2:
            s.remove(n)

    arr = s
    #print(arr)
    return arr
    
    


arr1 = [1,2,3]
arr2 = [2,3,4]

arr3 = []

arr3 = arr_inter(arr1, arr2)
print(arr3)




        
