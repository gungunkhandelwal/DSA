def buyOrSell(prices):
    profit = 0
    index = 0
    buy = prices[0]
    sell=0

    for day in range(len(prices)):
        if prices[day] <= buy:
            buy = prices[day]
            sell=prices[day]
            index = day
            for i in range(index, len(prices)):
                if prices[i] > sell:
                    sell = prices[i]
        profit = max(profit, sell - buy)
    return profit

prices = [7,1,5,3,6,4]
print(buyOrSell(prices))
p1=[1,2]
print(buyOrSell(p1))

