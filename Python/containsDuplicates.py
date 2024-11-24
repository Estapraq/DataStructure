#Youtube channel @TechWithEsta
class Solution:
     '''   
      Contains Duplicates                            
      --------------------------------
      Given an int array nums, return true if the value 
      appears at least twice in the array, and return false
      if every element is distinct.

     '''
     def containsDuplicates(prices:list[int]) -> int: 
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


     result=containsDuplicates([2,3,1,4,10])
     print(result)

                       
