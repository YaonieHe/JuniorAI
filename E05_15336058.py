from copy import deepcopy

def terminal(a):
	for i in range(3):
		if a[0][i]==a[1][i]==a[2][i]=='#':
			return 1
		if a[i][0]==a[i][1]==a[i][2]=='#':
			return 1
		if a[0][i]==a[1][i]==a[2][i]=='*':
			return -1
		if a[i][0]==a[i][1]==a[i][2]=='*':
			return -1
	for i in [-1,1]:
		if a[0][i+1]==a[1][1]==a[2][1-i]=='#':
			return 1
		if a[0][i+1]==a[1][1]==a[2][1-i]=='*':
			return -1
	for i in range(3):
		for j in range(3):
			if a[i][j]==' ':
				return 2
	return 0

def nextload(chess,player,alpha,beta):
	value=terminal(chess)
	if value!=2:
		return [-1,-1,value]
	allnex=[[i,j] for i in range(3) for j in range(3) if chess[i][j]==' ']
#	print(allnex)
	nex=[0,0]
	if player==1:
		for x in allnex:
			newchess=deepcopy(chess)
			newchess[x[0]][x[1]]='#'
			subvalue=nextload(newchess,-1,alpha,beta)
			if subvalue[2]>alpha:
				nex[0]=x[0]
				nex[1]=x[1]
				alpha=subvalue[2]
			if beta<=alpha:
				break
		return [nex[0],nex[1],alpha]
	else:
		for x in allnex:
			newchess=deepcopy(chess)
			newchess[x[0]][x[1]]='*'
			subvalue=nextload(newchess,1,alpha,beta)
			if subvalue[2]<beta:
				nex[0]=x[0]
				nex[1]=x[1]
				beta=subvalue[2]
			if beta<=alpha:
				break
		return [nex[0],nex[1],beta]
	
def printf(a):
	for i in range(3):
		print(' -- -- -- ')
		for j in range(3):
			print('|',a[i][j],end='')
		print('|')
	print(' -- -- -- ')

if __name__ == '__main__':
	chess=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	alpha=-2
	beta=2
	player=1
	name=['blue',' ','red']
	while terminal(chess)==2:
		print('player: ',name[player+1])
		nex=nextload(chess,player,alpha,beta)
		if player==1:
			chess[nex[0]][nex[1]]='#'
		else:
			chess[nex[0]][nex[1]]='*'
		printf(chess)
		player=-player
	
	print('player: ' ,name[player])
	if player==1:
		chess[nex[0]][nex[1]]='#'
	else:
		chess[nex[0]][nex[1]]='*'
	printf(chess)
	winner=['winner: bule','draw','winner: red']
	print(winner[terminal(chess)+1])
