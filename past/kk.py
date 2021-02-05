
x=list(range(15))
x=x[-1]+1
w=5
inc=2
listx=[]
final=[]
    
L=0
R=L+w
while R<=x:
    for i in range(L,R):
        listx.append(i)
    
    L= R-1-inc
    R=L+w
    final.append(listx)
    listx=[]
    print(final)

