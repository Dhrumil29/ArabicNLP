import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import codecs
s="مع"
s= 'مع'
t='مع'
p='فان'
q='فان'
file1name = codecs.open('arabic_text.txt', 'r', encoding="utf-8")
output1file = file1name.readlines()
string=[]
for s in output1file:
    string.append(s)
# print(string)
# print(string[0])
str=string[0].split(" ")
print(str)
s.encode('utf-8')
#q.encode('utf-8')
#unicode(s, encoding='utf-8')
file1name = codecs.open('final.txt', 'r', encoding="utf-8")
output1file = file1name.readlines()
stopwords=[]
for line in output1file:
    stopwords.append(line)
#print(string)
file2name = codecs.open('negative_words.txt', 'r', encoding="utf-8")
output2file = file2name.readlines()
neg_words=[]
for line in output2file:
    neg_words.append(line)
#print(string)
file3name = codecs.open('positive_words.txt', 'r', encoding="utf-8")
output3file = file3name.readlines()
pos_words=[]
for line in output3file:
    pos_words.append(line)
#print(string)
pos_word=[]
neg_word = []
stopword = []
normal_words = []
for i in range(0,len(pos_words)):
    pos_words[i]=pos_words[i][:-4]
for i in range(0,len(neg_words)):
    neg_words[i]=neg_words[i][:-4]
for i in range(0,len(stopwords)):
    stopwords[i]=stopwords[i][:-4]

for i in range(0,len(string)):
    str=string[i].split(" ")
    print(len(str))
    pos_word.append(0)
    neg_word.append(0)
    stopword.append(0)
    normal_words.append(0)
    for j in range(0,len(str)):
        #print(str[j])
        if (str[j] in pos_words):
            pos_word[i]=pos_word[i]+1
        elif (str[j] in neg_words):
            neg_word[i] = neg_word[i] + 1
        elif (str[j] in stopwords):
            stopword[i] = stopword[i]+1
        else:
            normal_words[i]=normal_words[i]+1
    print(pos_word[i],neg_word[i],stopword[i],normal_words[i])
pos_score=[]
neg_score=[]
for i in range(0,len(pos_word)):
    pos_score.append(0)
    neg_score.append(0)
    pos_score[i]=(pos_word[i]/(pos_word[i]+neg_word[i]+normal_words[i]))*100
    pos_score[i] = pos_score[i]-(stopword[i]/(pos_word[i]+neg_word[i]+normal_words[i]))*50
    if(pos_score[i]<0):
        pos_score[i]=0
    neg_score[i]=(neg_word [i]/(pos_word[i]+neg_word[i]+normal_words[i]))*100
    neg_score[i] = neg_score[i] - (stopword[i] / (pos_word[i] + neg_word[i] + normal_words[i])) * 50
    if (neg_score[i] < 0):
        neg_score[i] = 0
# import numpy as np
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# ## the data
#
# ## necessary variables
# ind=range(0,len(pos_word))     # the x locations for the groups
# width = 0.35                      # the width of the bars
#
# ## the bars
# rects1 = ax.bar(range(0,len(pos_word)),stopword,width,
#                 color='black')
#
# rects2 = ax.bar(range(0,len(neg_word)), neg_word, width,
#                     color='red')
#
# ## add a legend
# ax.legend( (rects1[0], rects2[0]), ('Men', 'Women') )
#
# plt.show()
#
# Setting the positions and width for the bars
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 4

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, pos_score, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Positivity')

rects2 = plt.bar(index + bar_width, neg_score, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Negativity')

plt.xlabel('Comments')
plt.ylabel('Score')
plt.title('Comment Score')
plt.xticks(index + bar_width, ('cmt1', 'cmt2', 'cmt3','cmt4','cmt5','cmt6','cmt7'))
plt.legend()

plt.tight_layout()
plt.show()
