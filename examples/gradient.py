def loss(weight, x=2.0, target=6.0):
    return (weight*x-target)**2
def step(weight, lr):
    gradient = 2 * (weight*2-6) * 2
    return weight - lr*gradient
if __name__ == '__main__':
    for lr in (0.01, 1.0):
        updated = step(0, lr)
        print('learning rate', lr, 'before', loss(0), 'after', loss(updated))
