import numpy as np

def criar_restricoes(solver, X, Y, A, D):
    # limite de vagas por disciplina
    for j in range(X.shape[1]):
        solver.Add(X[:, j].sum() <= D['limite'][j])
    
    # maximização do número de alunos matriculados
    for i in range(X.shape[0]):
        solver.Add(Y[i] <= X[i, :].sum())
    
    for g, df in D.groupby('horario'):
        if len(df) > 1:
            for i in range(X.shape[0]):
                solver.Add(X[i, df['index']].sum() <= 1)