countries=["Iran","Morocco", "Portugal", "Spain"]
iran_win=spain_win=iran_draw=spain_draw=spain_point=iran_point=team1_draws=team1_points=team1_win=0
spain_goal=iran_goal=iran_loses=spain_loses=goal_diff=team1_goal_diff=team1_loses=0
team1=team2=team3=team4=str
portugal_goal=portugal_win=portugal_draw=portugal_point=portugal_loses=portugal_goal_diff=0
morocco_goal=morocco_win=morocco_draw=morocco_point=morocco_loses=morocco_goal_diff=0
iran_goal_khorde=spain_goal_khorde=portugal_goal_khorde=morocco_goal_khorde=0
iran_goal_zade_total=iran_goal_khorde_total=0
spain_goal_khorde_total=portugal_goal_khorde_total=morocco_goal_khorde_total=0
spain_goal_zade_total=portugal_goal_zade_total=morocco_goal_zade_total=0
iran_goal_diff=spain_goal_diff=portugal_goal_diff=morocco_goal_diff=0
team2_win=team3_win=team4_win=0
team2_draws=team3_draws=team4_draws=0
team2_goal_diff=team3_goal_diff=team4_goal_diff=0
team2_loses=team3_loses=team4_loses=0
team2_points=team3_points=team4_points=0
for i in range (1, 7):
    resulti=input("")
    if i<=3:
        iran_goal=int(resulti[0])
        iran_goal_khorde=int(resulti[2])
        iran_goal_zade_total=iran_goal+iran_goal_zade_total
        iran_goal_khorde_total=iran_goal_khorde+iran_goal_khorde_total
        iran_goal_diff=iran_goal_zade_total-iran_goal_khorde_total
        if int(resulti[0])>int(resulti[2]):
            iran_win+=1
        if int(resulti[0])==int(resulti[2]):
            iran_draw+=1
        if int(resulti[0])<int(resulti[2]):
            iran_loses+=1
    if i ==1:
        spain_goal=int(resulti[2])
        spain_goal_khorde=int(resulti[0])
        spain_goal_zade_total=spain_goal+spain_goal_zade_total
        spain_goal_khorde_total=spain_goal_khorde+spain_goal_khorde_total
        if int(resulti[0])<int(resulti[2]):
            spain_win+=1
        if int(resulti[0])==int(resulti[2]):
            spain_draw+=1
        if int(resulti[0])>int(resulti[2]):
            spain_loses+=1

    if 4<=i<=5:
        spain_goal=int(resulti[0])
        spain_goal_khorde=int(resulti[2])
        spain_goal_zade_total=spain_goal+spain_goal_zade_total
        spain_goal_khorde_total=spain_goal_khorde+spain_goal_khorde_total
        spain_goal_diff=spain_goal_zade_total-spain_goal_khorde_total
        if int(resulti[0])>int(resulti[2]):
            spain_win+=1
        if int(resulti[0])==int(resulti[2]):
            spain_draw+=1
        if int(resulti[0])<int(resulti[2]):
            spain_loses+=1
    if (i==2) or (i==4):
        portugal_goal=int(resulti[2])
        portugal_goal_khorde=int(resulti[0])
        portugal_goal_zade_total=portugal_goal+portugal_goal_zade_total
        portugal_goal_khorde_total=portugal_goal_khorde+portugal_goal_khorde_total
        if int(resulti[0])<int(resulti[2]):
            portugal_win+=1
        if int(resulti[0])==int(resulti[2]):
            portugal_draw+=1
        if int(resulti[0])>int(resulti[2]):
            portugal_loses+=1
    if i==6:
        portugal_goal=int(resulti[0])
        portugal_goal_khorde=int(resulti[2])
        portugal_goal_zade_total=portugal_goal+portugal_goal_zade_total
        portugal_goal_khorde_total=portugal_goal_khorde+portugal_goal_khorde_total
        portugal_goal_diff=portugal_goal_zade_total-portugal_goal_khorde_total
        if int(resulti[0])>int(resulti[2]):
            portugal_win+=1
        if int(resulti[0])==int(resulti[2]):
            portugal_draw+=1
        if int(resulti[0])<int(resulti[2]):
            portugal_loses+=1
    if (i==3) or(i==5) or (i==6):
        morocco_goal=int(resulti[2])
        morocco_goal_khorde=int(resulti[0])
        morocco_goal_zade_total=morocco_goal+morocco_goal_zade_total
        morocco_goal_khorde_total=morocco_goal_khorde+morocco_goal_khorde_total
        morocco_goal_diff=morocco_goal_zade_total-morocco_goal_khorde_total
        if int(resulti[0])<int(resulti[2]):
            morocco_win+=1
        if int(resulti[0])==int(resulti[2]):
            morocco_draw+=1
        if int(resulti[0])>int(resulti[2]):
            morocco_loses+=1
