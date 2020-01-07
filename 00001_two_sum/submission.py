class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for idx, num in enumerate(nums):
             if num in index:
                 index[num].append(idx)
             else:
                 index[num] = [idx]
        new_nums = sorted([n for n in index])
        i, j = 0, len(new_nums)-1
        while i < j:
            tmp_target = new_nums[i] + new_nums[j] 
            if tmp_target == target:
                break
            elif tmp_target < target:
                i += 1
            else:
                j -= 1
        A, B = new_nums[i], new_nums[j]
        # print(A, B)
        if A == B:
            return sorted([x for x in index[A]])[:2]
        else:
            return sorted([index[A][0], index[B][0]])
