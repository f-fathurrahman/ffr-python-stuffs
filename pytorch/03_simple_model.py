# Handwritten-gradient

import torch

def model(t_u, w, b):
    return w*t_u + b

def dmodel_dw(t_u, w, b):
    return t_u

def dmodel_db(t_u, w, b):
    return 1.0

def loss_fn(t_p, t_c):
    s = (t_p - t_c)**2
    return s.mean()

def dloss_fn(t_p, t_c):
    dsq_diffs = 2*(t_p - t_c)/t_p.size(0)
    return dsq_diffs

# Gradient of the loss function wrt w and b
def grad_fn(t_u, t_c, t_p, w, b):
    dloss_dtp = dloss_fn(t_p, t_c)
    dloss_dw = dloss_dtp * dmodel_dw(t_u, w, b)
    dloss_db = dloss_dtp * dmodel_db(t_u, w, b)
    return torch.stack([dloss_dw.sum(), dloss_db.sum()])

# Data
t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]
t_c = torch.tensor(t_c)
t_u = torch.tensor(t_u)

# Initial model parameters
w = torch.ones(())
b = torch.zeros(())

t_p = model(t_u, w, b)
loss = loss_fn(t_p, t_c)
grad = grad_fn(t_u, t_c, t_p, w, b)


def training_loop(Nepochs, learning_rate, params, t_u, t_c):
    for epoch in range(1,Nepochs+1):
        w, b = params
        t_p = model(t_u, w, b)
        loss = loss_fn(t_p, t_c)
        grad = grad_fn(t_u, t_c, t_p, w, b)
        # Update parameters
        params = params - learning_rate*grad
        #
        print("Epoch %8d, Loss %18.10f " % (epoch, float(loss)))
        print("updated params = ", params)
        print("grad           = ", grad)
    return params

# Stable and slow
#sprint("\nTry 1\n")
#training_loop(
#    Nepochs=100,
#    learning_rate=1e-4,
#    params=torch.tensor([1.0, 0.0]),
#    t_u=t_u,
#    t_c=t_c
#)

# Using normalized/scaled input
print("\nUsing scaled input\n")
t_un = 0.1*t_u
params = training_loop(
    Nepochs=5000,
    learning_rate=1e-2,
    params=torch.tensor([1.0, 0.0]),
    t_u=t_un,
    t_c=t_c
)
print("params = ", params)
#t_p = model(t_un, *params)
#import matplotlib.pyplot as plt
#plt.clf()
#plt.plot( t_u.numpy(), t_p.detach().numpy() ) # linear
#plt.plot( t_u.numpy(), t_c.numpy(), "o")
#plt.xlabel("Temperature (°Fahrenheit)")
#plt.ylabel("Temperature (°Celsius)")
#plt.savefig("IMG_03_simple_model.pdf")
