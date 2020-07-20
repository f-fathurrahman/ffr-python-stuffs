import torch

torch.manual_seed(1234) # for reproducibility

#
# Prepare data
#
t_c = [0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0]
t_u = [35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4]
t_c = torch.tensor(t_c).unsqueeze(1)
t_u = torch.tensor(t_u).unsqueeze(1)

# Split into training and validation dataset
Nsamples = t_u.shape[0]
Nval = int(0.2*Nsamples) # for validation data

shuffled_indices = torch.randperm(Nsamples)
train_indices = shuffled_indices[:-Nval]
val_indices = shuffled_indices[-Nval:]

train_t_u = t_u[train_indices]
train_t_c = t_c[train_indices]

val_t_u = t_u[val_indices]
val_t_c = t_c[val_indices]

# scale
train_t_un = 0.1*train_t_u
val_t_un = 0.1*val_t_u

#
# Prepare model
#
linear_model = torch.nn.Linear(1,1)
print( linear_model(val_t_un) )

print( linear_model.weight )
print( linear_model.bias )

x = torch.ones(1)
print( linear_model(x) )

x = torch.ones(10, 1)
print( linear_model(x) )

optimizer = torch.optim.SGD(
    linear_model.parameters(),
    lr=1e-2
)

def training_loop(Nepochs, optimizer, model, loss_fn,
                   train_t_u, val_t_u, train_t_c, val_t_c):
    for epoch in range(1,Nepochs+1):
        
        train_t_p = model(train_t_u)
        train_loss = loss_fn(train_t_p, train_t_c)

        val_t_p = model(val_t_u)
        val_loss = loss_fn(val_t_p, val_t_c)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        if epoch == 1 or epoch % 100 == 0:
            print(f"Epoch {epoch:8d}, Training loss {train_loss.item():10.4f},"
                  f" Validation loss {val_loss.item():10.4f}")

def loss_fn(t_p, t_c):
    squared_diffs = (t_p - t_c)**2
    return squared_diffs.mean()

training_loop(
    3000, 
    optimizer,
    linear_model,
    loss_fn,
    train_t_un,
    val_t_un,
    train_t_c,
    val_t_c
)

