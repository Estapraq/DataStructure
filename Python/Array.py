#Follow My youtube channel @TechWithEsta
class Array:
     import array as arr
     import numpy as np
     
     '''   
     array=[5,6,9,9,5]  

     properties:
       - Homogeneous data: All array memeber has same data type
       - Ordered: every element has an index
       - Allow duplicates, values can be duplicated
     '''

    #Operations: Create, Add, Update, Delete 
     ''' 
        Array can be created using: 
       - List built-in Data Structure: 
       - Import Python Array Model
       - Import Python library NumPY
	 to create a string data type array by using array model, you 
                          will nee to cast, for example: arr.array('u', u'hello \u2641')'''
     array_usingList = [1,2,4]
     array_usingList.append(4)
     array_usingList.remove(4)
     array_usingList[0]=11
     #print(array_usingList)

     array_usingModel = arr.array('u', ['c','v','k'])
     #array_usingModelString = arr.array('u', u'hello \u2641')
     array_usingModel.append('c')
     array_usingModel.remove('c')
     array_usingModel[1]='m'
     #print(array_usingModel)

     array_usingNP = np.array((4,5))
     result = np.append(array_usingNP, 4)
     remove_element = np.delete(result, 2)
     remove_element[0] = 12
     print(result)
     print(remove_element)


     '''  
        BigO: 
        -best: O(1) when insert/Remove at the end of the array 
        -worst: O(n) when insert/Remove at the begining of the array '''
        

       
    



