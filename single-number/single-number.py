from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_dict =  Counter(nums) #중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지 dict 형태로 변환
        items = num_dict.items()
        
        for key, val in items: #중복이 있으면 count가 늘어나기에, 중복값이 없는 val이 1인 숫자가 정답
            if val == 1:
                result = key
                break
        return result