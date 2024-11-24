#Youtube channel @TechWithEsta
class solution:
     '''   
      Valid Parentheses                         
      --------------------------------
      Given a string s containing jut the characters 
      '(', ')', '{', '}', '[', and ']', determine
      if the input string is valid.

      An input string is valid if: 
      1- Open brackets must be closed by the same typr of brakets. 
      2- Open brackets must be closed in the correct order


      Ex: 
      Input: s="()"
      Output: true 

      Ex:
      Tnput: s="()[]{}"
      Output: true 

      Ex:
      ([)]
      false the reason is the  order 
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

                       
