class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            while j < k:
                local = nums[i] + nums[j] + nums[k]
                if local > 0:
                    k -= 1

                elif local < 0:
                    j += 1

                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1

        return res



        