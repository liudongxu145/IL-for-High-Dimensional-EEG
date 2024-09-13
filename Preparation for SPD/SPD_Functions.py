import scipy
#using LogmTranfer, you can transform 3D data on SPD manifold into tangent space
def LogmTranfer(myRM):
    size1=len(myRM)
    size2=len(myRM[1])
    myRMlog=np.zeros((size1,size2,size2))
    for i in range(len(myRM)):
        myRMlog[i]=scipy.linalg.logm(myRM[i], disp=True)#
    return myRMlog
