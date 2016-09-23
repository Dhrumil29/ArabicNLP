import codecs
s="مع"
s= 'مع'
t='مع'
print(s==t)
print(s)
print(type(s))
s.encode('utf-8')
print(s)
print(type(s))
#unicode(s, encoding='utf-8')
print(type(s))
file1name = codecs.open('final.txt', 'r', encoding="utf-8")
output1file = file1name.readlines()
ranks_nl_stopwords=[]
for line in output1file:
    ranks_nl_stopwords.append(line)
if s in ranks_nl_stopwords:
    print("found")
else:
    print("not found")
