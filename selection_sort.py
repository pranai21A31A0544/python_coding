n=int(input())
nums=list(map(int, input().split()))[:n]
def Selectionsort(nums):
    pos=n-1
    while pos>0:
        maxnum=pos
        for i in range(0,pos-1):
            if nums[maxnum]<nums[i]:
                maxnum=i
        if maxnum!=pos:
            temp=nums[maxnum]
            nums[maxnum]=nums[pos]
            nums[pos]=temp
        pos-=1 
Selectionsort(nums)
print("aftersorting",nums)