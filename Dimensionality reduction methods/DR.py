# the size of input data is (N, d, d), the DR data is expected to (N, wantaftersize, wantaftersize)

# the process of PCA
from sklearn.decomposition import PCA
x_train=x_train.reshape(-1,d*d)
x_val=x_val.reshape(-1,d*d)
pca = PCA(n_components=wantaftersize*wantaftersize)
pca = pca.fit(x_train)
x_train_R = pca.transform(x_train)
x_val_R = pca.transform(x_val)

x_train_R=x_train_R.reshape(-1,wantaftersize,wantaftersize)
x_val_R=x_val_R.reshape(-1,wantaftersize,wantaftersize)


# LLE
from sklearn.manifold import LocallyLinearEmbedding
x_train=x_train.reshape(-1,d*d)
x_val=x_val.reshape(-1,d*d)
lle = LocallyLinearEmbedding(n_components=wantaftersize*wantaftersize, n_neighbors=10)
x_train_R = lle.fit_transform(x_train)
x_val_R =lle.transform(x_val)

x_train_R=x_train_R.reshape(-1,wantaftersize,wantaftersize)
x_val_R=x_val_R.reshape(-1,wantaftersize,wantaftersize)

#2DPCA
def PCA2D_2D(samples, row_top, col_top):
    '''samples are 3d matrices'''
    size = samples[0].shape
    # m*n matrix
    mean = np.zeros(size)

    for s in samples:
        mean = mean + s
    # get the mean of all samples
    mean /= float(len(samples))

    # n*n matrix
    cov_row = np.zeros((size[1],size[1]))
    for s in samples:
        diff = s - mean;
        cov_row = cov_row + np.dot(diff.T, diff)
    cov_row /= float(len(samples))
    row_eval, row_evec = np.linalg.eigh(cov_row)
    # select the top t evals
    sorted_index = np.argsort(row_eval)
    # using slice operation to reverse
    X = row_evec[:,sorted_index[:-row_top-1 : -1]]
    Z=X
    return X, Z
    
x_train=...   
X, Z = PCA2D_2D(x_train, wantaftersize, wantaftersize)
x_train_R=np.zeros((len(x_train),wantaftersize,wantaftersize))
for sz in range(len(x_train)):
    x_train_R[sz] = np.dot(Z.T, np.dot(x_train[sz], X))
    
x_val_R=np.zeros((len(x_val),wantaftersize,wantaftersize))
for sz in range(len(x_val)):
    x_val_R[sz] = np.dot(Z.T, np.dot(x_val[sz], X))



#B2DPCA-SPD under LEM
# LogmTranfer can be found in SPD_Functions.py
x_train=LogmTranfer(x_train)
x_val=LogmTranfer(x_val)
X, Z = PCA2D_2D(x_train, wantaftersize, wantaftersize)
x_train_R=np.zeros((len(x_train),wantaftersize,wantaftersize))
for sz in range(len(x_train)):
    x_train_R[sz] = np.dot(Z.T, np.dot(x_train[sz], X))
    
x_val_R=np.zeros((len(x_val),wantaftersize,wantaftersize))
for sz in range(len(x_val)):
    x_val_R[sz] = np.dot(Z.T, np.dot(x_val[sz], X))
