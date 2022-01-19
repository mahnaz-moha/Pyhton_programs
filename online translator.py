number_word=int(input(""))
counter=dict()
counter_keys=[]
counter_value=[]
for i in range(0,number_word):
    word_meaning=input("")
    word_meaning=word_meaning.split()
    counter_keys.append(word_meaning[0])
    counter_value.append(word_meaning[1])
    #print(counter_keys,counter_value)
    counter[counter_keys[i]]=counter_value[i]
    
#print(counter)    
sentence=input("")
lst=sentence.split()
#print(lst)
lst1=[]
for letter in lst:
    if letter in counter:
        letter=counter[letter]
        #print(letter)
    #else:
        #print(letter)
    lst1.append(letter)
lst1=" ".join(lst1)
print(lst1)
        

        
    




