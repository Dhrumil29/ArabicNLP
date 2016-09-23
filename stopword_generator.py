import codecs
file1name = codecs.open('1.txt', 'r', encoding="utf-8")
output1file = file1name.readlines()
ranks_nl_stopwords=[]
for line in output1file:
    ranks_nl_stopwords.append(line)
    #print(line)
print(len(ranks_nl_stopwords))
file2name = codecs.open('2.txt', 'r', encoding="utf-8")
output2file = file2name.readlines()
translated_stopwords=[]
for line in output2file:
    translated_stopwords.append(line)
    #print(line)
print(len(translated_stopwords))
file3name = codecs.open('3.txt', 'r', encoding="utf-8")
output3file = file3name.readlines()
github_stopwords=[]
for line in output3file:
    github_stopwords.append(line)
    #print(line)
print(len(github_stopwords))
file4name = codecs.open('stopwords.txt', 'r', encoding="utf-8")
output4file = file4name.readlines()
github_another_stopwords=[]
for line in output4file:
    github_another_stopwords.append(line)
    #print(line)
print(len(github_another_stopwords))
a=[2,3,5]
b=[1,2,3]
b.append(a)
print(b)
stopwords_1 = [val for val in github_stopwords if val in ranks_nl_stopwords]
stopwords_2 = [val for val in github_another_stopwords if val in github_stopwords]
stopwords_3 = [val for val in github_another_stopwords if val in ranks_nl_stopwords]
stopwords_4 = [val for val in stopwords_1 if val in stopwords_2]
stopwords_5=list(set(stopwords_4 + stopwords_3))
print(len(stopwords_1))
print(len(stopwords_2))
print(len(stopwords_3))
print(len(stopwords_4))
print(len(stopwords_5))
print(stopwords_5)

with codecs.open("final.txt", "w", encoding="utf-8") as f:
    for i in stopwords_5:
        f.write(i)
