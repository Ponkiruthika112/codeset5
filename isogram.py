#isogram
s=input()
l=[]
for i in s:
	l.append(s.count(i))
if max(l)>1:
	print("no")
else:
	print("yes")
