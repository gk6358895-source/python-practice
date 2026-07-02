arr=[2,1,5,1,3,2]
k=3
window_sum=sum(arr[:k])
window_avg=sum(arr[:k])/k
max_avg=window_avg

for i in range(k,len(arr)):
    window_sum+=((window_sum+arr[i])-arr[i-k])
    window_avg=window_sum/k
    max_avg=max(max_avg,window_avg)

print(max_avg)   

