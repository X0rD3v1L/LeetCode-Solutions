'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.

Link - https://leetcode.com/problems/sort-colors/'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low,high,mid = 0,len(nums)-1,0
        
        while mid<=high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1;mid += 1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
            else:
                mid += 1
