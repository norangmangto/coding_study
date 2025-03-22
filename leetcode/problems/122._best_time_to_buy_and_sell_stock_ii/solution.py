class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit = 0
        bought_price = -1

        for i in range(n-1):
            if bought_price == -1 and prices[i+1] > prices[i]:
                bought_price = prices[i]
                print(f"buy a stock: {prices[i]=}")
            elif bought_price >= 0 and prices[i+1] < prices[i]:
                profit += prices[i] - bought_price
                bought_price = -1
                print(f"sell a stock: {prices[i]=}")
                print(f"profit: {profit=}")

        if bought_price >= 0:
            profit += prices[i+1] - bought_price
            bought_price = -1
            print(f"FINAL! sell a stock: {prices[i]=}")
            print(f"profit: {profit=}")

        return profit

    def simplest_solution(self, prices: list[int]) -> int:
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))

    def other_solution2(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]

        return profit
