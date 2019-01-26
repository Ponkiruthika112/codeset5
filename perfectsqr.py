#this is my code
import math
n,m=map(int,input().split())
k=n*m
p=int(math.sqrt(k))
if k==p*p:
	print("yes")
else:
	print("no")
