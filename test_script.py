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
print d