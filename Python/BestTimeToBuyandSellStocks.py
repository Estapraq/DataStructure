#Youtube channel @TechWithEsta
class ArrayBestTimeToBuySellStocks:
     '''   
      Best Time to Buy and Sell Stocks                             
      --------------------------------
      Say you have an array for which the ith element is
      the price of a given stock on day i.
      If you were only permitted to complete at most one 
      design an algorithm to find the maximum profit. 
      transaction (i.e buy one and sell one share of the stock),

     '''
     def maxProfit(prices:list[int]) -> int: 
      l, r= 0, 1 #l=buy r=sell
      maxProfit = 0

      while r < len(prices):
         if prices[l]<prices[r]:
            profit = prices[r]-prices[l]
            maxProfit=max(profit, maxProfit)
         else:
            l=r

         r +=1
      return maxProfit   


     result=maxProfit([2,3,1,4,10])
     print(result)

                       
