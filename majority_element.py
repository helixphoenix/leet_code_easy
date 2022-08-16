from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        majority_treshold =n//2
        element_counts=defaultdict(int)
        for i in range(n):
            element_counts[nums[i]]+=1
            

        for element in element_counts.keys():
            if element_counts[element]>majority_treshold:
                return element        