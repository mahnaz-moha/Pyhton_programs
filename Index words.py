string=input("")
sentences = string.replace(",","").split(".")
word=string.replace(",","").replace(".","").split(" ")
#print(word)
a=[]
for i in range(0,len(sentences)):
    #vocab=sentences[i].strip().split(" ")[1:]
    sentences1=sentences[i].strip().split(" ")[1:]
    #print(sentences1)
    sentences2=" ".join(sentences1)
    a.append(sentences2)
#print(a)
a1=" ".join(a)
#print(a1)
vocab=a1.split(" ") 
#print(vocab)
b=[]
for i in range(0,len(vocab)):
    if vocab[i].istitle():
        b.append(vocab[i])
#print(b)

if len(b)==0:
    print("None")
else: 
    for i in range(0,len(b)):
        print("%s:%s" %(word.index(b[i])+1,b[i]))
        word[word.index(b[i])]="man"
       
    







