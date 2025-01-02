class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsmap={}
        for i in range(len(nums)):
            t=target - nums[i]
            if t in numsmap:
                return[numsmap[t],i]
            numsmap[nums[i]]=i
        return []