n=int(input())
nums=list(map(int, input().split()))[:n]
target=int(input())
nums=sorted(nums)
left,right=0,len(nums)-1
found = False
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
if found == True:
    print("target found",mid)
else:
    print("target not found")