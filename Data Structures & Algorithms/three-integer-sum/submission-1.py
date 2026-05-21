class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for ptr in range(n - 2):
            if ptr > 0 and nums[ptr] == nums[ptr-1]:
                continue
            k = ptr + 1
            j = n - 1
            while k < j:
                total = nums[ptr] + nums[k] + nums[j]
                if total == 0:
                    res.append([nums[ptr], nums[k], nums[j]])
                    while k < j and nums[k] == nums[k+1]:
                        k += 1
                    while k < j and nums[j] == nums[j-1]:
                        j -= 1
                    k += 1
                    j -= 1
                elif total < 0:
                    k += 1
                else:
                    j -= 1
        return res