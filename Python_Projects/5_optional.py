import numpy as np

n = int(input())
price = list(map(int, input().split()))

pmin=np.amin(price)
pmax=np.amax(price)
i=0
for i in range(n):
    if price[i]==pmin:
        a=True
        im=i+1

profit=pmax-pmin
print(profit)
print(im)


