import numpy as np


x = np.array([
    [8],
    [10],
    [12],
])


y = np.array([
    100, 150, 200  
])

xm = x.mean()
ym = y.mean()



DX = np.array([
    [x[0][0] - xm],
    [x[1][0] - xm],
    [x[2][0] - xm],
])


DY = np.array([
    [y[0] - ym],
    [y[1] - ym],
    [y[2] - ym],
])


PD = np.array([
    [DX[0][0] * DY[0][0]],
    [DX[1][0] * DY[1][0]],
    [DX[2][0] * DY[2][0]]
])


SP = np.sum(PD)

SX = np.array([
    [DX[0][0] ** 2],
    [DX[1][0] ** 2],
    [DX[2][0] ** 2]
])

SSX = np.sum(SX)

m=SP/SSX

b=ym - (m * xm)

# D = np.sum(DX * (y - ym)) / np.sum(DX ** 2)
print("Mean of x:", xm)
print("Mean of y:", ym)
print("Deviation of x (DX):", DX)
print("Deviation of y (DY):", DY)
print("Product of Deviations (PD):", PD)
print("Sum of Products (SP):", SP)
print("Squares of DX (SX):", SX)
print("Sum Squares of DX (SX):", SSX)
print("M is ",m)
print("B is ",b)

NewPizza=20

predicted_price = m * NewPizza + b

print(f"The predicted price of a pizza with {NewPizza} Inches is: ${predicted_price:.2f}")

# table of all pizza price
for i in range(len(x)):
    predicted_price = m * x[i][0] + b
    print(f"The predicted price of a pizza with {x[i][0]} Inches is: ${predicted_price:.2f}")