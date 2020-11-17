import xlrd
import xlsxwriter

def indexofMinabs(arr):
    minindex = 0
    currentindex = 1
    while currentindex < len(arr):
        if abs(arr[currentindex]) < abs(arr[minindex]):
            minindex = currentindex
        currentindex += 1
    return minindex

Rpath = r'C:\Users\Ray\Desktop\实验\数据\830mm-强轴-轴压比0.1\horizon.xlsx'
Wpath = r'C:\Users\Ray\Desktop\实验\数据\830mm-强轴-轴压比0.1\dispart_old.xlsx'
roun = 26
origin = xlrd.open_workbook(Rpath)
table = origin.sheets()[0]
F = table.col_values(2)
D = table.col_values(3)
t = table.col_values(1)
T_li = []
T_t_o = table.col_values(4)
T_t = T_t_o[0:roun]
for tran in T_t:
    i = 0
    T_mined = []
    for time in t:
        T_mined.append(time - tran)
        i=i+1
    T_li.append(indexofMinabs(T_mined))

workbook = xlsxwriter.Workbook(Wpath)
worksheet_1 = workbook.add_worksheet('F')
worksheet_2 = workbook.add_worksheet('D')
worksheet_1.write_row('A1',F[0:T_li[0]])
worksheet_2.write_row('A1',D[0:T_li[0]])

for i in list(range(2,roun+1)):
    print('running NO.' + str(i) + ' row')
    place = 'A' + str(i) 
    worksheet_1.write_row(place,F[T_li[i-2]:T_li[i-1]])
    worksheet_2.write_row(place,D[T_li[i-2]:T_li[i-1]])
    
worksheet_1.write_row('A31',F[T_li[len(T_li)-1]:len(F)-1])
worksheet_2.write_row('A31',D[T_li[len(T_li)-1]:len(D)-1])
workbook.close()


    
 