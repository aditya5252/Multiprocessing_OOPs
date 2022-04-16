import numpy as np
import matplotlib.pyplot as plt
def CD2_data(linear,init,c,ntime,N_x,delt,delx):
    data_ls=[]
    u=init
    if linear == True: 
        for step in range(ntime):
            data_ls.append(u) # At t = 0 ,step = 0  At t = ntime-1 , step = ntime-1
            unew=u.copy() 
            for i in range(1,N_x-1):
                unew[i]=u[i] + delt*( -c*(u[i+1]-u[i-1])/delx )  ## B.D. model
            unew[0]=u[0] + delt*( -c*(u[1]-u[N_x-2]) )
            unew[N_x-1]=unew[0] 
            u=unew
    elif linear == False:
        pass
    data_sol=np.stack(data_ls)
    return data_sol
