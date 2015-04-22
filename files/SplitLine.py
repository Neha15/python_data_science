def word_count():
	file_paths = open('/home/prodapt/Documents/documentation of tasks.txt') 
	list = []
	for word in file_paths.read().split():
		print(word)
		list.append(word)

	print len(list)


word_count()