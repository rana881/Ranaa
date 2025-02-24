
def tanh(x):
    return (2 / (1 + pow(2.718281828459045, -2 * x))) - 1  
def random_weight():
    seed = 42  
    seed = (seed * 1103515245 + 12345) % (2**31)  
    return (seed % 1000) / 1000 - 0.5  
W1 = [[random_weight(), random_weight()],  
      [random_weight(), random_weight()]]  

W2 = [[random_weight()], [random_weight()]]  
b1 = [0.5, 0.5]  
b2 = [0.7]       
X = [0.3, -0.2]  
z1 = [X[0] * W1[0][0] + X[1] * W1[1][0] + b1[0],  
      X[0] * W1[0][1] + X[1] * W1[1][1] + b1[1]] 
a1 = [tanh(z1[0]), tanh(z1[1])]
z2 = a1[0] * W2[0][0] + a1[1] * W2[1][0] + b2[0]
output = tanh(z2)
print("Output of the network:", output)
