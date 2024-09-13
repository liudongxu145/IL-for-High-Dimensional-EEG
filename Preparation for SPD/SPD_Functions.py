import scipy
import numpy as np
import pyriemann

#using RM_M_G, you can transform the time series EEG signal to SPD matrices
#the shape 0f data (N, n, len)   N is the number of samples, n is channels of EEG data, len is the length of EEG data
def RM_M_G(data):
    size1=len(data)
    size2=len(data[1])
    RM_M=np.zeros((size1,size2,size2))
    for i in range(size1):
        tmp=data[i]
        #1280 here is the len, you can change it base on the shape of your EEG data.
        rmdata=np.dot(tmp,tmp.T)/(1280-1)+1e-9
        RM_M[i]=rmdata
    return RM_M

#you can also use another version of RM_M_G
def RM_M_G(data):
    RM_M=pyriemann.estimation.Covariances('scm').fit_transform(data)
    return RM_M

#using LogmTranfer, you can transform 3D data on SPD manifold into tangent space
#the shape of input 3D data (N,d,d) N is the number of samples, d is the the size of SPD matrix
def LogmTranfer(mySPDdata):
    Dimension_1=len(mySPDdata)
    Dimension_2=len(mySPDdata[1])
    myRMlog=np.zeros((Dimension_1,Dimension_2,Dimension_2))
    for i in range(len(mySPDdata)):
        myRMlog[i]=scipy.linalg.logm(mySPDdata[i], disp=True)#
    return myRMlog
