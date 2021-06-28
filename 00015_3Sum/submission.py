class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        
        nums = sorted(nums)
        tmp_res = {}
        
        for idx in range(len(nums) - 2):
            i, j = idx + 1, len(nums) - 1
            while i < j:
                tmp = nums[idx] + nums[i] + nums[j]
                if tmp == 0:
                    tmp_res[(nums[idx], nums[i], nums[j])] = True
                    i += 1
                elif tmp > 0:
                    j -= 1
                else:
                    i += 1
        res = []
        for key in tmp_res:
            res.append(list(key))
        
        return res




class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Time complexity: O(n^2)
        # Space complexity: O(n)
                                                                            
        res = []
        
        pos = {}
        neg = {}
        z = 0
                                                                                                                            
        for num in nums:
            if num == 0:
                z = z + 1
            elif num > 0:
                pos[num] = True if num in pos else False
            else:
                neg[num] = True if num in neg else False
                                                                                                                                                                                                                                                            
        if z:
            if z >= 3:
                res.append([0, 0, 0])
            
            for p in pos:
                if -p in neg:
                     res.append([-p, 0, p])
        
        for p in pos:
            for n in neg:
                target = - (p + n)
                if target in pos and ((target == p and pos[target]) or target > p):
                    res.append([n, p, target])

                if target in neg and ((target == n and neg[target]) or target < n ):
                    res.append([target, n, p])
        
        return res
