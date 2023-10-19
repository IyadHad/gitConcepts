import numpy as np

def exo1():
	arr = []
	for i in range(0,21):
		arr.append(i)
	T = np.array(arr)
	for j in range(9,16):
		T[j]= T[j]*(-1)
	print(T)
	
def exo2():
	T=[]
	for i in  range(0,56):
		T.append(i)
	T = np.array(T)
	for i in range(14,55):
		print(T[i])

def exo3():
	T = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
	rows, columns = T.shape
	for i in range(0, rows):
		for j in range(0,columns):
			print(T[i,j])
		print("\n")

def exo4():
	T = np.linspace(5,50,10)
	print(T)

def exo5():
	random_vector = np.random.randint(0,11,size =5)
	T = np.array(random_vector)
	print (T)

def exo5():
	random_vector = np.arange(10, 22).reshape(3, 4)
	print (random_vector)

def exo6():
	random_matrix = np.arange(10,22).reshape(4,3)
	rows, columns = random_matrix.shape
	print(f"The number of rows is {rows} and the number of columns is {columns}")
	
def exo7():
	matrix = np.zeros((4,4), dtype=int)
	for i in range(0,4):
		for j in range (0,4):
			if i == j:
				matrix[i,j] = 0
			else:
				matrix[i,j]=1
	print (matrix)

def exo8():
	A1 = np.array([0,10,20, 40, 60])
	A2 = np.array([10, 30, 40])
	A = np.intersect1d(A1,A2)
	print(A)

def exo9():
	A1 = np.array([10,10,20,20,30,30])
	A = np.unique(A1)	
	print(A)

def exo10():
	A1 = np.array([ 0,10,20])
	A2 = np.array([10,10,20])
	A = np.cross(A1,A2)	
	print(A)

dico = {}
dico.keys()
dico.values()
dico.items()
exo10()