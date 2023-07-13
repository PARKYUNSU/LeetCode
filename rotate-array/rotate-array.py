class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) #k가 nums리스트 보다 클 경우 예를들어, nums=[1,2,3], k=5 에서 k를 nums의 길이로 나누어 몫을 새로운 k로 할당
        nums[:] = nums[-k:] + nums[:-k] #nums의 전체리스트는 k기준으로 슬라이싱