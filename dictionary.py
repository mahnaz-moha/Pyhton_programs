number_word=int(input(""))
english_counter=dict()
french_counter=dict()
germany_counter=dict()
counter_keys_english=[]
counter_keys_french=[]
counter_keys_germany=[]
counter_value=[]
for i in range(0,number_word):
    word_meaning=input("")
    word=word_meaning.split()[:1]
    word_meaning=word_meaning.split()[1:]
    #print(word)
    #print(word_meaning)
    counter_keys_english.append(word_meaning[0])
    counter_keys_french.append(word_meaning[1])
    counter_keys_germany.append(word_meaning[2])
    counter_value.append(word[0])
    #print(counter_keys,counter_value)
    english_counter[counter_keys_english[i]]=counter_value[i]
    french_counter[counter_keys_french[i]]=counter_value[i]
    germany_counter[counter_keys_germany[i]]=counter_value[i]
    #print(counter_keys_english,counter_value)
    #print(counter_keys_french,counter_value)
    #print(counter_keys_germany,counter_value)
    
sentence=input("")
lst=sentence.split()

lst1=[]
for letter in lst:
    if letter in english_counter:
        letter=english_counter[letter]
    elif letter in french_counter:
        letter=french_counter[letter]
    elif letter in germany_counter:
        letter=germany_counter[letter]
       
    lst1.append(letter)
    #print(lst1)
lst1=" ".join(lst1)
print(lst1)
        

        
    




