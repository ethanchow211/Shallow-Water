import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

X = 100
dx = 0.1
dy=0.1
x1 = -10
x2 = 10
x = np.linspace(x1,x2,X+1)
y = np.linspace(x1,x2,X+1)
g = 9.81
Xgrid,Ygrid = np.meshgrid(x,y)
gamma = 0.15
u = np.zeros((X+1,X+1,2))
eta= np.zeros((X+1,X+1,2))
v= np.zeros((X+1,X+1,2))
# b=0.1*np.ones((X+1,X+1))*(1/3)*x +0.5
b=0.1*np.ones((X+1,X+1)) *np.sin(Xgrid) +(1/26)*x +0.5
# b=(1/10)*np.sin(x)
H = 1

dt=(dx/np.sqrt(g*H))/15

eta[:,:,0]= 30*np.exp(-5*(Xgrid**2 + Ygrid**2)) + H








plt.ion()
fig = plt.figure(figsize=(10, 5))
ax=fig.add_subplot(1,2,1, projection='3d')
ax.title.set_text('2D Shallow Water Equations with Variant Slope Bottom')
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.title.set_text('Zoomed In (Shrunken Z Axis)')

plt.pause(8)


for t in range(3000):
    


    for i in range(0,X):
        
        dvdy = g*((eta[:,i+1,0]) - (eta[:,i-1,0]))/(2*dy)
        v[:,i,1] = v[:,i,0] - dt * (dvdy)

        dudx = g*((eta[i+1,:,0]) - (eta[i-1,:,0]))/(2*dx) 
        u[i,:,1] = u[i,:,0] - dt * (dudx)


        
    u[0,:,1] = u[1,:,1]*0.9
    u[X,:,1] = u[X-1,:,1]*0.9
    v[:,0,1] = v[:,0,1]*0.9
    v[:,X,1] = v[:,X-1,1]*0.9
    for l in range(0,X):
        for j in range(0, X):
            h = eta[j,l,0] - b[j,l]
            eta[j,l,1]= (-h*((u[j+1,l,1]-u[j-1,l,1])/(2*dx)))*dt \
                + (-h*((v[j,l+1,1]-v[j,l-1,1])/(2*dy)))*dt  \
                    + 0.5*(((0.5* (eta[j+1,l,0]+eta[j,l,0]) + 0.5* (eta[j-1,l,0]+eta[j,l,0]) )/2) \
                           + ((0.5* (eta[j,l+1,0]+eta[j,l,0]) + 0.5* (eta[j,l-1,0]+eta[j,l,0]) )/2))

    
    
        
    eta[0,:,1] = eta[1,:,1]
    eta[X,:,1] = eta[X-1,:,1] 
    eta[:,0,1] = eta[:,1,1]
    eta[:,X,1] = eta[:,X-1,1]   
    
    v[:,:,0] = np.copy(v[:,:,1])
    u[:,:,0] = np.copy(u[:,:,1])
    eta[:,:,0] = np.copy(eta[:,:,1])
    

    
    if t % 30 == 0:
        
        ax.title.set_text('2D Shallow Water Equations with Variant Slope Bottom')

        ax2.title.set_text('Zoomed In (Shrunken Z Axis)')
        ax.plot_surface(Xgrid,Ygrid,b,cmap='copper')
        ax.plot_surface(Xgrid,Ygrid,eta[:,:,0],cmap='Blues_r',vmin=0.98,vmax=1.2)
       
        ax.set_xlim3d(-10, 10)
        ax.set_ylim3d(-10, 10)
        ax.set_zlim3d(0, 1.1)
        ax2.plot_surface(Xgrid,Ygrid,eta[:,:,0],cmap='Blues_r',vmin=0.98,vmax=1.2)
        ax.set_xlim3d(-10, 10)
        ax.set_ylim3d(-10, 10)
        ax2.set_zlim3d(0.9, 1.1)

        
        plt.pause(0.0001)
        ax.clear()
        ax2.clear()
       
