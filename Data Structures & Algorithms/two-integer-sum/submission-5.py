class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        # {4:6, 5:5, 6:4}

        for num in range(len(nums)):
            if nums[num] not in complement:
                complement[target - nums[num]] = nums[num]
            else:
                if num < nums.index(complement[nums[num]]):
                    return [num, nums.index(complement[nums[num]])]
                else:
                    return [ nums.index(complement[nums[num]]), num,]
        print(complement)
