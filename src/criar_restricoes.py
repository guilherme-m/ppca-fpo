def criar_restricoes(solver, X, A, D):
    for j in range(X.shape[1]):
        solver.Add(X[:, j].sum() <= D['limite'][j])