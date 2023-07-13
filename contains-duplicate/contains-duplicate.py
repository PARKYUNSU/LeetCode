class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums=list(set(nums)) #set은 중복 값을 허용하지 않음을 이용
        return len(new_nums) != len(nums) #중복 값을 제거한 new_nums와 기존 nums 길이가 다르면 중복 값이 있으므로 True