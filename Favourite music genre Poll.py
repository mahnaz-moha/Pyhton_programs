total_genres=["Horror", "Romance", "Comedy", "History" , "Adventure" , "Action"]
Horror_num=Romance_num=Comedy_num=History_num=Adventure_num=Action_num=0
firstgenre=secondgenre=thirdgenre=forthgenre=fifthgenre=sixthgenre=str
firstgenre_num=secondgenre_num=thirdgenre_num=forthgenre_num=fifthgenre_num=sixthgenre_num=0
lst=[]
counter=dict()
num=int(input(""))
for i in range (1,num+1):
    vorudyi=input("")
    vorudy_s=vorudyi.split()
    name=vorudy_s[0]
    chosen_genres=vorudy_s[1:]
    if vorudy_s[1]=="Horror":
        Horror_num+=1
    #print("Horror : %i"%Horror_num)
    elif vorudy_s[1]=="Romance":
        Romance_num+=1
    elif vorudy_s[1]=="Comedy":
        Comedy_num+=1
    elif vorudy_s[1]=="History":
        History_num+=1
    elif vorudy_s[1]=="Adventure":
        Adventure_num+=1
    elif vorudy_s[1]=="Action":
        Action_num+=1
    if vorudy_s[2]=="Horror":
        Horror_num+=1
    if vorudy_s[2]=="Romance":
        Romance_num+=1
    if vorudy_s[2]=="Comedy":
        Comedy_num+=1
    if vorudy_s[2]=="History":
        History_num+=1
    if vorudy_s[2]=="Adventure":
        Adventure_num+=1
    if vorudy_s[2]=="Action":
        Action_num+=1
    if vorudy_s[3]=="Horror":
        Horror_num+=1
    #print("Horror : %i"%Horror_num)
    if vorudy_s[3]=="Romance":
        Romance_num+=1
    if vorudy_s[3]=="Comedy":
        Comedy_num+=1
    if vorudy_s[3]=="History":
        History_num+=1
    if vorudy_s[3]=="Adventure":
        Adventure_num+=1
    if vorudy_s[3]=="Action":
        Action_num+=1
for letter in lst:
    counter[letter]=counter.get(letter,0)+1
counter={"Action":Action_num,"Adventure":Adventure_num,"Comedy":Comedy_num,"History":History_num,"Horror":Horror_num,"Romance":Romance_num}
for this_one in sorted(counter,key=counter.get,reverse=True):
       print(this_one,":",counter[(this_one)])







