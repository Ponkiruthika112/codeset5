def sort(s):
	p=list(s)
	p.sort()
	y="".join(p)
	return y
c=0
	
n=int(input())
s="kabali"
d=sort(s)
for i in range(0,n):
	k=input()
	f=sort(k)
	if d==f:
		c=c+1
print(c)
#anagram
