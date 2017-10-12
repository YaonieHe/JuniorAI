from copy import deepcopy

class Eight_figure():  #八数码类
	def __init__(self):
		self.start=[[1,2,3],[4,0,5],[6,7,8]] 
		self.end=[[1,2,3],[4,5,6],[7,8,0]]
		self.nownull=[1,1]
		self.now=deepcopy(self.start)
		self.havegone=[]
		self.willgone=[]
		
	
	def h(self,a):  #选择使用哪个启发式函数
		return self.h2(a)
	def h1(self,a):  #第一种启发式函数
		n=0
		for i in range(len(a)):
			for j in range(len(a[i])):
				if a[i][j]!=self.end[i][j] and a[i][j]!=0:
					n+=1
		return n

	def h2(self,a):  #第二种启发式函数
		n=0
		for i in range(len(a)):
			for j in range(len(a[i])):
				locate=[[l,k] for l in range(len(a)) for k in \
				range(len(a[0])) 	if self.end[l][k] == a[i][j]][0]	
				if a[i][j]!=0:
					n=n+abs(i-locate[0])+abs(j-locate[1])
		return n
			
	def set_start(self,a):  #设置初始状态
		self.start=deepcopy(a)
		return
	
	def set_end(self,a): #设置最终状态
		self.end=deepcopy(a)
		return
	
	def set_null(self):  #获取当前状态的八数码空格位置
		for i in range(len(self.now)):
			for j in range(len(self.now[0])):
				if self.now[i][j]==0:
					self.nownull=[i,j]
					return

	def next_status(self): #获得当前状态的所以后继
		ns=[]
		na=self.nownull
		for i in [[1,0],[-1,0],[0,1],[0,-1]]:
			if 0<=na[0]+i[0]<3 and 0<=na[1]+i[1]<3 :
				nw=deepcopy(self.now)
				nw[na[0]][na[1]]=nw[na[0]+i[0]][na[1]+i[1]]
				nw[na[0]+i[0]][na[1]+i[1]]=0
				ns.append(nw)
		return ns

	def get_load(self): #求出从初始状态到最终状态的路径
		self.willgone=[]
		self.havegone=[]
		self.willgone.append([self.start,self.start,self.h(self.start)])
		while len(self.willgone)>0 and self.end != self.now:
			minwg = min(self.willgone,key =lambda x: x[2])
			self.willgone.remove(minwg)
			self.now=minwg[0]
			self.set_null()
			free = minwg[2]-self.h(self.now)+1
			nsa=self.next_status()
			hg=[s[0] for s in self.havegone]
			wg = [s[0] for s in self.willgone]
			for ns in nsa:
				if ns in hg:
					continue
				else:
					fns = self.h(ns)+free
					if ns not in wg:
						self.willgone.append([ns,self.now,fns])
					else:
						prefns = [s for s in self.willgone if s[0]==ns][0]
						if prefns[2]>fns:
							prefns[2]=fns
							prefns[1]=self.now
			self.havegone.append(minwg)
		return
	
	def print_load(self):  #输出路径
		hg = [s[0] for s in self.havegone]
		if self.end not in hg:
			print("have no load")
			return
		load=[]
		nw=self.end
		while self.start not in load:
			hnw = [s for s in self.havegone if s[0] == nw][0]
			load.append(nw)
			nw=hnw[1]
		n = len(load)
		load=load[::-1]
		print("step : ",n-1)
		nd5=n//5
		for i in range(nd5):  #每行输出5步 
			for j in range(len(load[0])):
				for l in range(i*5,i*5+5):
					print(load[l][j],end="")
					if j==len(load[0])//2 and l!=n-1:
						print("-->",end="")
					else:
						print("   ",end="")
				print("")
		if n%5!=0:
			for j in range(len(load[0])):
				for l in range(nd5*5,n):
					print(load[l][j],end="")
					if j==len(load[0])//2 and l!=n-1:
						print("-->",end="")
					else:
						print("   ",end="")
				print("")

		return
					

if __name__ =="__main__":
	ef=Eight_figure()
#测试样例：
#	ef.set_start([[1,2,3],[4,0,5],[6,7,8]])
#	ef.set_end([[1,2,3],[0,4,5],[6,7,8]])
#	ef.set_start([[1,2,3],[4,0,5],[6,7,8]])
#	ef.set_end([[2,0,3],[1,4,5],[6,7,8]])
	ef.set_start([[7,2,4],[5,0,6],[8,3,1]])
	ef.set_end([[0,1,2],[3,4,5],[6,7,8]])
	ef.get_load()
	ef.print_load()