spain_point=3*spain_win+spain_draw
iran_point=3*iran_win+iran_draw
portugal_point=3*portugal_win+portugal_draw
morocco_point=3*morocco_win+morocco_draw
if ((iran_point>morocco_point) or ((iran_point==morocco_point) and(iran_win>=morocco_win)))  and ((iran_point>portugal_point) or ((iran_point==portugal_point) and (iran_win>=portugal_win))) and ((iran_point>spain_point) or ((iran_point==spain_point) and (iran_win>=spain_win))):
    team1="Iran"
    team1_win=iran_win 
    team1_draws=iran_draw 
    team1_points=iran_point
    team1_loses=iran_loses
    team1_goal_diff=iran_goal_diff
    if ((morocco_point>portugal_point) or ((morocco_point==portugal_point) and (morocco_win>=portugal_win))) and ((morocco_point>spain_point)or ((morocco_point==spain_point) and (morocco_win>=spain_win))):
        team2="Morocco"
        team2_win=morocco_win 
        team2_draws=morocco_draw 
        team2_points=morocco_point
        team2_loses=morocco_loses
        team2_goal_diff=morocco_goal_diff
        if ((portugal_point>spain_point) or ((portugal_point==spain_point) and (portugal_win>=spain_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((portugal_point<spain_point) or ((portugal_point==spain_point) and (portugal_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
    elif ((portugal_point>morocco_point) or ((morocco_point==portugal_point) and (morocco_win<portugal_win))) and ((portugal_point>spain_point)or ((portugal_point==spain_point) and (portugal_win>=spain_win))):
        team2="Portugal"
        team2_win=portugal_win 
        team2_draws=portugal_draw 
        team2_points=portugal_point
        team2_loses=portugal_loses
        team2_goal_diff=portugal_goal_diff
        if ((morocco_point>spain_point) or ((morocco_point==spain_point) and (morocco_win>=spain_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((morocco_point<spain_point) or ((morocco_point==spain_point) and (morocco_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
    elif ((spain_point>morocco_point) or ((morocco_point==spain_point) and (morocco_win<spain_win))) and ((portugal_point<spain_point)or ((portugal_point==spain_point) and (portugal_win<spain_win))):
        team2="Spain"
        team2_win=spain_win 
        team2_draws=spain_draw 
        team2_points=spain_point
        team2_loses=spain_loses
        team2_goal_diff=spain_goal_diff
        if ((morocco_point>portugal_point) or ((morocco_point==portugal_point) and (morocco_win>=portugal_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
        elif ((morocco_point<portugal_point) or ((morocco_point==portugal_point) and (morocco_win<portugal_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
if ((morocco_point>iran_point) or ((iran_point==morocco_point) and(iran_win<morocco_win)))  and ((morocco_point>portugal_point) or ((morocco_point==portugal_point) and (morocco_win>=portugal_win))) and ((morocco_point>spain_point) or ((morocco_point==spain_point) and (morocco_win>=spain_win))):
    team1="Morocco"
    team1_win=morocco_win 
    team1_draws=morocco_draw
    team1_points=morocco_point
    team1_loses=morocco_loses
    team1_goal_diff=morocco_goal_diff
    if ((iran_point>portugal_point) or ((iran_point==portugal_point) and (iran_win>=portugal_win))) and ((iran_point>spain_point)or ((iran_point==spain_point) and (iran_win>=spain_win))):
        team2="Iran"
        team2_win=iran_win 
        team2_draws=iran_draw 
        team2_points=iran_point
        team2_loses=iran_loses
        team2_goal_diff=iran_goal_diff
        if ((portugal_point>spain_point) or ((portugal_point==spain_point) and (portugal_win>=spain_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((portugal_point<spain_point) or ((portugal_point==spain_point) and (portugal_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
    elif ((iran_point<portugal_point) or ((iran_point==portugal_point) and (iran_win<portugal_win))) and ((portugal_point>spain_point)or ((portugal_point==spain_point) and (portugal_win>=spain_win))):
        team2="Portugal"
        team2_win=portugal_win 
        team2_draws=portugal_draw 
        team2_points=portugal_point
        team2_loses=portugal_loses
        team2_goal_diff=portugal_goal_diff
        if ((iran_point>spain_point) or ((iran_point==spain_point) and (iran_win>=spain_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((iran_point<spain_point) or ((iran_point==spain_point) and (iran_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
    elif ((iran_point<spain_point) or ((iran_point==spain_point) and (iran_win<spain_win))) and ((portugal_point<spain_point)or ((portugal_point==spain_point) and (portugal_win<spain_win))):
        team2="Spain"
        team2_win=spain_win 
        team2_draws=spain_draw 
        team2_points=spain_point
        team2_loses=spain_loses
        team2_goal_diff=spain_goal_diff
        if ((iran_point>spain_point) or ((iran_point==spain_point) and (iran_win>=spain_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
        elif ((iran_point<portugal_point) or ((iran_point==portugal_point) and (iran_win<portugal_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
if ((portugal_point>iran_point) or ((iran_point==portugal_point) and(iran_win<portugal_win)))  and ((morocco_point<portugal_point) or ((morocco_point==portugal_point) and (morocco_win<portugal_win))) and ((portugal_point>spain_point) or ((iran_point==spain_point) and (portugal_win>=spain_win))):
    team1="Portugal"
    team1_win=portugal_win 
    team1_draws=portugal_draw
    team1_points=portugal_point
    team1_loses=portugal_loses
    team1_goal_diff=portugal_goal_diff
    if ((iran_point>morocco_point) or ((iran_point==morocco_point) and (iran_win>=morocco_win))) and ((iran_point>spain_point)or ((iran_point==spain_point) and (iran_win>=spain_win))):
        team2="Iran"
        team2_win=iran_win 
        team2_draws=iran_draw 
        team2_points=iran_point
        team2_loses=iran_loses
        team2_goal_diff=iran_goal_diff
        if ((morocco_point>spain_point) or ((morocco_point==spain_point) and (morocco_win>=spain_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((morocco_point<spain_point) or ((morocco_point==spain_point) and (morocco_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
    elif ((iran_point<morocco_point) or ((iran_point==morocco_point) and (iran_win<morocco_win))) and ((morocco_point>spain_point)or ((morocco_point==spain_point) and (morocco_win>=spain_win))):
        team2="Morocco"
        team2_win=morocco_win 
        team2_draws=morocco_draw 
        team2_points=morocco_point
        team2_loses=morocco_loses
        team2_goal_diff=morocco_goal_diff
        if ((iran_point>spain_point) or ((iran_point==spain_point) and (iran_win>=spain_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Spain"
            team4_win=spain_win 
            team4_draws=spain_draw 
            team4_points=spain_point
            team4_loses=spain_loses
            team4_goal_diff=spain_goal_diff
        elif ((iran_point<spain_point) or ((iran_point==spain_point) and (iran_win<spain_win))):
            team3="Spain"
            team3_win=spain_win 
            team3_draws=spain_draw 
            team3_points=spain_point
            team3_loses=spain_loses
            team3_goal_diff=spain_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
    elif ((iran_point<spain_point) or ((iran_point==spain_point) and (iran_win<spain_win))) and ((morocco_point<spain_point)or ((morocco_point==spain_point) and (morocco_win<spain_win))):
        team2="Spain"
        team2_win=spain_win 
        team2_draws=spain_draw 
        team2_points=spain_point
        team2_loses=spain_loses
        team2_goal_diff=spain_goal_diff
        if ((iran_point>morocco_point) or ((iran_point==morocco_point) and (iran_win>=morocco_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
        elif ((iran_point<morocco_point) or ((iran_point==morocco_point) and (iran_win<morocco_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
if ((spain_point>iran_point) or ((iran_point==spain_point) and(iran_win<spain_win)))  and ((morocco_point<spain_point) or ((morocco_point==spain_point) and (morocco_win<spain_win))) and ((portugal_point<spain_point) or ((iran_point==spain_point) and (portugal_win<spain_win))):
    team1="Spain"
    team1_win=spain_win 
    team1_draws=spain_draw
    team1_points=spain_point
    team1_loses=spain_loses
    team1_goal_diff=spain_goal_diff
    if ((iran_point>morocco_point) or ((iran_point==morocco_point) and (iran_win>=morocco_win))) and ((iran_point>portugal_point)or ((iran_point==portugal_point) and (iran_win>=portugal_win))):
        team2="Iran"
        team2_win=iran_win 
        team2_draws=iran_draw 
        team2_points=iran_point
        team2_loses=iran_loses
        team2_goal_diff=iran_goal_diff
        if ((morocco_point>portugal_point) or ((morocco_point==portugal_point) and (morocco_win>=portugal_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
        elif ((morocco_point<portugal_point) or ((morocco_point==portugal_point) and (morocco_win<portugal_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
    elif ((iran_point<morocco_point) or ((iran_point==morocco_point) and (iran_win<morocco_win))) and ((morocco_point>portugal_point)or ((morocco_point==portugal_point) and (morocco_win>=portugal_win))):
        team2="Morocco"
        team2_win=morocco_win 
        team2_draws=morocco_draw 
        team2_points=morocco_point
        team2_loses=morocco_loses
        team2_goal_diff=morocco_goal_diff
        if ((iran_point>portugal_point) or ((iran_point==portugal_point) and (iran_win>=portugal_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Portugal"
            team4_win=portugal_win 
            team4_draws=portugal_draw 
            team4_points=portugal_point
            team4_loses=portugal_loses
            team4_goal_diff=portugal_goal_diff
        elif ((iran_point<portugal_point) or ((iran_point==portugal_point) and (iran_win<portugal_win))):
            team3="Portugal"
            team3_win=portugal_win 
            team3_draws=portugal_draw 
            team3_points=portugal_point
            team3_loses=portugal_loses
            team3_goal_diff=portugal_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
    elif ((iran_point<portugal_point) or ((iran_point==portugal_point) and (iran_win<portugal_win))) and ((morocco_point<portugal_point)or ((morocco_point==portugal_point) and (morocco_win<portugal_win))):
        team2="Portugal"
        team2_win=portugal_win 
        team2_draws=portugal_draw 
        team2_points=portugal_point
        team2_loses=portugal_loses
        team2_goal_diff=portugal_goal_diff
        if ((iran_point>morocco_point) or ((iran_point==morocco_point) and (iran_win>=morocco_win))):
            team3="Iran"
            team3_win=iran_win 
            team3_draws=iran_draw 
            team3_points=iran_point
            team3_loses=iran_loses
            team3_goal_diff=iran_goal_diff
            team4="Morocco"
            team4_win=morocco_win 
            team4_draws=morocco_draw 
            team4_points=morocco_point
            team4_loses=morocco_loses
            team4_goal_diff=morocco_goal_diff
        elif ((iran_point<morocco_point) or ((iran_point==morocco_point) and (iran_win<morocco_win))):
            team3="Morocco"
            team3_win=morocco_win 
            team3_draws=morocco_draw 
            team3_points=morocco_point
            team3_loses=morocco_loses
            team3_goal_diff=morocco_goal_diff
            team4="Iran"
            team4_win=iran_win 
            team4_draws=iran_draw 
            team4_points=iran_point
            team4_loses=iran_loses
            team4_goal_diff=iran_goal_diff
print(team1,"wins:",team1_win,",","loses:",team1_loses,",","draws:",team1_draws,",","goal difference:",team1_goal_diff,",""points:",team1_points)
print(team2,"wins:",team2_win,",","loses:",team2_loses,",","draws:",team2_draws,",","goal difference:",team2_goal_diff,",","points:",team2_points)
print(team3,"wins:",team3_win,",","loses:",team3_loses,",","draws:",team3_draws,",","goal difference:",team3_goal_diff,",","points:",team3_points)
print(team4,"wins:",team4_win,",","loses:",team4_loses,",","draws:",team4_draws,",","goal difference:",team4_goal_diff,",","points:",team4_points)



            










            






