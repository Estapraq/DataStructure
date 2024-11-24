class Tuple:
	'''
	students=('sami', 'huda', 'nada')
    thisTuple = ("apple", "apple", "banana", "cherry", True, 1, 2.7. 'c')
	properties: 
	  - Ordered (i.e has index)
	  - Allow duplicates 
	  - Immutable (i.e you can NOT use any method that modify the tuple structure)
	    Note: to add/remove/update elements using methods would require
	     to cast the tuple to list first
	  - The tuple values can be a mix of different data types
	''' 

	#Operations:
	#Create
	names=()
	fruit=tuple()
	print(names, fruit)

	#Add  - thisTuple=tuple(('item1','item2'))
	names=('sarah','ali')
	fruit=tuple(('apple','orange'))

	#Casting
	names_list=list(names)
	#Add items by using methods
	print(names_list)
	names_list.append('huda')
	#print(names_list)

	#Update
	#names[0]='huda'
	names_list[0]='huda'
	#print('names_list:', names_list)

	#Read
	#print('names:', names)
	#print(names[0])

	#for name in names:
	#	print(name)

	#Delete
	#print('names_list:', names_list)
	#print('names:', names)
	names_list.remove('ali')
	#print('names_list:', names_list)

	names=tuple(names_list)
	#print('recasting names:', names)

	#Functions and Mehtods
	#type() and dir() function
	#print(type(names))
	#print(type(names_list))

	#print(dir(names))
	#print(dir(names_list))

	#Concatinate tuples using +
	classNames=('nada','fatma')
	allNames=classNames+names
	#print(allNames)

	#Len() and Count() method
	#print(len(allNames))
	#print(allNames.count('huda'))


	#Slicing [inclusive:exclusive]
	#print('allNames:', allNames)
	#print(allNames[:])
	#print(allNames[1:3])

	#Packing/Unpacking - for unpacking we MUST have the same numbers of values 
	#                     on both sides to map the values
	person=('ahmed', 54, 162)
	(name,age,height)=('ahmed',54,162)
	print(name)
	print(age)
	(name,age,*height)=('ahmed',54,162, 'brown')
	print(height)




