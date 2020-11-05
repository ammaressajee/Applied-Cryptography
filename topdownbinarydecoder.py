import sys
        
col_num = 2
col_data = []
delimiter = " " 
with open('infection.txt') as f:
    col_data.append(f.readline().split(delimiter)[col_num])

print(f[0])
