def find_bigrams(input_list):
	return zip(input_list, input_list[1:])

def find_tigrams(input_list):
	return zip(input_list, input_list[1:], input_list[2:])

file_path = open('/home/prodapt/Documents/documentation of tasks.txt') 
word = file_path.read().split()

bigrams = find_bigrams(word)
tigrams = find_tigrams(word)
print bigrams
print tigrams