from tamil import utf8
from collections import Counter
import csv
import sys
import re
f=open(sys.argv[1], "r")
if f.mode == 'r':
 contents =f.read()
words = contents.split()
words_list= []
#print(words)
for word in words:
 regex = re.compile('[!a-zA-Z0-9<>,.?"=\.\\\/\-\_\+\~\`@:?\)\(\*\%\#\!]')
 c = regex.sub('', word)
 words_list.append(c)
words1 = [i for i in words_list if i]
w_c = Counter(words1)
book = sys.argv[1]
print("Generating count of words and letters for book {}".format(book))
print("*"*100)
most_com_word = w_c.most_common()
most_com_words = []
for i in most_com_word:
 list_con = list(i)
 list_con.append(book)
 most_com_words.append(list_con)
letter_list = []
for word in words1:
 word_1 = utf8.get_letters(word)
 for letter in word_1:
   letter_list.append(letter)
print(letter_list)
l_c = Counter(letter_list)
most_com_letters = l_c.most_common()
print("*"*100)
print("*"*100)

print("Generating two csv with above output")

f = open(book+"_words.csv", "w")
writer = csv.DictWriter(f, fieldnames=["words", "count","book"])
writer.writeheader()
f.close()
with open(book+"_words.csv","a")  as f:
    writer=csv.writer(f, delimiter=",", lineterminator="\r\n",) 
    writer.writerows(most_com_words)

f = open(book+"_letters.csv", "w")
writer = csv.DictWriter(f, fieldnames=["letters", "count"])
writer.writeheader()
f.close()
with open(book+"_letters.csv","a")  as f:
    writer=csv.writer(f, delimiter=",", lineterminator="\r\n",) 
    writer.writerows(most_com_letters)

print("Generated words.csv and letters.csv filw with most common used words and letters in ascending order")

