class Set:
	'''
	students={'sami', 'huda', 'nada'}
    thisset = {"apple", "banana", "cherry", True, 1, 2}
	properties: 
	  - Unorder (i.e no index)
	  - Don't allow duplicates 
	  - Mutable (because you can add/remove elements, but you can't update the values)
	  - The values can be a mix of different data types
	'''

	#Operations:
	#Create
	color={}
	print(color)
	fruit=set()
	print(fruit)
	#Add - Note:thisset = set(("apple", "banana", "cherry"))
	color={'red','yellow'}
	print(color)
	fruit=set(('mango','apple'))
	print(fruit)
	color.add('black')
	print(color)

	#Read
	for item in color:
		print(item)

	#Update
	color={'green', 'blue'}
	print(color)

	#Delete using discard() and remove() methods
	#color.discard('blue')
	#print(color)
	#fruit.remove('mango')
	#Mathematical operations - intersection(), union(), issubset(), &, |
	print(fruit)
	basket={'mango','orange'}
	print(basket)
	print(fruit.intersection(basket))
	print(fruit.union(basket))
	print(fruit)
	print(basket)
	basket &= fruit
	print(basket)
	#Methods and Functions
	#dir() function
	print(dir(basket))

	#False and 0 is considered the same values in sets
	numbers={2}
	numbers.add(True)
	print(numbers)
	numbers.add(False)
	print(numbers)

	#Len(), Type()
	print(len(numbers))

	#frozenset() method
	frozenset(basket)

	#casting
	name="esta"
	print(list(name))

