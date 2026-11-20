class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        3, 4, 5, 6

        dict: number:index

        diff in dict:
        return dict[number], i
        """

        seen = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seen:
                return [seen[diff], i]

            seen[nums[i]] = i

        return None
        