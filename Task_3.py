#Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#*Пример:* 
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def addpoly(p1,p2):
    i=0
    su=0
    j=0
    c=[]
    
    if len(p1)==0:
    #if p1 empty
        return p2
    if len(p2)==0:
    #if p2 is empty
        return p1

    while i<len(p1) and j<len(p2):
        if int(p1[i][1])==int(p2[j][1]):
            su=p1[i][0]+p2[j][0]
        if su !=0:
            c.append((su,p1[i][1]))
        i=i+1
        j=j+1
        if p1[i][1]>p2[j][1]:
            c.append((p1[i]))
        i=i+1
        if p1[i][1]<p2[j][1]:
            c.append((p2[j]))
        j=j+1
    if p1[i:]!=[]:
        for k in p1[i:]:
            c.append(k)
    if p2[j:]!=[]:
        for k in p2[j:]:
            c.append(k)
    return c