# your code goes here
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)

l=list(map(int,input().split()))
a=l[0]
b=l[1]
g=gcd(a,b)
for i in range(2,len(l)):
	g=gcd(g,l[i])
print(g)
#gcd_array
