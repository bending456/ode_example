import numpy as np
########################################################################
def func1(y,t):
    
    k1 = 1
    k2 = 0.5
    k3 = 1.2
    k4 = 0.7
    k5 = 0.8
    k6 = 0.7
    
    dAdt = -k1*y[0] + k2*y[1]
    dBdt = -(k2+k3)*y[1] + k1*y[0] + k4*y[2]
    dCdt = -(k4+k5)*y[2] + k3*y[1] + k6*y[3]
    dDdt = -k6*y[3] + k5*y[2]
    
    dydt = [dAdt, dBdt, dCdt, dDdt]
    
    return dydt 

#########################################################################
def func2(y,t,k):
    
    k1 = k[0]
    k2 = k[1]
    k3 = k[2]
    k4 = k[3]
    k5 = k[4]
    k6 = k[5]
    
    dAdt = -k1*y[0] + k2*y[1]
    dBdt = -(k2+k3)*y[1] + k1*y[0] + k4*y[2]
    dCdt = -(k4+k5)*y[2] + k3*y[1] + k6*y[3]
    dDdt = -k6*y[3] + k5*y[2]
    
    dydt = [dAdt, dBdt, dCdt, dDdt]
    
    return dydt 

#########################################################################
def func3(y,t,k):
    
    A,B,C,D = y
    k1,k2,k3,k4,k5,k6 = k
    
    dAdt = -k1*A + k2*B
    dBdt = -(k2+k3)*B + k1*A + k4*C
    dCdt = -(k4+k5)*C + k3*B + k6*D
    dDdt = -k6*D + k5*C
    
    dydt = [dAdt, dBdt, dCdt, dDdt]
    
    return dydt 

##########################################################################
def func4(y,t,J):
    return np.dot(J,y)