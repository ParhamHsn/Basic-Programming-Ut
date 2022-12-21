file = open("input.txt")
action = []
for line in file:
	action.append(line.strip())
print(action)

x = 0
y = len(action)







import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((6 * 50, 50 * 12))

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))






mat = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(14):
	for j in range(6):
		mat[i].append(0)


#n = 4 , WARNING : THIS VARIABLE MUST BE FROM 3 UP TO 8

color_m1 = action[0][0]
color_m2 = action[0][1]
color_m3 = action[0][2]


mat[0][2] = color_m1
mat[1][2] = color_m2
mat[2][2] = color_m3

sabz =  0
ghermez = 1
abi = 2

z = 1
stop = 0

idx = 0 #Left Or Right

score = 0


def tek():
	global color_m1,color_m2,color_m3,mat,sabz,ghermez,abi,idx,inter,pygame,n,running
	color_m1 = random.randint(1,n)
	color_m2 = random.randint(1,n)
	color_m3 = random.randint(1,n)
	if mat[2][2] == 0:
		mat[0][2] = color_m1
		mat[1][2] = color_m2
		mat[2][2] = color_m3
		idx = 0
	else:
		if 0 not in mat[2]:
			running = False
		else:
			rnd = random.randint(0,5)
			while(mat[2][rnd] != 0):
				rnd = random.randint(0,5)
			mat[0][rnd] = color_m1
			mat[1][rnd] = color_m2
			mat[2][rnd] = color_m3
			idx = rnd - 2
	sabz =  0
	ghermez = 1
	abi = 2
	inter = 1000

def check_delete(m):
	result = False

	for i in range(2,14):
		for j in range(6):
			if(m[i][j] != 0 and i<=11 and m[i][j] == m[i+1][j] and m[i+1][j] == m[i+2][j]):
				result = True
			if(m[i][j] != 0 and j<=3 and m[i][j] == m[i][j+1] and m[i][j+1] == m[i][j+2]):
				result = True
			if (m[i][j] != 0 and i<=11 and j<=3 and m[i][j] == m[i + 1][j + 1] and m[i + 1][j + 1] == m[i + 2][j + 2]):
				result = True
			if(m[i][j] != 0 and i>=4 and j<=3 and m[i][j] == m[i - 1][j + 1] and m[i - 1][j + 1] == m[i - 2][ j + 2]):
				result = True
	return result

def check_down(m):

	for i in range(2,14):
		for j in range(6):
			if(m[i][j] != 0 and i<=12 and m[i+1][j] == 0):
				return 1
	return 0

def delete(m):
	d = []
	global score
	k = 3
	for i in range(2,14):
		for j in range(6):
			if(m[i][j] != 0 and i<=11 and m[i][j] == m[i+1][j] and m[i+1][j] == m[i+2][j]):
				while(k + i <= 13 and m[i][j] == m[i + k][j]):
					d.append([i+k,j])
					k+=1
				d.append([i,j])
				d.append([i+1,j])
				d.append([i+2,j])
				score += k
				k = 3
			if(m[i][j] != 0 and j<=3 and m[i][j] == m[i][j+1] and m[i][j+1] == m[i][j+2]):
				while(k + j <= 5 and m[i][j] == m[i][j + k]):
					d.append([i,j+k])
					k+=1
				d.append([i,j])
				d.append([i,j+1])
				d.append([i,j+2])
				score += k
				k = 3
			if(m[i][j] != 0 and i<=11 and j<=3 and m[i][j] == m[i + 1][j + 1] and m[i + 1][j + 1] == m[i + 2][ j + 2]):
				while(i + k <=13 and k + j <= 5 and m[i][j] == m[i + k][j + k]):
					d.append([i+k,j+k])
					k += 1
				d.append([i,j])
				d.append([i+1,j+1])
				d.append([i+2,j+2])
				score += k
				k = 3
			if(m[i][j] != 0 and i<=11 and j>=2 and m[i][j] == m[i + 1][j - 1] and m[i + 1][j - 1] == m[i + 2][ j - 2]):
				while(i + k <=13 and k + j >= 4 and m[i][j] == m[i + k][j - k]):
					d.append([i+k,j-k])
					k += 1
				d.append([i,j])
				d.append([i+1,j-1])
				d.append([i+2,j-2])
				score += k
				k = 3
	res = []
	for i in d:
		if i not in res:
			res.append(i)
	for i in res:
		m[i[0]][i[1]] = 0
	return m

def down(m):


	for i in range(2,14):
		for j in range(6):
			if(m[i][j] != 0 and i<=12 and m[i+1][j] == 0):
				(m[i][j] , m[i+1][j]) = (m[i+1][j] , m[i][j])

	return m
