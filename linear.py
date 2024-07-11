n=int(input())
nums=list(map(int, input().split()))[:n]
target=int(input())
position=-1
for i in range(len(nums)):
    if nums[i]==target:
        position=i
        break
if position==-1:
    print("target not found")
else:
    print("target is found",position)