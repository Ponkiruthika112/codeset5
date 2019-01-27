#sum of the all nos
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
	s=s+l[i]
print(s)
