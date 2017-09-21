def h(now,end):
	a=0
	b=0
	for i in range(len(now)):
		if now[i]<end[i]:
			a+=1
		elif now[i]>end[i]:
			b+=1
	return max(a,b)

print("please enter the number of tests:")
m=int(input())
while m !=0:
	m-=1
	print("input the number of caps: ")
	n=int(input())
	print("input the capacity of two caps:")
	caps=input().split()
	caps=[int(i) for i in caps]
	print("input the fnally water in caps:")
	end=input().split()
	end=[int(i) for i in end]

	on=[]
	close=[]
	pre=[]
	start=[0]*n
	on.append([start,h(start,end)])
	pre.append([start,start])
	while len(on)>0 :
		lwater = min(on,key=lambda x:x[1])
		on.remove(lwater)
		now=lwater[0]
		if now == end:
			break
		fn = lwater[1]-h(now,end)
		close.append(now)
		allnex=[]
		for i in range(n):
			if now[i]<caps[i]:
				nex=now[0:i]+[caps[i]]+now[i+1:]
				allnex.append(nex)

			if now[i]>0:
				nex=now[0:i]+[0]+now[i+1:]
				allnex.append(nex)
				
				for j in range(i):
					if now[j]<caps[j]:
						pour=min(now[i],caps[j]-now[j])
						nex=now[0:j]+[now[j]+pour]+now[j+1:i]+[now[i]-pour]+now[i+1:]
						allnex.append(nex)	
				
				for j in range(i+1,n):
					if now[j]<caps[j]:
						pour=min(now[i],caps[j]-now[j])
						nex=now[0:i]+[now[i]-pour]+now[i+1:j]+[now[j]+pour]+now[j+1:]
						allnex.append(nex)
		
		
		for nex in allnex:
			value=fn+1+h(nex,end)
			if nex in [s[0] for s in on]:
				ll=[s for s in on if s[0]==nex][0]
				if(value<ll[1]):
					ll[1]=value
					lll = [s for s in pre if s[0]==nex][0]
					lll[1]=now
			elif nex not in close:
				on.append([nex,value])
				pre.append([nex,now])
	if end in [s[0] for s in pre]:
		load=[]
		now = end
		while start not in  load:
			load.append(now)
			now = [s[1] for s in pre if s[0]==now][0]
		print("Minimum stps:",len(load)-1)
		for i in range(1,len(load)):
			print(load[len(load)-i],"-->",end='')
		print(load[0])
	else :
		print("Impossible!")


