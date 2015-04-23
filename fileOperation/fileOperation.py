
import csv
import sys
import urllib 
import json 
import re
from collections import Counter

def open_file():
	file_content = open(sys.argv[1])
	return file_content

#Counting lines in a text file
def file_count(content):
	num_lines = sum(1 for line in content if line.rstrip('\n'))
	print num_lines

#Splitting a line into words and counting words
def word_count(content):
 	list = []
 	for word in content:
 		print(word)
 		list.append(word)
 	print len(list)

#Calculating word frequencies from a text file
def word_freq(content):
	print Counter(content).most_common()

def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

#Calculating word frequencies after eliminating stop words
def freq_count(content):
	stopWords = ['a','after','all','am','and','any','are','as','at','but','can','for','from','get','if',
		'in','than','that','the','this','to', 'is']
	word = removeStopwords(content,stopWords) #Calling removeStopWords helper function
	list= Counter(word).most_common()
	print list

#bigrams
def find_bigrams(content):
	bigram = zip(content, content[1:])
	print bigram

#trigram
def find_tigrams(content):	
	trigram = zip(content, content[1:], content[2:])
	print trigram

#reading html
def read_html():
	url = "https://docs.python.org/2/tutorial/"
	html = urllib.urlopen(url).read() 
	#removing html tags and attributes
	cleanr =re.compile(r'<[^>]+>') 
	cleantext = re.sub(cleanr,'', html)
	print cleantext

#reading json file
def read_json():
	file_path = open(sys.argv[2]) 
	data = json.load(file_path)
	jsondata = json.dumps(data, sort_keys=True, indent=4)
	print jsondata
	
#Reading the csv File
def read_csv_file():
	file = open(sys.argv[3], 'rt')
	reader = csv.reader(file)
	for row in reader:
		print row

#Writing the csv FIle
def write_csv_file():
	file = open(sys.argv[3], 'wt')
	writer = csv.writer(file)
	writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
	for i in range(10):
		writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )


file = open_file()
file_count(file)

filecontent = open_file()
content = filecontent.read().split()
word_count(content)
word_freq(content)
freq_count(content)
find_bigrams(content)
find_tigrams(content)
read_html()
read_json()
write_csv_file()
read_csv_file()





