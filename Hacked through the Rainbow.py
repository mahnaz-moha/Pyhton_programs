import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    rainbow_dict = {} #generating hashlib data base
    for i in range(1000, 10000): # note you need upper end to be 10000 in odrder to include 9999
        my_hash = hashlib.sha256(str(i).encode()).hexdigest()
        rainbow_dict[my_hash] = i
    with open(input_file_name, mode='r') as csv_in:
        csv_content = csv.reader(csv_in)
        with open(output_file_name, 'w', newline='') as csv_out:
            csv_writer = csv.writer(csv_out)
            name=list()
            pas=dict()
            for row in csv_content:
                name=row[0]
                vall=row[1]
                pas[name]=vall
            for x,y in pas.items():
                pas_new=rainbow_dict[y]
                #print('%s, %i' %(x,pas_new))
                csv_writer.writerow([x,pas_new])

#hash_password_hack('source.csv', 'passwrod.csv')
    


