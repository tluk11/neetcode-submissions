class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1) + len(nums2)
        divide = False
        if len1%2 == 0:
            divide = True
        len2 = len1//2+1

        num = []
        p1 = p2 = 0
        while len(num)<len2:
            if p1>=len(nums1):
                num.append(nums2[p2])
                p2+=1
            elif p2>=len(nums2):
                num.append(nums1[p1])
                p1+=1
            elif nums1[p1] < nums2[p2]:
                num.append(nums1[p1])
                p1+=1
            else:
                num.append(nums2[p2])
                p2+=1

        if divide:
            return (num[len(num)-1]+num[len(num)-2])/2
        else:
            return num[len(num)-1]