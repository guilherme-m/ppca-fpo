def criar_restricoes(solver, X, Y, A, D):
    for j in range(X.shape[1]):
        solver.Add(X[:, j].sum() <= D['limite'][j])
    
    for i in range(X.shape[0]):
        solver.Add(Y[i] <= X[i, :].sum())