def go_down():
	global mat,abi,ghermez,sabz,idx,z
	# if(abi<13 and ghermez<13 and sabz <13):
	# 	if(mat[abi + 1][2 + idx] != 0 and mat[ghermez + 1][2 + idx] != 0 and mat[sabz + 1][2 + idx] != 0):
	# 		while(check_delete(mat) == 1 or check_down(mat) == 1):
	# 			mat = delete(mat)
	# 			mat = down(mat)
	# 		z = 1


		#Go Down

	if(mat[abi + 1][2 + idx] == 0 and z != 1 and stop == 0):
		(mat[abi + 1][2 + idx] , mat[abi][2 + idx]) = (mat[abi][2 + idx] , mat[abi + 1][2 + idx])
		abi+=1
	if(mat[ghermez + 1][2 + idx] == 0 and z != 1 and stop == 0):
		(mat[ghermez + 1][2 + idx] , mat[ghermez][2 + idx]) = (mat[ghermez][2 + idx] , mat[ghermez + 1][2 + idx])
		ghermez+=1
	if(mat[sabz + 1][2 + idx] == 0 and z != 1 and stop == 0):
		(mat[sabz + 1][2 + idx] , mat[sabz][2 + idx]) = (mat[sabz][2 + idx] , mat[sabz + 1][2 + idx])
		sabz+=1

	#Check Not Finish Game

	if(abi < 13 and mat[abi + 1][2 + idx] != 0):
		if(sabz == 1 or sabz == 0):
			running = False
			print("Cant Place")

	z = 0
def draw():
	for i in range(2,14):
		for j in range(6):
			if(mat[i][j] != 0):
				if(mat[i][j] == 'A'):
					color=(0,255,0)
				elif(mat[i][j] == 'B'):
					color=(255,0,0)
				elif(mat[i][j] == 'C'):
					color=(0,0,255)
				elif(mat[i][j] == 'D'):
					color=(255,140,0)
				elif(mat[i][j] == 'E'):
					color=(255,0,255)
				elif(mat[i][j] == 'F'):
					color=(139,69,19)
				elif(mat[i][j] == 'G'):
					color=(255,255,0)
				elif(mat[i][j] == 'H'):
					color=(128,0,128)

				pygame.draw.rect(screen,(color),(j*50,(i-2)*50,50,50))
	pygame.display.flip()
	screen.blit(background, (0, 0))

x = 1

while(x < y):
	if action[x] == "Left":
		if(idx > -2):
			if(mat[abi][2 + idx - 1] == 0 and mat[ghermez][2 + idx - 1] == 0 and mat[sabz][2 + idx - 1] == 0):
				(mat[abi][2 + idx] , mat[abi][2 + idx - 1]) = (mat[abi][2 + idx - 1], mat[abi][2 + idx])
				(mat[sabz][2 + idx] , mat[sabz][2 + idx - 1]) = (mat[sabz][2 + idx - 1], mat[sabz][2 + idx])
				(mat[ghermez][2 + idx] , mat[ghermez][2 + idx - 1]) = (mat[ghermez][2 + idx - 1], mat[ghermez][2 + idx])
				idx += -1
			if(abi < 13 and mat[abi + 1][2 + idx] != 0):
				if(sabz == 1 or sabz == 0):
					running = False
					print("Cant Place")
	elif action[x] == "Right":
		if(idx < 3):
			if(mat[abi][2 + idx + 1] == 0 and mat[ghermez][2 + idx + 1] == 0 and mat[sabz][2 + idx + 1] == 0):
				(mat[abi][2 + idx] , mat[abi][2 + idx + 1]) = (mat[abi][2 + idx + 1], mat[abi][2 + idx])
				(mat[sabz][2 + idx] , mat[sabz][2 + idx + 1]) = (mat[sabz][2 + idx + 1], mat[sabz][2 + idx])
				(mat[ghermez][2 + idx] , mat[ghermez][2 + idx + 1]) = (mat[ghermez][2 + idx + 1], mat[ghermez][2 + idx])
				idx += 1
			if(abi < 13 and mat[abi + 1][2 + idx] != 0):
				if(sabz == 1 or sabz == 0):
					running = False
					print("Cant Place")

	elif action[x] == "Rotate":
		(mat[ghermez][2 + idx],mat[abi][2 + idx]) = (mat[abi][2 + idx],mat[ghermez][2 + idx])
		(mat[ghermez][2 + idx],mat[sabz][2 + idx]) = (mat[sabz][2 + idx],mat[ghermez][2 + idx])



	elif action[x] == "FREEZE":
		draw()
		while abi < 13 and mat[abi + 1][2 + idx] == 0:
			go_down()
			pygame.time.wait(500)
			draw()
		while(check_delete(mat) == 1 or check_down(mat) == 1):
			mat = delete(mat)
			mat = down(mat)

		sabz = 0
		ghermez = 1
		abi = 2


	else:
		color_m1 = action[x][0]
		color_m2 = action[x][1]
		color_m3 = action[x][2]
		if mat[2][2] == 0:
			mat[0][2] = color_m1
			mat[1][2] = color_m2
			mat[2][2] = color_m3
			idx = 0
		else:
			if 0 not in mat[2]:
				running = False
			else:
				rnd = random.randint(0,5)
				while(mat[2][rnd] != 0):
					rnd = random.randint(0,5)
				mat[0][rnd] = color_m1
				mat[1][rnd] = color_m2
				mat[2][rnd] = color_m3
				idx = rnd - 2


		sabz =  0
		ghermez = 1
		abi = 2





	draw()
	pygame.time.wait(500)
	go_down()


	x += 1













print()

for i in mat:
	print(i)


print()
print()
print()

print("YOUR SCORE :",score)
