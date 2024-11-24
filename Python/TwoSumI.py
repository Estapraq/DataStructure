#Youtube channel @TechWithEsta
class ArrayTwoSumI:
     '''   
      Two Sum I
      ----------
      Given an array of integers, return indices of two 
      numbers such that they add up to a specific target.

      You may assume that one input would have exactly
      one solution, and you may not use same element twice. 

     '''

     def TwoSums(nums:list[int],target: int)->list[int]:
         prevMap={} # value:i
         for i, value in enumerate(nums):
            diff=target-value
            if diff in prevMap:
               return [prevMap[diff], i]
            prevMap[value]=i


     result=TwoSums([2,3,4],6)
     print(result)



        

       
    



