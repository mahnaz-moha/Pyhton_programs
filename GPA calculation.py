import csv
# For the average
from statistics import mean
from operator import itemgetter

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            esm=list()
            moadel=dict()
            for row in csv_content:
                name=row[0]
                vals=[float(val) for val in row[1:]]
                ave=mean(vals)
                moadel[name]=ave
                #print('%s,%2.18f' %(name,ave))
                #csv_writer.writerow([row[0],mean(vals)])
            # print(moadel)
            # find persons with the same moadel
            fliped={}
            for key,value in moadel.items(): 
                if value not in fliped:
                    fliped[value]=[key]
                else:
                    fliped[value].append(key)
            #print(fliped)
            tekrari=[]
            for key, value in fliped.items():
                if len(value)>1:
                    tekrari.extend(value)
            #print(tekrari)
            tekrari_2=tuple() # same as tekrari to avoid missing any names
            tekrari_2=tuple(tekrari)
            tekrari.sort()
            #print(tekrari)
            for x,y in moadel.items():
                if x in tekrari_2:
                    esm=tekrari.pop(0)
                else:
                    esm=x              
                print('%s,%2.15f' %(esm,y))
                csv_writer.writerow([esm,y])   
                #print(tekrari)
                #print(tekrari_2)        
#calculate_averages('source.csv','averages.csv')
        
    
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            moadel=dict()
            sorted_averages=dict()
            for row in csv_content:
                name=row[0]
                vals=[float(val) for val in row[1:]]
                ave=mean(vals)
                moadel[name]= ave
            sorted_averages= sorted(moadel.items(), key=itemgetter(1))
            # print(sorted_averages)
            fliped={}
            for key, value in sorted_averages:
                if value not in fliped:
                    fliped[value]=[key]
                else:
                    fliped[value].append(key)
            #print(fliped)
            tekrari=list()
            for key, value in fliped.items():
                if len(value)>1:
                    tekrari.extend(value)
            tekrari_2=tuple(tekrari)
            tekrari.sort()
            #print(tekrari)
            #print(tekrari_2)
            for x,y in sorted_averages:
                if x in tekrari_2:
                    esm=tekrari.pop(0)
                else:
                    esm=x
                print('%s %2.15f' %(esm,y))
                csv_writer.writerow([esm,y])
#calculate_sorted_averages('source.csv','output sorted.csv')
    


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            moadel=dict()
            sorted_averages=dict()
            for row in csv_content:
                name=row[0]
                vals=[float(val) for val in row[1:]]
                ave=mean(vals)
                moadel[name]= ave
            sorted_averages= sorted(moadel.items(), key=itemgetter(1))
            #print(sorted_averages)
            fliped={}
            for key, value in sorted_averages:
                if value not in fliped:
                    fliped[value]=[key]
                else:
                    fliped[value].append(key)
            #print(fliped)
            tekrari=list()
            for key, value in fliped.items():
                if len(value)>1:
                    tekrari.extend(value)
            tekrari_2=tuple(tekrari)
            tekrari.sort()
            #print(tekrari)
            #print(tekrari_2)
            for i in range(3):
                if sorted_averages[-1-i][0] in tekrari_2:
                    esm=tekrari.pop(0)
                    val= sorted_averages[-1-i][1]
                else:
                    esm= sorted_averages[-1-i][0]
                    val= sorted_averages[-1-i][1]
                print('%s %2.15f' %(esm,val))
                csv_writer.writerow([esm,val])
#calculate_three_best('source.csv','three_best.csv')



def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            moadel=dict()
            sorted_averages=dict()
            for row in csv_content:
                name=row[0]
                vals=[float(val) for val in row[1:]]
                ave=mean(vals)
                moadel[name]= ave
            sorted_averages= sorted(moadel.items(), key=itemgetter(1))
            #print(sorted_averages)
            fliped={}
            for key, value in sorted_averages:
                if value not in fliped:
                    fliped[value]=[key]
                else:
                    fliped[value].append(key)
            #print(fliped)
            tekrari=list()
            for key, value in fliped.items():
                if len(value)>1:
                    tekrari.extend(value)
            tekrari_2=tuple(tekrari)
            tekrari.sort()
            #print(tekrari)
            #print(tekrari_2)
            for i in range(3):
                if sorted_averages[i][0] in tekrari_2:
                    esm=tekrari.pop(0)
                    val= sorted_averages[i][1]
                else:
                    esm= sorted_averages[i][0]
                    val= sorted_averages[i][1]
                print('%2.15f' %(val))
                csv_writer.writerow([val])
#calculate_three_worst('source.csv','three_worst.csv')


def calculate_average_of_averages(input_file_name, output_file_name):   
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            moadel=dict()
            moadels=list() # list of all moadels
            for row in csv_content:
                name=row[0]
                vals=[float(val) for val in row[1:]]
                ave=mean(vals)
                moadel[name]= ave
                moadels.append(ave)
            print(mean(moadels  ))
            csv_writer.writerow([mean(moadels)])
#calculate_average_of_averages('source.csv','total_averages.csv') 