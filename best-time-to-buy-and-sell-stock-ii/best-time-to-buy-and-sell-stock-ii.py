class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0 #처음은 0으로 시작
        
        for i in range(1, len(prices)): #처음부터 prices list 전체 탐색
            profit = prices[i] - prices[i-1] #구매한 날의 익일 금액의 차
                
            if profit > 0: #이윤이 날 때만 계산하기
                total += profit
        return total