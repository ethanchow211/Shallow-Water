import numpy as np
import matplotlib.pyplot as plt

X = 1000
dx = 0.05
x1 = -10
x2 = 10
x = np.linspace(x1,x2,X+1)
dt = 0.001
g = 9.81

gamma = 0.15
u = np.zeros((X+1,2))
h = np.zeros((X+1,2))
eta= np.zeros((X+1,2))
b=1/30*x
H = 1



for k in range(0,X+1):
    eta[k,0]= (2)*np.exp(-5*(x[k])**2) + H 


for t in range(15000):
    


    for i in range(0,X):
        
        dudx = g*((eta[i+1,0]) - (eta[i-1,0]))/(2*dx)
        du2dx2 = (u[i+1,0] -2*u[i,0] +u[i-1,0])/dx**2
        u[i,1] = u[i,0] - dt * (dudx)
        #u[i,1] = u[i,0] - dt * (dudx-gamma*du2dx2)
    u[0,1] = u[1,1]*0.9
    u[X,1] = u[X-1,1]*0.9

    for j in range(0, X):
        h = eta[j,0] - b[j]
        eta[j,1]= (-h*((u[j+1,1]-u[j-1,1])/(2*dx)))*dt + (eta[j+1,0] + eta[j-1,0])/2



        
    eta[0,1] = eta[1,1]*1
    eta[X,1] = eta[X-1,1]*1


    u[:,0] = np.copy(u[:,1])
    eta[:,0] = np.copy(eta[:,1])

    # Plot every few steps
    if t % 50 == 0:
        plt.cla()
        plt.plot(x, b)
        plt.plot(x, eta[:,0])
        plt.ylim(-0.2, 2)
        plt.xlabel("x")
        plt.ylabel("height")
        plt.pause(0.01)