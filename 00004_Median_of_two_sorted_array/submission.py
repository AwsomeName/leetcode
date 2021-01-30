class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 先归并排序合为一个数组，再返回对应位置的数字
        res = []
        self.merge(nums1, nums2, res)
        print res
        if len(res) % 2 == 0:
            idx = len(res) / 2 - 1
            return (res[idx] + res[idx+1]) / 2.0
        else:
            if len(res) == 1:
                return float(res[0])
            idx = len(res) // 2
            return float(res[idx])
        
        
    def merge(self, nums1, nums2, res):
        if len(nums1) == 0:
            res.extend(nums2)
            return 
        if len(nums2) == 0:
            res.extend(nums1)
            return
        if nums1[0] < nums2[0]:
            res.append(nums1[0])
            self.merge(nums1[1:], nums2, res)
            return
        else:
            res.append(nums2[0])
            self.merge(nums1, nums2[1:], res)
            return
        
        
        