import re

re_word = re.compile('\w+')

line = input()
raw_words = line.replace('_', ' ')
words = re_word.findall(raw_words)
res = [x.capitalize() for x in words[1:]]
print(words[0].lower() + ''.join(res))
