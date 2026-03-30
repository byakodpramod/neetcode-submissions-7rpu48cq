class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, slate):
            if i == len(nums):
                result.append(slate[:])
                return
            count = 0
            for idx in range(i,len(nums)):
                if nums[i] == nums[idx]:
                    count += 1
                else:
                    break
            #exclude
            helper(i+count, slate)
            #include
            for c in range(count):
                slate.append(nums[i])
                helper(i+count, slate)
            for c in range(count):
                slate.pop()
        
        nums.sort()
        result = []
        helper(0,[])
        return result