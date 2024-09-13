# Incremental-Classification-for-High-Dimensional-EEG-Manifold-Representation
Incremental Classification for High-Dimensional EEG Manifold Representation Using Bidirectional Dimensionality Reduction and Prototype Learning

# Innovations and major contributions will be updated soon.

## Preparation for SPD
This directory introduces the method of converting EEG signals into SPD matrices and how to map data on the SPD manifold into the tangent space.

## Dimensionality reduction methods
This directory introduces four dimensionality reduction methods, including principal component analysis (PCA), two-dimensional principal component analysis (2DPCA), locally linear embedding (LLE) and B2DPCA-SPD.

## Incremental dimensionality reduction methods
This directory introduces the specific code of IB2DPCA-SPD we proposed, and provides an example verified by random data. IB2DPCA-SPD can achieve lossless increment, which is consistent with the experimental results of batch B2DPCA.

## Classification Method on SPD manifold

This directory introduces four classification methods on SPD manifolds and their implementation codes, namely MDRM, FgMDRM, SPD-Net and MF-GNG.
