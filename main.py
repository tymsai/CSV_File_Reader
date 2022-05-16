#%%
#CSV reader
import csv
with open('csvfile.csv', 'r+') as f:
    mock_data_reader=csv.reader(f)
    line_count=1
    users=[]
    for row in mock_data_reader:
        if line_count>1:
            SNo= row[0]
            Name= [1]
            Object= [2]
            users.append({'SNo':row[1], 'Name':row[2], 'Object':row[3]})
            break
        line_count+=1
print(users)
