class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        nl = len(nums)
        delta = 100000
        res = nums[0] + nums[1] + nums[2]
                                                                                                    
        for idx, num in enumerate(nums):
             
            if idx < nl - 1 and num == nums[idx-1]:
                continue
                                                                                                                                                        
            i, j = idx + 1, nl -1
            while i < j:
                # print "-----", idx, i, j
                tt = num + nums[i] + nums[j]
                if tt == target:
                    return tt
                elif tt > target:
                    # print ">", res, tt, delta
                    if delta > tt - target:
                        delta = tt - target
                        res = tt
                    j -= 1
                else:
                    if delta > target - tt:
                        delta = target - tt
                        res = tt
                    i += 1
                
                
        return res
