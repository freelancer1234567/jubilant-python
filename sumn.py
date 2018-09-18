#sum
k,l=input().split()
n=list(map(int, input().split()))
l=int(l)
sum=0
for i in range (l):
    sum=sum+n[i]
print(sum)
