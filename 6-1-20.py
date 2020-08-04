#Linear Search%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

li=[2,4,5,7,8,9,1]
a=6
f=search(li,a)
print("Element found at index:",f)
print("Element found at position:",f+1)'''


#BINARY SEARCH --USING RecurtiOn%%%%%%%%%%%%%%%%%%%%%

'''def BinarySearch(arr,l,r,x):
    if r>=l:
        mid = l+(r-l)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BinarySearch(arr,l,mid-1,x)
        else:
            return BinarySearch(arr,mid+1,r,x)
    else:
        return -1
arr = [2,3,4,10,40]
x=50
result=BinarySearch(arr,0,len(arr)-1,x)

if result!=-1:
    print("Element is present at index %d"%result)
else:
    print("Element is mot present in array")'''

#Binary Search using Iteration%%%%%%%%%%%%%%%%%%%%%%


'''def binarySearch(arr,l,r,x):
    while l <=r:
         mid = l+(r-l)//2
         if arr[mid]==x:
             print(mid)
         elif arr[mid]<x:
             l=mid+1
         else:
             r=mid-1
    return -1

arr = [10,20,30,40,50,60,70,80,90]
x=90
result = binarySearch(arr,0,len(arr)-1,x)
print(result)'''

#SORTING TECHNIQUES
#Bubble Sort++++++++++++

'''def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr =[64,34,25,12,22,11,90]
print(bubbleSort(arr))'''


#Selection Sort+++++++++++++++

'''A = [64,25,12,22,11]
for i in range(len(A)):
    min_ind=i
    #print(min_ind)
    for j in range(i+1,len(A)):#iteration1 i=0 & j=1,2,3,4
        print("i=",i,'j=',j)
        if A[min_ind]>A[j]:
            min_ind = j
            #print(min_ind)
    A[i],A[min_ind]=A[min_ind],A[i]

print("Sorted Array")
for i in range(len(A)):
    print("%d"%A[i])'''

#REGULER EXPRESSION
#re using Search
'''import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

if (x):
    print("Yes! We have a match!")
else:
    print("No Match")'''
#re using findall()
'''import re
str = "The rain in Spain"
x = re.findall("ai",str)
print(x)'''

#exp re using search
'''import re
str = "The Rain in Spain"
#x = re.findall("\s",str)
x = re.search("\s",str)
print("The First white sapce occurence at position:",x.start())'''
       
#re using split()

'''import re
str = "The rain in Spain"
x = re.split("\s",str,1)
print(x)'''
#mcq&&&&&&&&&&&&&&&&&
'''class Sales:
    def __init__(self,id):
        self.id = id
        id=100
val = Sales(123)
print(val.id)'''

#re using sub

'''import re
txt = "The rain in Spain"
x = re.sub("\s","-",txt)
print(x)'''

#exm%%%%%%%%%%%

'''import re
txt = "The rain in Spain"
x = re.findall('\bain',txt)
if (x):
    print("The Word found")
else:
    print("Not Found")'''


'''import re
txt = "The rain in Spain"
x = re.findall(r'ain\b',txt)
if (x):
    print("Yes! word Found")
else:
    print("Not Found")'''

#where in last occurence of letter 'e' when only search b/n 5 and 10

'''import re
txt = "Hello, Welcome to my world"
x = txt.rfind("e",5,10)
print(x)'''

#Renoving the Duplicate Charecters in given String

def dup(a):
    #x =set()    
    l=[]
    for i in a:
        if i not in l:
           #x.add(i)
           l.append(i)
    return ''.join(l)
a = '11222@@@333444888###'
print(dup(a))
        


































































