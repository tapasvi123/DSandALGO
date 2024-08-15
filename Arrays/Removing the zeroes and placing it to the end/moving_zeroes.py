arr=[0,0,0,1,0,12,4,5,0,3,0,12,0]
i=0
j=0

def swap(i, j):
    temp=0
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    
while(j<(len(arr)) and i <len(arr)):
    # print("i",arr[i])
    # print("j",arr[j])
    if arr[i]!=0:
         i+=1
         j+=1
    else:
        if arr[j]==0:
            j+=1  
        else:
            swap(i,j)
            
        
print(arr)
# [0,1,0,3,0,4,5]
# [0,1,3,0,0,4,5]
# [0,1,3,4,5,0,0]
