import re
import numpy as np
from scipy.spatial import distance

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
word_list = sorted(word_dict.items(), key=lambda x: x[1])


with open('sentences.txt') as text:
	sentences = text.readlines()

i = 0
y = 0 
string = np.eye(22,254)
for sen in sentences:
	sentences[i] = sentences[i].lower()
	sentences[i] = re.sub(r"['-?,.!\n]", '', sentences[i])
	for j in range(254):
		count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word_list[j][0]), sentences[i]))
		string[i][j] = count
	i += 1

dist = {}
for x in range(22):
	dist[x] = distance.cosine(string[0], string[x])
dist = sorted(dist.items(), key=lambda x: x[1])
print dist

#6 and 4