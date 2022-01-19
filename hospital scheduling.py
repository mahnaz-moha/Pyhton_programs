from random import expovariate
from math import inf 
from statistics import mean


Avg_IAT = 1.0                      # Average Inter-Arrival Time
Avg_ST = 0.5                       # Average Service Time
Tot_ST = 480.0                     # Total Simulation Time
Current_ST = 0.0                   # Current Simulation Time
Last_Event_Time = 0.0              # Time of last event

N = 0                               # State variable; number of customers in the system
Arr_Time = expovariate(1.0/Avg_IAT) # Time of the next arrival event
Dep_Time = inf                 # Time of the next departure event


# Output Variables
Arr_Time_Data = []   # Collect arrival times
Dep_Time_Data = []   # Collect departure times
Waiting_Data = []    # Collect waiting time of individual packets
q_custome_num = []   # collect number of customers in the queue
Serve_Time_Data=[]   # collect server working time

while Current_ST <= Tot_ST:
    if Arr_Time < Dep_Time:                      # Arrival Event
        Current_ST = Arr_Time
        rectangle_Height = (Current_ST - Last_Event_Time) * (N-1)
        if rectangle_Height < 0:
          rectangle_Height =0
        q_custome_num.append(rectangle_Height)            # Area of rectangle
        Last_Event_Time = Current_ST
        Arr_Time_Data.append(Current_ST)              # save Arrival Time
        N = N + 1.0
        Arr_Time = Current_ST + expovariate(1.0/Avg_IAT)
        if N == 1:
          service_time = expovariate(1.0/Avg_ST)
          Serve_Time_Data.append(service_time)   # to save s erver working time
          Dep_Time = Current_ST + service_time
    else: # Departure Event
        Current_ST = Dep_Time
        rectangle_Height = (Current_ST - Last_Event_Time) * (N-1)
        if rectangle_Height < 0:
          rectangle_Height =0
        q_custome_num.append(rectangle_Height)             # Area of rectangle
        Last_Event_Time = Current_ST
        Dep_Time_Data.append(Current_ST)
        N = N - 1.0
        if N > 0:
            service_time = expovariate(1.0/Avg_ST)
            Serve_Time_Data.append(service_time) # to save server working time
            Dep_Time = Current_ST + service_time
        else:
            Dep_Time = inf

## Calculate Dalay for each individual packets
for i in range(len(Dep_Time_Data)):
    d = (Dep_Time_Data[i] - Arr_Time_Data[i])-Serve_Time_Data[i]
    Waiting_Data.append(d)

print( "Average Waiting in Queue = ", round( mean(Waiting_Data), 4))
print( "Server Utilization Percentage = ", (round( (sum( Serve_Time_Data)/Current_ST), 4))*100)
print( "Average number of customers in the queue  = ", round(sum(q_custome_num) / Current_ST, 4) )
print("the number of customers who get service =",len(Dep_Time_Data))