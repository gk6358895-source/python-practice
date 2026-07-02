arr=[1,2,4,5,6]
k=3
even_count=0
for i in arr[:k]:
    if i%2==0:
        even_count+=1
        
print(even_count) 
            


for i in range(k,len(arr)):
    if  arr[i-k]%2==0:
        even_count-=1
    if arr[i]%2==0:
        even_count+=1

   

    print(even_count)
