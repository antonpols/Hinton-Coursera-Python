import math


def sigmoid(z):
    return 1/(1+math.exp(-z))


x0 = 9
x1 = 4
x2 = -2

Wxh = 0.5
Whh = -1
Why = -0.7
hbias = -1
ybias = 0

z0 = Wxh*x0 + hbias
h0 = sigmoid(z0)
y0 = Why*h0 + ybias

z1 = Wxh*x1 + Whh*h0 + hbias
h1 = sigmoid(z1)
y1 = Why*h1 + ybias

z2 = Wxh*x2 + Whh*h1 + hbias
h2 = sigmoid(z2)
y2 = Why*h2 + ybias
print(h2)
