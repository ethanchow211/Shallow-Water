import numpy as np
import matplotlib.pyplot as plt

X = 1000
dx = 0.1
x1 = -10
x2 = 10
x = np.linspace(x1,x2,X+1)

g = 9.81

gamma = 0
u = np.zeros((X+1,2))
h = np.zeros((X+1,2))
eta= np.zeros((X+1,2))

b=  0.05*np.sin(2*x)+(1/26*x) +0.5
# b=0.1*np.ones((X+1))
H = 1

dt=(dx/np.sqrt(g*H))/8


for k in range(0,X+1):
    eta[k,0]= (2)*np.exp(-5*(x[k])**2) + H 

plt.plot(x,b)
plt.show()
for t in range(18000):
    


    for i in range(0,X):
        
        dudx = g*((eta[i+1,0]) - (eta[i-1,0]))/(2*dx)
        du2dx2 = (u[i+1,0] -2*u[i,0] +u[i-1,0])/dx**2
        # u[i,1] = u[i,0] - dt * (dudx)
        u[i,1] = u[i,0] - dt * (dudx-gamma*du2dx2)
    u[0,1] = u[1,1]*0.9
    u[X,1] = u[X-1,1]*0.9

    for j in range(0, X):
        h = eta[j,0] - b[j] 
        eta[j,1]= ((-h*((u[j+1,1]-u[j-1,1])/(2*dx)))*dt + (0.5*(eta[j+1,0]+eta[j,0]) + 0.5*(eta[j-1,0]+eta[j,0]))/2)
        

    

        
    eta[0,1] = eta[1,1]*1
    eta[X,1] = eta[X-1,1]*1


    u[:,0] = np.copy(u[:,1])
    eta[:,0] = np.copy(eta[:,1])

    # Plot every few steps
    if t % 30 == 0:
        plt.cla()
        plt.plot(x, b,color='brown')
        plt.plot(x, eta[:,0],color='blue')
        plt.title('Shallow Water Equations Variant Sloped Bottom')
        plt.legend(["ηb(x)", "η(x,t)"])
        plt.ylim(-0.2, 2)
        plt.xlabel("x")
        plt.ylabel("height")
        plt.pause(0.01)

