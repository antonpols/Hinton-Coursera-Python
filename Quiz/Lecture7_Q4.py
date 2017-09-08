import math


def sigmoid(z):
    return 1/(1+math.exp(-z))


x0 = 18
x1 = 9
x2 = -8

t0 = 0.1
t1 = -0.1
t2 = -0.2

Wxh = -0.1
Whh = 0.5
Why = 0.25
hbias = 0.4
ybias = 0.0

z0 = Wxh*x0 + hbias
h0 = sigmoid(z0)
y0 = Why*h0 + ybias
print(h0, y0)

z1 = Wxh*x1 + Whh*h0 + hbias
h1 = sigmoid(z1)
y1 = Why*h1 + ybias
print(h1, y1)

z2 = Wxh*x2 + Whh*h1 + hbias
h2 = sigmoid(z2)
y2 = Why*h2 + ybias
print(h2, y2)

# h0 = 0.2
# h1 = 0.4
# h2 = 0.8
#
# y0 = 0.05
# y1 = 0.1
# y2 = 0.2

dE1_dz1 = -(t1-y1) * Why * h1*(1-h1)
dE2_dz1 = -(t2-y2) * Why * h2*(1-h2) * Whh * h1*(1-h1)

dE_dz1 = dE1_dz1 + dE2_dz1
print(dE_dz1)
