import re

with open('sentences.txt') as text:
	content = text.read()
words = re.findall(r'[a-z]+', content)


print(words)