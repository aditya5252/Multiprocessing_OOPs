import numpy as np
import matplotlib.pyplot as plt

def upwind_data(linear,init,c,ntime,N_x,delt,delx):
    data_ls=[]
    u=init
    if ((linear == True) and (c>0)): ## Apply B.D. with preiodic boundary conditions
        for step in range(ntime):
            data_ls.append(u) # At t = 0 ,step = 0  At t = ntime-1 , step = ntime-1
            unew=u.copy() 
            for i in range(1,N_x-1):
                unew[i]=u[i] + delt*( -c*(u[i]-u[i-1])/delx )  ## B.D. model
            unew[0]=u[0] + delt*( -c*(u[0]-u[N_x-2]) )
            unew[N_x-1]=unew[0] 
            u=unew

    elif ((linear == True) and (c<=0)): ## Apply F.D. with preiodic boundary conditions
        for step in range(ntime):
            data_ls.append(u) # At t = 0 ,step = 0  At t = ntime-1 , step = ntime-1
            unew=u.copy() 
            for i in range(1,N_x-1):
                unew[i]=u[i] + delt*( -c*(u[i+1]-u[i])/delx )  ## F.D. model
            unew[0]=u[0] + delt*( -c*(u[1]-u[0])/delx )
            unew[N_x-1]=unew[0] 
            u=unew
    else:
        print(c)
        for step in range(ntime):
            data_ls.append(u) # At t = 0 ,step = 0  At t = ntime-1 , step = ntime-1
            unew=u.copy()
            for i in range(1,N_x-1):
                if u[i]>0:
                    unew[i]=u[i] + delt*( -u[i]*(u[i]-u[i-1])/delx)
                else:
                    unew[i]=u[i] + delt*( -u[i]*(u[i+1]-u[i])/delx)
            if u[0]>0:
                unew[0]=u[0] + delt*( -u[0]*(u[0]-u[N_x-2])/delx)
            else:
                unew[0]=u[0] + delt*( -u[0]*(u[1]-u[0])/delx ) 
                
            unew[N_x-1]=unew[0]   
            u=unew
    data_sol=np.stack(data_ls)
    return data_sol
