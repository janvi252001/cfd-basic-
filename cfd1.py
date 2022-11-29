import math 
import numpy as np
lx=1.0
ly=0.6
nx=1001
ny=586

dx=lx/(nx-1)
dy=ly/(ny-1)
#x=np.array(1,1001)
#y=np.array(1,586)
X=[]
Y=[]
x=0
y=0

for i in range(0, nx):
    X.append(x)
    x = x + dx

for i in range(0, ny):
    Y.append(y)
    y = y + dy

for i in range(0, nx):
    for j in range(0, ny):
        print(X[i], Y[j])

f = open(r"C:\Users\Adhya\Desktop\assig1.dat", "w")
f.write("TITLE = \"Grid Try 1\"\nVARIABLES = x, y\nZONE T = \"2D\", I = 1001, J = 586")
f.close()

f = open(r"C:\Users\Adhya\Desktop\assig1.dat", "a")
f.write("\n")

for j in range(0, ny):
    for i in range(0, nx):
        f.write(str(X[i]) + "\t" + str(Y[j]) + "\n")
        f.write(" ")
        f.write(str(Y[j]))
        f.write("\n")
f.close()
