import csv, xlsxwriter
wyshworkbook = xlsxwriter.Workbook("change.xlsx")
wyshsheet = wyshworkbook.add_worksheet()
lst=[]
with open("telgu_tv_stars.csv") as f:
    lines=list(f.readlines())
    for i in lines[1::]:
        lst.append(list(i.split(','))[-1])
print(lst)
lst2=[]
for i in lst:
    i=i.strip('\n"')
    lst2.append(i)
print(lst2)
# #---------for addition to excel file-------------------
wyshsheet.write(0,0,'Name')
for item in range(len(lst2)):
    wyshsheet.write(item+1,0,lst2[item])
wyshworkbook.close()