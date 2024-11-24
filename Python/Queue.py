class Queue:
	'''
	customers=['sami', 'huda', 'nada', 'Ali']
	properties: 
	  - First-In-First-Out i.e FIFO
	  - three operations has to be preformed with O(1) 
	     Pop - removing the back (rear) element
	     append - adding element to the end
	     peak - return the back element  
	''' 
	students=['sami', 'huda', 'nada', 'Ali']
	students.append('sam')
	print(students)
	students.pop()
	print(students)
	print(students[-1])
	students.remove(students[0])
	print([students])
	students.insert(0,'don')
	print(students)
