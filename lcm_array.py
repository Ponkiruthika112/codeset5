# your code goes here
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
def cal_lcm(a,b):
	k=gcd(a,b)
	return (a*b)//k
l=list(map(int,input().split()))
a=l[0]
b=l[1]
lcm=cal_lcm(a,b)
for i in range(2,len(l)):
	lcm=cal_lcm(lcm,l[i])
print(lcm)
#array
