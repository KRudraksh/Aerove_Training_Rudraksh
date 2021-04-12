import numpy as np
x=np.random.normal(size=(20,20))
y = np.ones([20], dtype='int32')
for i in range(20):
    y[i]=(float(input("Element:")))

c=x.transpose()
z=np.matmul(c,x)
a=np.linalg.inv(z)
b=np.matmul(a,c)
theta=np.matmul(b,y)

print(theta)
