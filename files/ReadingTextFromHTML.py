import urllib 
import re

def cleanhtml(raw_html):
	cleanr =re.compile(r'<[^>]+>')

	cleantext = re.sub(cleanr,'', raw_html)

	return cleantext

url = "https://docs.python.org/2/tutorial/"
html = urllib.urlopen(url).read()
print cleanhtml(html)

