import re
import numpy as np

with open('sentences.txt') as text:
	content = text.read()
content = content.lower()
#content.replace("'", "")

words = re.findall(r'[a-z]+', content)

word_dict = {}
for word in words:
	if word not in word_dict:
		word_dict[word] = len(word_dict)
d = max(i for i in word_dict.values())

with open('sentences.txt') as text:
	sentences = text.readlines()

i = 0
for sen in sentences:
	sentences[i] = sentences[i].lower()
	sentences[i] = re.sub(r"['-?,.!\n]", '', sentences[i])
	i += 1
print sentences
#for value in word_dict.values():
#	i = 0
