#My youtube channel is @TechWithEsta
class Dictionary:
     '''
      Sami="405-666-2345",
      Huda="406-776-2245",
      Sara="501-686-2445"
    '''
    #Operations
	#creating a dictionary
     Age={}
     print(Age)
     Height = dict()
     print(Height)
	#Adding Key-Values pairs
     Age={'sara':72, "ali":17}
     print(Age)
     Height = dict(sara=162, ali= 163)
     print(Height)
     Age['huda']=16
     print(Age)
     Height['huda'] = 159
     print(Height)
	#Read data
     print(Height['sara'])
     print(Age['sara'])
    #Update values (keys are immutable and values are mutable)
     Age['sara']=62
     print(Age)
   
	#Delete values
     del(Age['sara'])
     print(Age)
     Height.pop('sara')
     print(Height)
     #del(Age)

    #Functions 
	#values(), keys(), and items() functions
     print(Age.values())
     print(Age.keys())
     print(Age.items())

	#length function len()
     print(len(Age))
     print(len(Height))
    #Type function
     type(Age)
    #In operator
     print('ali' in Age)
     print('sara' in Age)
    #Casting
     dict(Age)
     print(Age)
     #List(Age)

	#for loop
     for key in Age.keys():
     	print(key)

      





     







    
