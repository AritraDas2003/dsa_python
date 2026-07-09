from array import *  
def LinearSearch(a,n,s):  
    for i in range(0,n):
        if(a[i]==s):            
             return i    
    return -1  
a=array('i',[]) 
n=int(input("Enter how many elements:")) 
for i in range(n):     
    x=int(input("Enter Data:"))     
    a.append(x)  
    
s=int(input("Enter data which you want to search:"))  
pos=LinearSearch(a,n,s)  
if(pos>=0):     
    print("Data found in",pos+1,"th position") 
else:     
    print("Data Not Found") 