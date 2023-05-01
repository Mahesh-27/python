
def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]

    
a=[2,6,5,7,4,3]
bubblesort(a)
print(a)   
    
        