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
x_train_R=PCA2Dfor3DimData(x_train,wantaftersize)
    
    X, Z = PCA2D_2D(x_train, wantaftersize, wantaftersize)
    x_val_R=np.zeros((len(x_val),wantaftersize,wantaftersize))
    for sz in range(len(x_val)):
        x_val_R[sz] = np.dot(Z.T, np.dot(x_val[sz], X))

    x_train_R = x_train_R.reshape((x_train_R.shape[0], x_train_R.shape[1], x_train_R.shape[2], 1))
    # print(x_train_R.shape)
    x_val_R = x_val_R.reshape((x_val_R.shape[0], x_val_R.shape[1], x_val_R.shape[2], 1))
    
    x_test_R2=np.zeros((len(XTEST2),wantaftersize,wantaftersize))
    for sz in range(len(XTEST2)):
        x_test_R2[sz] = np.dot(Z.T, np.dot(XTEST2[sz], X))
    x_test_R2 =x_test_R2 .reshape((x_test_R2.shape[0], x_test_R2.shape[1], x_test_R2.shape[2], 1))


