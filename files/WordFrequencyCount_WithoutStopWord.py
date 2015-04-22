from collections import Counter

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

file_paths = open('/home/user/Videos/athi.txt') 
stopWords = ['a','after','all','am','and','any','are','as','at','but','can','for','from','get','if',
	'in','than','that','the','this','to', 'is']
wordList = file_paths.read().split()
word = removeStopwords(wordList,stopWords)
list= Counter(word).most_common()
print list

