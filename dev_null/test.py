#23.04.17: leanring reg.expressions

import re

mytext = " Vasu aaaaaa 1934, Kolya 1234 mail@mail.ru, aaaa@intel.com, "\
		"bbbb@intel.com, Petya gggg, 1222, cccccc@yahoo.com, "\
		"vladimir@yandex.ru, 1238, Fargo, vlodes@gmail.com, 1993"

"""
\d any digit 0-9
\D any nonDigit

\w any alphabet symbol [A-Z, a-z]
\W any nonAlphabet symbols

\s any breakspace
\S any nonBreakspace



"""
"""text_for_search = r"\d\d\d" #look for any 3 digits in a row
result = re.findall(text_for_search, mytext)
print result

text_for_search = r"[0-9]{3}" #the same as above
result = re.findall(text_for_search, mytext)
print result


text_for_search = r"[A-Z][a-z]+" #all names
result = re.findall(text_for_search, mytext)
print result

text_for_search = r"\w+[.]\w+" #all domains
result = re.findall(text_for_search, mytext)
print result
"""
def m(r,s):
	match = re.match(r,s)
	if match:
		print match.group()
	return "Nope!"

m('....', mytext)