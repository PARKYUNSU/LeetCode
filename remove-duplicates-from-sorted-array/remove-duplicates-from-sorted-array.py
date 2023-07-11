class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:  #nums이 비어있을때
            return None

        first_nums = 1 #첫번째 숫자는 첫 고유값이니깐 한 개 반환
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[first_nums] = nums[i]  #고유값으로 설정
                first_nums += 1  #고유값 개수 증가
        return first_nums